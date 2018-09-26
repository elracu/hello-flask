from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit"/>
        </form>
    </body>
</html>
"""


#@app.route in the parent directory ("/") runs function def index() which loads form

@app.route("/")
def index():
    return form

#@app.route in the /hello subdirectory has used a post method from the form and renders a string of html + user input  

@app.route ("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    #used cgi.escape to render any html or javascript entered maliciously as content
    return '<h1>Hello, ' + cgi.escape (first_name) + '</h1>'




app.run()