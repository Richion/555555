#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, abort
import requests
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from bs4 import BeautifulSoup

app = Flask(__name__)

line_bot_api = LineBotApi('Ean1Xdkkpjr6JRgPC5j5cZeoZkLbDwWB78+xXZYAcCFLwRok8wqNsQ6Cf4xfM+WOw25PPK6KKGXGrc7gGa1Q19ObvrXBKREq5o2JPV8h3CXF4naM9NBJID07UlrKrP8PHnPGKW2FRASHdqcWlje/sAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('08ed3b014b9d96754789a1d594c3e423')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def movie():
    res = requests.get('https://oursogo.com/forum-174-1.html')
    soup = BeautifulSoup(res.text,'html.parser')
    title= soup.find_all('a',{'class':'xst'})
    content = ""
    #print(title)
    content = []
    for i, data in enumerate(title):
        if i > 10:
            break
        content.append(data.text)
    return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "近期上映電影":
        content = movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='\n'.join(content)))
        return 0


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




