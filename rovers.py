import json

import requests
from json import loads


class Rover:
    def __init__(self):
        self.api_key = ""
        self.host = "https://mars-photos.herokuapp.com/api/v1/rovers/"
        self.cameras = []
        self.rover_name = ""

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
                            + date
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


class Curiosity(Rover):
    def __init__(self):
        super().__init__()
        # each rover has a distinct set of cameras
        self.cameras = ["NAVCAM", "FHAZ", "fAVCAM"]  # :TODO: add all cameras and rovers
        self.rover_name = "curiosity"


"""
c = Curiosity()
info = c.query_by_camera_and_earthdate("FHAZ", "2015-6-3")
c.return_first_image(info)
"""
