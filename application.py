from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")

@application.route("/help")
def helppage():
    return render_template("help.html")

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------