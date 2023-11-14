from flask import Flask, request
from module.talk.chat_gpt import talk_with_robot

app = Flask(__name__)

isGall: bool = False
isTranslated: bool = False
task = talk_with_robot
receivedText = ''

@app.route('/', methods=['POST'])
def get_textfield_value():
	data = request.form['data']  # Flutterからの入力データを取得
	print(data)  # 入力された値をPythonのコンソールに出力
	receivedText = data
	task(input_prompt=receivedText, isTranslated=isTranslated, isGall=isGall)
	return 'Received data: ' + data, 200

def runReceiver(isTranslated: bool=False, isGall: bool=False):
	isTranslated = isTranslated
	isGall = isGall
	app.run(port=8000) # Macでは「> 5000 & 7000 <」じゃないと動かなかった

if __name__ == '__main__':
	runReceiver()