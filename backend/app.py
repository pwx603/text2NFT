from flask import Flask, request, jsonify
from flask_cors import CORS

from OpenAIProcessor import OpenAIProcessor
from StableFusionAPI import StableFusionAPI

app = Flask(__name__)
CORS(app)

o = OpenAIProcessor()
s = StableFusionAPI()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/prompt',methods = ['POST'])
def enter_prompt():
    prompt = request.json["prompt"]
    result = o.enter_prompt(prompt)
    return jsonify(result)

@app.route('/txt2Img',methods = ['POST'])
def txt2Img():
    prompt = request.json["prompt"]
    pic_des = o.get_img_prompt(prompt).choices[0].message.content
    result = s.txt2img(pic_des)
    return jsonify(result.json())
if __name__ == '__main__':
    app.run()
