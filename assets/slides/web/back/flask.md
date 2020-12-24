# Flask

Provides annotations mapping URL paths to Python function
Every URL for which you want the server to respond requires an annotation/function combination.

$ python flaskpage.py  →  http://127.0.0.1:5000/ 
```flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"

app.run()
```

http://127.0.0.1:5000/index
http://127.0.0.1:5000/index/Adam
http://127.0.0.1:5000/data?format=idontknow
```flask
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