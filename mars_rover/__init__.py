from flask import Flask

app = Flask(__name__)  # this way it knows where to find static files etc
app.config["SECRET_KEY"] = "66d40d5fbcd28ca752f7df2f"  # set as an env var later

from mars_rover import routes
