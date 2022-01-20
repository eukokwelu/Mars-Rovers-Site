from flask import Flask, render_template, url_for, flash, redirect
from forms import DateSubmissionForm
import rovers

app = Flask(__name__)  # this way it knows where to find static files etc

app.config["SECRET_KEY"] = "66d40d5fbcd28ca752f7df2f"  # set as an env var later


def get_info(selected_rover, date, camera="FHAZ"):
    if str(selected_rover) == "Curiosity":
        rover = rovers.Curiosity()
    elif selected_rover == "Perseverance":
        rover = rovers.Perseverance()
    else:
        raise AssertionError(f"Rover not available yet, you asked for {selected_rover}")
    #  check that the date is valid for the specified rover
    if rover.check_date(date):
        print(date)
        response = rover.query_by_camera_and_earthdate(camera, date)
        first_image = rover.return_first_image(response)
        return first_image


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():  # put application's code here
    form = DateSubmissionForm()
    if form.validate_on_submit():
        returned_image = get_info(form.Rover.data, form.Date.data)
        flash(f"Submitted!", "success")

        # return redirect(url_for('home'))
        return render_template("home.html", image=returned_image, form=form)
    return render_template("home.html", image="", form=form)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(debug=True)
    app.run()
