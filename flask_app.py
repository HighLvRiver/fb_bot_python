import requests
import json
from flask import Flask, request
import apiai

# FB messenger credentials
ACCESS_TOKEN = "EAAInkcLZAzucBAOsZAryopOY17FZB8c2HijWcLxaHcUgulcfZBcBGw7H7YZCV6dyD4qgb9XNXaKMWOe7hB2se2xffpOGKsm8x6feDL4btBOSvNdTzG2r6TYnI02B8fPOUHwAi9f0uSiftLEa9eCYxvsolmb4VgnLRZApd7TjlScAZDZD"

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

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
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
    reply(sender, response)

    return "ok"

if __name__ == '__main__':
    app.run(debug=True)