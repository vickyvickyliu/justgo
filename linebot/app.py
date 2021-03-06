from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('h/qzAlK+Od4E6XlfwPN1LFMvDdhYMvw+E3ydSqRWD9zkXgneLQphaaKmQ06w8g9Dc2HZN/lBIcXmXr60HQuGh97klwcAIe209ohmK6EfVLPxvXV1ibwTXNNr++WeWnFGqY8SxaQyNzrHYS7vU7YnNAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fbd62f353ced2061e7a5306ea11897ed')

# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    try:
        User_ID = TextMessage(text=event.source.user_id)
        uu=event.source.user_id
        #line_bot_api.push_message('Uea89b2572fdf1e317967abcc6adf9acc',TextSendMessage(text=uu+msg))
        line_bot_api.multicast(['Uea89b2572fdf1e317967abcc6adf9acc', 'U0b7c9d483a2832b52d89e7d6f8820284'], TextSendMessage(text=uu+"發了:"+msg))
        try:
            #uu=event.source.user_id
            if '拉拉拉' in msg:
                line_bot_api.push_message(uu,TextSendMessage(text=msg))
                try:
                    #a=event.reply_token
                    #b=str(a)
                    #line_bot_api.reply_message(a, TextSendMessage(text=b+"成功"))
                    line_bot_api.push_message(uu,TextSendMessage(text="哈哈"))
                    '''try:
                        line_bot_api.reply_message(a, TextSendMessage(text="哈哈成功"))
                    except:
                        line_bot_api.push_message(uu,TextSendMessage(text="錯誤"))'''

                   
                except:
                    line_bot_api.push_message(uu,TextSendMessage(text="錯誤"))

        except:
            line_bot_api.push_message('Uea89b2572fdf1e317967abcc6adf9acc',TextSendMessage(text="錯誤"))
    except:
        message = TextSendMessage(text="錯誤")
        line_bot_api.reply_message(event.reply_token, message)
    if '會員' in msg:
        message = membersystem()
        line_bot_api.reply_message(event.reply_token, message)
        #from app123 import *
    elif '即時資訊' in msg:
        message = nowinformation()
        line_bot_api.reply_message(event.reply_token, message)
    elif '123' in msg:
        try:
            message = aaa()
        except:
            message = TextSendMessage(text="錯誤")
        line_bot_api.reply_message(event.reply_token, message)
    elif '尋找共乘' in msg:
        message = findjustgo()
        line_bot_api.reply_message(event.reply_token, message)
    elif '揪車情況/取消揪車' in msg:
        message = justgosystem()
        line_bot_api.reply_message(event.reply_token, message)
    elif '使用說明/QA/其他' in msg:
        message = others()
        line_bot_api.reply_message(event.reply_token, message)    
    else:
        message = TextSendMessage(text="請點選圖文表單上的功能，進入服務喔！")
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def a(x):
    line_bot_api.push_message('Uea89b2572fdf1e317967abcc6adf9acc',TextSendMessage(text=x))


