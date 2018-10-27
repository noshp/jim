from flask import render_template, request, Response, jsonify
from . import application, db
import requests
import json
import os
from sqlalchemy import func
from jim.models import Log

#SLACK_BOT_OAUTH_TOKEN = os.environ['SLACK_BOT_OAUTH_TOKEN']

#Helper functions
def get_stats():
    statQuery = db.session.query(Log.user_id, func.count(Log.user_id)).group_by(Log.user_id).all()
    return_string = "Current stats: \n"
    for stat in statQuery:
        return_string += '<@%s>: $%s \n' % (stat[0], str(stat[1] * 5))
    return return_string

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/slack', methods=['POST'])
def inbound():

    user_id = request.form['user_id']
    channel_id = request.form['channel_id']
    response_url = request.form['response_url']
    slash_message_text = request.form['text']
    commands = ["$5", "stats"]

    if slash_message_text in commands:

        if slash_message_text == "$5":
            escaped_channelid = '<@%s>' % (channel_id)
            escaped_userid = '<@%s>' % (user_id)

            response_dict = {
                "response_type": "in_channel",
                "text": "<!channel> " +  escaped_userid + "CAN'T MAKE IT TO THE GYM TODAY $5!!"
            }
            headers = {'content-type': 'application/json'}
            
            r = requests.post(response_url, headers=headers, data=json.dumps(response_dict))
            
            return("",200)
        elif slash_message_text == "stats":
            stats_string = get_stats()
            response_payload = {
                "response_type" : "in_channel",
                "text": stats_string
            }
            headers = {'content-type': 'application/json'}
            r = requests.post(response_url, headers=headers, data=json.dumps(response_payload))
            return("", 200)
            
    else:
        return("Sorry i'm not programmed for that commad", 500)

@application.route('/stats', methods=['GET'])
def stats():
    statQuery = db.session.query(Log.user_id, func.count(Log.user_id)).group_by(Log.user_id).all()
    return_payload = []
    for stat in statQuery:
        return_payload.append({
            "user_id": stat[0],
            "total_contribution": stat[1] * 5
        })
    return(jsonify({"current_stats": return_payload}),200)