import requests
from datetime import datetime


class Rover:
    def __init__(self):
        self.api_key = ""
        self.host = "https://mars-photos.herokuapp.com/api/v1/rovers/"
        self.cameras = []
        self.rover_name = ""
        self.landing_date = ""
        self.last_date = ""

    def check_date(self, requested_date):
        if isinstance(requested_date, str):
            return False
        if self.last_date == "":
            self.last_date = datetime.now()
            self.last_date = datetime.date(self.last_date)
        self.landing_date = datetime.date(self.landing_date)
        if self.landing_date < requested_date < self.last_date:
            return requested_date
        else:
            return False

    def query_by_camera_and_earthdate(self, camera, date):
        try:
            # check that the camera requested exists for the specific rover
            if not self.cameras:
                raise Exception(
                    "Camera list not specified. Have you set the available cameras?"
                )
            else:
                if camera in self.cameras:
                    # :TODO: is there a better way to construct the query? we don't want to hardcode earth_date etc
                    our_request = (
                        self.host
                        + self.rover_name
                        + "/photos?&earth_date="
                        + str(date)
                        + "/&camera="
                        + camera
                    )
                    answer = (requests.get(our_request)).json()
                    return answer
        # some error handling so we know what the problem is each time
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def return_first_image(self, request_result):
        """
        :rtype: object
        """
        # this isn't the best, the loop stops at the first row so we grab the first image.
        # later we probably want to be able to return all the images, but that's easy enough.
        for i in request_result["photos"]:
            return i["img_src"]


class Perseverance(Rover):
    def __init__(self):
        super().__init__()
        # each rover has a distinct set of cameras
        self.cameras = [
            "EDL_RUCAM",
            "EDL_RDCAM",
            "EDL_DDCAM",
            "EDL_PUCAM1",
            "EDL_PUCAM2",
            "NAVCAM_LEFT",
            "NAVCAM_RIGHT",
            "MCZ_RIGHT",
            "MCZ_LEFT",
            "FRONT_HAZCAM_LEFT_A",
            "FRONT_HAZCAM_RIGHT_A",
            "REAR_HAZCAM_LEFT",
            "REAR_HAZCAM_RIGHT",
            "SKYCAM",
            "SHERLOC_WATSON",
        ]
        self.rover_name = "perseverance"
        self.landing_date = datetime(2021, 2, 18)


class Curiosity(Rover):
    def __init__(self):
        super().__init__()
        # each rover has a distinct set of cameras
        self.cameras = [
            "FHAZ",
            "RHAZ",
            "MAST",
            "CHEMCAM",
            "MAHLI",
            "MARDI",
            "NAVCAM",
        ]
        self.rover_name = "curiosity"
        self.landing_date = datetime(2012, 8, 6)


class Opportunity(Rover):
    def __init__(self):
        super().__init__()
        # each rover has a distinct set of cameras
        self.cameras = [
            "FHAZ",
            "RHAZ",
            "MAST",
            "CHEMCAM",
            "MAHLI",
            "MARDI",
            "NAVCAM",
        ]
        self.rover_name = "opportunity"
        self.landing_date = datetime(2004, 1, 25)
        self.last_date = datetime(2018, 6, 10)


class Spirit(Rover):
    def __init__(self):
        super().__init__()
        # each rover has a distinct set of cameras
        self.cameras = [
            "FHAZ",
            "RHAZ",
            "MAST",
            "CHEMCAM",
            "MAHLI",
            "MARDI",
            "NAVCAM",
        ]
        self.rover_name = "spirit"
        self.landing_date = datetime(2004, 1, 4)
        self.last_date = datetime(2010, 3, 22)
