# fb_bot_python

1. https://console.api.ai
  - sign up 
  - get a api.ai client access token

2. https://developers.facebook.com/
  - sign up 
  - Add a new app 
  - messenger start 
    - get a token
    - create a new page
      - get a page access token
    - Webhook setting
      - Callback URL : https://[id].pythonanywhere.com/
      - Confirm token : foo (your token)
      - receive field : messages
      - Select a page to subscribe your webhook to the page events : subscribe
      
3. https://www.pythonanywhere.com/
  - Beginner
  3.1. Web > Add a new web app > Flask > Python 3.5
  3.2. File > mysite > flask_app.py : edit & save
    - insert "page access token"
    - insert "api.ai client access token"
  3.3. Consoles > Start a new console > Bash
    - pip3 install --user apiai
  3.4. File > mysite > flask_app.py : run & refresh
  
