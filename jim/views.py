from flask import render_template, request, Response
from . import application
import requests
import json
import os

SLACK_BOT_OAUTH_TOKEN = os.environ['SLACK_BOT_OAUTH_TOKEN']

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/slack', methods=['POST'])
def inbound():

    user_id = request.form['user_id']
    channel_id = request.form['channel_id']
    response_url = request.form['response_url']
    slash_message_text = request.form['text']
    commands = ["$5"]

    if slash_message_text in commands:
        escaped_channelid = '<@%s>' % (channel_id)
        escaped_userid = '<@%s>' % (user_id)

        response_dict = {
            "response_type": "in_channel",
            "text": "<!channel> " +  escaped_userid + "CAN'T MAKE IT TO THE GYM TODAY $5!!"
        }
        headers = {'content-type': 'application/json'}
        
        r = requests.post(response_url, headers=headers, data=json.dumps(response_dict))
        
        return("",200)
    else:
        return("Sorry i'm not programmed for that commad", 500)