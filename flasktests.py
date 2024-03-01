import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("index.html")

@app.rout('/login')
def handle_login():
    form_data = flask.request
    campus_id = form_data["campus_id"]
    if authenticate_user(campus_id):
        return flask.redirect(flask.url_for("welcome_page"))
    else:
        flask.flash("The campus ID that you entered was incorrect. Please try again.")
        return flask.redirect(flask.url_for("index"))
        
@app.route("/welcome")
def welcome_page():
    return flask.render_template("welcome.html")
    
def authenticate_user(login_campus_id):
    return login_campus_id == "random_user876"
        

app.run(debug = True)