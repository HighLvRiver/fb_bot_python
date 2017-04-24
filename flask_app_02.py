import requests
import json
from flask import Flask, request
import apiai
from fbmessenger import BaseMessenger
from fbmessenger.templates import GenericTemplate
from fbmessenger.elements import Text, Button, Element
from fbmessenger import quick_replies
from fbmessenger.attachments import Image, Video
from fbmessenger.thread_settings import (
    GreetingText,
    GetStartedButton,
    PersistentMenuItem,
    PersistentMenu,
)

# FB messenger credentials
ACCESS_TOKEN = "EAAInkcLZAzucBAMSeEqDWMwMlC8Q4O0L6dk4VpwwVZA3EA9D8yvR9O8T0yG40Mi5ArIaJAW1Opzqi6H69AANKJDGJlgPoliyOiTJW8Qu0trZBrNIFnB8ZACz0iNkXcKpVONiMsiNASk76eyVI58eT58TvtXA5v2ZBZBqRmZA1ZBf3AZDZD"

# api.ai credentials
CLIENT_ACCESS_TOKEN = "b9b055bad0ee4dc9b53482ad6d458b9d"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # our endpoint echos back the 'hub.challenge' value specified when we setup the webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == 'foo':
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return 'Hello World (from Flask!)', 200

def get_button(ratio):
    return Button(
        button_type='web_url',
        title='facebook {}'.format(ratio),
        url='https://facebook.com/',
        webview_height_ratio=ratio,
    )

def get_element(btn):
    return Element(
        title='Testing template',
        item_url='http://facebook.com',
        image_url='http://placehold.it/300x300',
        subtitle='Subtitle',
        buttons=[btn]
    )

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "배고파",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "넌 누구니",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "도와줘",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply2(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "한식",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "중식",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "일식",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply3(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "H스퀘어",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "유스페이스",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "삼환하이펙스",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply4(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "커피 한잔 사줄게",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply_jayden(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "우유빛깔 제이든",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply_h(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "좋아!",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "별로야",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply_u(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "좋아!",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "별로야!",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply_s(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "좋아!",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "별로야!!",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply_end(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg,
                    "quick_replies":[
                  {
                    "content_type":"text",
                    "title": "응응~ 안녕~",
                    "payload":""
                  },
                  {
                    "content_type":"text",
                    "title": "가지마",
                    "payload":""
                  }
                ]
        }
            }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    if 'attachments' in data :
        message = "I am an attachment"
    else :
        message = data['entry'][0]['messaging'][0]['message']['text']

    # prepare API.ai request
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = message

   # get response from API.ai
    api_response = req.getresponse()
    responsestr = api_response.read().decode('utf-8')
    response_obj = json.loads(responsestr)
    if 'result' in response_obj:
        response = response_obj["result"]["fulfillment"]["speech"]
        if "배고파" in message:
            reply2(sender, response)
        elif "우윳빛깔 제이든" in response:
            reply_jayden(sender, response)
        elif "장소가 있으신가요" in response:
            reply3(sender, response)
        elif "빛깔" in message:
            reply4(sender, response)
        elif "어때요???" in response:
            reply_s(sender, response)
        elif "어때요??" in response:
            reply_u(sender, response)
        elif "어때요?" in response:
            reply_h(sender, response)
        else :
            reply(sender, response)

    return "OK"

if __name__ == '__main__':
    app.run(debug=True)
