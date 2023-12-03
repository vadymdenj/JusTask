from ntpath import join
from tkinter import Entry
from dao import add_event, get_event
from flask import Flask, render_template, jsonify, request
from app.utils.auth_utils import get_token
from flask_cors import CORS

from scheduling_alg import fastest_travel


# Create the Flask app with the template folder specified that will contain your index.html and static folder which will contain your JavaScript files
app = Flask(__name__, template_folder='app/templates', static_url_path='/static')
# By adding CORS(app), you are telling Flask to include CORS headers in responses. The flask_cors extension will add headers such as Access-Control-Allow-Origin: *, allowing requests from any origin.
# This way, when your frontend makes requests to your Flask server, the server will respond with the appropriate CORS headers, and the browser will permit the requests. Since the frontend and backend are on the same origin (domain), you won't encounter CORS issues.
# For more info on CORS goto: https://www.bannerbear.com/blog/what-is-a-cors-error-and-how-to-fix-it-3-ways/
CORS(app)
app.debug=False
# This is the route that will serve your index.html template
@app.route('/')
def index():
    return render_template('index.html')

# This is the route that will help you get the token and return it as a JSON response
@app.route('/getToken', methods=['GET'])
def display_token():
    # This makes the call to the get_token function in the auth_utils.py file
    response, status_code = get_token()
    # If the request is successful, return the token
    if status_code == 200:
        api_token = response
        return jsonify({'message': api_token})
    #If the request fails, return the error message
    else:
        return jsonify({'message': response})

# This is the route that will help you get the token and return it as a JSON response
@app.route('/fastestTravel', methods=['GET'])
def fastest_travel_endPoint():
    # event = {"name": eventName, "start": eventStart, "end": eventEnd, "address": eventAddress}
    # task = {"name":"Grocery Shopping","duration":30, "address":"2901 Pacific Ave San Francisco, CA 94115"}

    body = request.json
    calendar = get_event('santiago')
    calendars = [calendar,calendar,calendar]
    print(calendars)
    task = {"name": body['eventName'],"duration":body['eventDuration'], "address":body['eventAddress']}
    addedFlexibleEvent = fastest_travel(task, calendars)
    # calendar=[event,event,event]
    # if addedFlexibleEvent:
        # If successful, return a success response
    response = {'message': 'Event added successfully', 'addedFlexibleEvent': addedFlexibleEvent}
    return jsonify(response), 200
    # else:
    #     # If there was an error, return an error response
    #     response = {'message': 'Failed to add event'}
    #     return jsonify(response), 500

# @app.route('/add_event', methods=['PUT'])
# def fastest_travel_endPoint():
#     userId = request.args.get('userId')
#     eventName = request.args.get('eventName')
#     eventAddress = request.args.get('eventAddress')
#     eventStartTime = request.args.get('eventStartTime')
#     eventEndTime = request.args.get('eventEndTime')
#     eventIsFlexible = request.args.get('eventIsFlexible')

#     add_event(userId, eventName, eventAddress, eventIsFlexible, eventStartTime, eventEndTime, eventEndTime-eventStartTime)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
