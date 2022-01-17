from flask import Flask, render_template, url_for

import rovers

app = Flask(__name__)  # this way it knows where to find static files etc


# just a quick test
def get_image():
    cure = rovers.Curiosity()
    response = cure.query_by_camera_and_earthdate("FHAZ", "2015-6-3")
    first_image = cure.return_first_image(response)
    return first_image


@app.route("/")
@app.route("/home")
def home():  # put application's code here
    return render_template("home.html", image=get_image())


@app.route("/about")
def about():  # put application's code here
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(debug=True)
    app.run()
