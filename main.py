from flask import Flask, request, redirect
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

time_form = """
<style>
    .error {{color: red;}}
</style>
<h1>Validate Time</h1>
<form method="POST">
    <label> Hours (24-hour format)
        <input name="hours" type="text" value='{hours}'/>
    </label>
    <p class="error">{hours_error}</p>

    <label> Minutes
            <input name="minutes" type="text" value='{minutes}'/>
        </label>
        <p class="error">{minutes_error}</p>
        
    <input type="submit" value="Validate" />
</form>
"""


#@app.route in the parent directory ("/") runs function def index() which loads form

@app.route("/")
def index():
    return form

#@app.route in the /hello subdirectory has used a post method from the "form" and renders a string of html + user input  

@app.route ("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    #used cgi.escape to render any html or javascript entered maliciously as content
    return '<h1>Hello, ' + cgi.escape (first_name) + '</h1>'

#app.routes in the /validate-time subdirectory below are specific to the "time_form" above

#app.route in the /validate-time subdirectory below renders the "time_form" above with empty values

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')

#validate wether hours and minutes submitted can be converted to a string

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

#app.route in the /validate-time subdirectory below has used a post method from the "time_form" and validates submissions

@app.route('/validate-time', methods=['POST'])
def validate_time():

    #values from form
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error =''
    minutes_error = ''

    #check if submitted values are valid integers
    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours =''
    #if yes check if it's within range
    else:
        hours = int(hours)
        if hours > 23 or hours <0:
            hours_error = 'Hour value out of range (0-23)'
            hours =''

    #check if submitted values are valid integers
    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes =''
    #if yes check if it's within range
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes <0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes =''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))

    #display form with correct values (if any) and error messages
    else:
        return time_form.format(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

#app.route in the /valid-time subdirectory below renders a string of html + user input

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)


app.run()