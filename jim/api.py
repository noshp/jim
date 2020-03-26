from flask import render_template, request, Response, jsonify, Blueprint
from jim import db
import requests
import random
import json
import os
from sqlalchemy import func
from jim.models import Log, ArchiveStats
from datetime import datetime

#SLACK_BOT_OAUTH_TOKEN = os.environ['SLACK_BOT_OAUTH_TOKEN']

api_blueprint = Blueprint('api', __name__, template_folder='./templates')
#Helper functions
def get_stats():
    statQuery = db.session.query(Log.user_id, func.count(Log.user_id)).group_by(Log.user_id).all()
    if len(statQuery) > 0:
        return_string = ""
        for stat in statQuery:
            return_string += '<@%s>: $%s \n' % (stat[0], str(stat[1] * 5))
        return return_string
    else:
        return "*Clean slate yall, let's keep it this way*"
        

def get_quote():
    rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    random_quote = random.choice(list(open(rootdir + '/quotes.txt')))
    return random_quote

@api_blueprint.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!' 
    })

@api_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api_blueprint.route('/api/slack', methods=['POST'])
def inbound():

    user_id = request.form['user_id']
    channel_id = request.form['channel_id']
    response_url = request.form['response_url']
    slash_message_text = request.form['text']
    commands = ["$5", "stats", "inspire me", "reset stats"]

    if slash_message_text in commands:

        if slash_message_text == "$5":
            escaped_channelid = '<@%s>' % (channel_id)
            escaped_userid = '<@%s>' % (user_id)
            
            enter_log = Log(user_id=user_id, date=datetime.now())
            try:
                db.session.add(enter_log)
                db.session.commit()
                db.session.close()
            except Exception as e:
                print(e)
                db.session.rollback()

            response_dict = {
                "response_type": "in_channel",
                "text": "<!channel> " +  escaped_userid + "CAN'T MAKE IT TO THE GYM TODAY $5!!"
            }
            headers = {'content-type': 'application/json'}
            
            r = requests.post(response_url, headers=headers, data=json.dumps(response_dict))
            
            return("",200)

        elif slash_message_text == "stats":
            stats_string = "Current stats: \n" + get_stats()
            response_payload = {
                "response_type" : "in_channel",
                "text": stats_string
            }
            headers = {'content-type': 'application/json'}
            r = requests.post(response_url, headers=headers, data=json.dumps(response_payload))
            return("", 200)
            
        elif slash_message_text == "inspire me":
            quote_string = get_quote()
            response_payload = {
                "response_type" : "in_channel",
                "text": ">" + quote_string
            }
            headers = {'content-type': 'application/json'}
            r = requests.post(response_url, headers=headers, data=json.dumps(response_payload))
            return("", 200)

        elif slash_message_text == "reset stats":
            statGroupQuery = db.session.query(Log.user_id, func.count(Log.user_id)).group_by(Log.user_id).all()
            return_payload = []
            for stat in statGroupQuery:
                return_payload.append({
                    "user_id": stat[0],
                    "total_contributtion": stat[1] * 5
                })
            stats_string = "*ARCHIVED THE STATS TODAY* \n" + get_stats()
            
            return_payload = {"archived_stats":return_payload}
            archivePayload = ArchiveStats(date=datetime.now(),stats=json.dumps(return_payload))

            try:
                db.session.add(archivePayload)
                db.session.query(Log).delete()
                db.session.commit()
                db.session.close()
                response_payload = {
                    "response_type" : "in_channel",
                    "text": stats_string
                }
                headers = {'content-type': 'application/json'}
                r = requests.post(response_url, headers=headers, data=json.dumps(response_payload))
                return("", 200)
            except Exception as e:
                db.session.rollback()
                response_payload = {
                    "response_type" :"in_channel",
                    "text": "Failed to archive stats"
                }
                headers = {'content-type': 'application/json'}
                r = requests.post(response_url, headers=headers, data=json.dumps(response_payload))
                return("", 200)
            
    else:
        return("Sorry, I'm not programmed for that command yet.", 500)

@api_blueprint.route('/api/stats', methods=['GET'])
def stats():
    statQuery = db.session.query(Log.user_id, func.count(Log.user_id)).group_by(Log.user_id).all()
    return_payload = []
    for stat in statQuery:
        return_payload.append({
            "user_id": stat[0],
            "total_contribution": stat[1] * 5
        })
    return(jsonify({"current_stats": return_payload}),200)

@api_blueprint.route('/api/archived_stats', methods=['GET'])
def archived_stats():
    archiveQuery = db.session.query(ArchiveStats).all()
    return_payload =[]
    for stat in archiveQuery:
        return_payload.append({
            "date": stat.date,
            "archived_stats": json.loads(stat.stats)
        })
    return(jsonify({"archived": return_payload}), 200)