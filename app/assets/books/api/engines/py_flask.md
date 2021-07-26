# Flask

Provides annotations mapping URL paths to Python function
Every URL for which you want the server to respond requires an annotation/function combination.

$ python flaskpage.py  →  http://127.0.0.1:5000/ 

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"

app.run()
```


server.py 
```py
from flask import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
```

http://127.0.0.1:5000/index
http://127.0.0.1:5000/index/Adam
http://127.0.0.1:5000/data?format=idontknow
```python
from flask import Flask
from flask import request
app = Flask(__name__)

page = '''
<html>
<body>
<h1> Hello Flask </h1>
<p> This is an instance of the flask page. </p>
<li><a href="index/Sue"> Sue </a></li>
<li><a href="index/Tom"> Tom </a></li>
<p>Click to get the data: 
<li><a href="data?format=txt">text</a></li>
<li><a href="data?format=html">html</a></li>
</p>
</body>
</html>
'''

mydata = """Sue, 10, 134.983
Tom, 11, 99.001
"""

mydata_html = """
<b>Sue</b>, 10, 134.983<br>
Tom, 11, 99.001
"""


@app.route("/")
def hello():
    return "Hello World!\n"

@app.route("/index")
def index():
    return page

@app.route("/index/<name>")
def hiname(name):
    return "Hello %s!\n" % name

@app.route("/data")
def foo():
    if request.args.get("format")=='txt':
        return mydata
    else:
        return mydata_html

app.run()
```


- https://py.plainenglish.io/abandoning-flask-for-fastapi-20105948b062




# Flask

http://flask.pocoo.org/
Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.

Flask is a microframework for developing web applications with the Python programming language. Flask lets us separate major sections of our application into "blueprints". Each blue box in the sketch represents a blueprint that will exist in our application. Let's elaborate on the function of each blueprint.

https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH


https://www.palletsprojects.com/p/werkzeug/
	HTTP header parsing and dumping
	Easy to use request and response objects
	Interactive JavaScript based in-browser debugger
	100% WSGI 1.0 compatible
	Supports Python 2.6, 2.7, 3.3, 3.4 and 3.5.
	Unicode support
	Basic session and signed cookie support
	URI and IRI utilities with unicode awareness
	builtin library of fixes for buggy WSGI servers and browsers
	integrated routing system for matching URLs to endpoints and vice versa

# WSGI utility library for Python.
  \___ Web Server Gateway Interface
		https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface
  		WSGI was thus created as an implementation-agnostic interface between web servers and web applications or frameworks to promote common ground for portable web application development
	Werkzeug is Simple
		from werkzeug.wrappers import Request, Response

		@Request.application
		def application(request):
		    return Response('Hello World!')

		if __name__ == '__main__':
		    from werkzeug.serving import run_simple
		    run_simple('localhost', 4000, application)

# Jinja 2 - templating language for Python, modelled after Django’s templates.
	http://jinja.pocoo.org/docs/2.10/  
	<title>{% block title %}{% endblock %}</title>
	<ul>
	{% for user in users %}
	  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
	{% endfor %}
	</ul>


# FLASK SETUP
> pip install Flask
> conda install flask

# FLASK APP

app.py
```py
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"
```

>flask run 						look for app.py or wsgi.py

>FLASK_APP=hello.py flask run
* Running on http://localhost:5000/

> set FLASK_APP=hello.py
> set FLASK_ENV=development
> flask run

>set FLASK_APP=C:\api\hello.py	    
>flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [16/Mar/2018 08:58:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [16/Mar/2018 08:58:01] "GET /favicon.ico HTTP/1.1" 404 -


# SAMPLES

env FLASK_APP=app.py FLASK_ENV=development flask run
```py
@app.route('/')
def home():
    return render_template("home.html")

	<!DOCTYPE html>
	<html>
	<head>
	  <meta charset="UTF-8">
	  <title>Predict Covid</title>
	<link type="text/css" rel="stylesheet" href="{{ url_for('static', filename='./style.css') }}">
	</head>
	<body>
	 <div class="page">
	     <form if="form" action="{{ url_for('predict')}}"method="POST">
	         <input type="text" name="country" placeholder="Country" required="required" /><br>
	         <h3 class='res'>{{pred}}</h3>
	         <button id="button" type="submit" class="btn btn-primary btn-block btn-large">Predict</button>
	        </form>
	 </div>
	</body>
	</html>    

@app.route('/predict',methods=['POST'])
def predict():
    input_val = [x for x in request.form.values()][0]
    rf = load_model(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
    if input_val not in available_countries:
        return f'Country {input_val} is not in available list. Try one from the list! Go back in your browser', 400
    to_pred = get_prediction_params(input_val, url_to_covid)
    prediction = rf.predict(to_pred)[0]
    return render_template('home.html',pred=f'New cases will be {prediction}')
```


# CORS

```py
	from flask import Flask, request
	from flask_cors import CORS   # pip install flask-cors
	from typing import List 

	if __name__ == '__main__"
		app = Flask(__name__)
		CORS(app)

	@app.route("/")

	def hello():
	  return "Hello World!"
```

## AUTH

https://www.loginradius.com/blog/async/guest-post/user-authentication-in-python/

```py
from flask import *
from LoginRadius import LoginRadius as LR

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

LR_AUTH_PAGE = "https://<APP_NAME>.hub.loginradius.com/auth.aspx?action={}&return_url={}"
LR.API_KEY = "LR_API_KEY"
LR.API_SECRET = "LR_API_SECRET"
loginradius = LR()


@app.route("/")
def index():
    return "Hello World!"


@app.route("/register/")
def register():
    # redirect the user to our LoginRadius register URL
    return redirect(LR_AUTH_PAGE.format("register", request.host_url[:-1] + url_for("login")))


@app.route("/login/")
def login():
    access_token = request.args.get("token")
    if access_token is None:
        # redirect the user to our LoginRadius login URL if no access token is provided
        return redirect(LR_AUTH_PAGE.format("login", request.base_url))

    # fetch the user profile details with their access tokens
    result = loginradius.authentication.get_profile_by_access_token(access_token)

    if result.get("ErrorCode") is not None:
        # redirect the user to our login URL if there was an error
        return redirect(url_for("login"))

    session["user_acccess_token"] = access_token

    return redirect(url_for("dashboard"))


@app.route("/dashboard/")
def dashboard():
    access_token = session.get("user_acccess_token")
    if access_token is None:
        return redirect(url_for("login"))

    # fetch the user profile details with their access tokens
    result = loginradius.authentication.get_profile_by_access_token(access_token)

    if result.get("ErrorCode") is not None:
        # redirect the user to our login URL if there was an error
        return redirect(url_for("login"))

    return jsonify(result)


@app.route("/logout/")
def logout():
    access_token = session.get("user_acccess_token")
    if access_token is None:
        return redirect(url_for("login"))

    # invalidate the access token with LoginRadius API
    loginradius.authentication.auth_in_validate_access_token(access_token)
    session.clear()

    return "You have successfully logged out!"


if __name__ == "__main__":
    app.run(debug=True)
```