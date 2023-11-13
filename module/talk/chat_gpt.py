import openai
import deepl
import pickle
import datetime
import os
from module.talk.voicevox import Voicevox

#! Steps:
#!   1. run in terminal "ngrok http 50021"

openai.organization = "org-azIO3KFDIKHhntGEWdKlVutt" # OPENAIで取得したorganization idを入力してください。
openai.api_key = os.environ["OPENAI_API_KEY"] # OPENAIで取得したAPIKeyを入力してください。
deepl_api_key = "38eef120-d584-deef-8bee-77b4fedb2d2e:fx"

messages = []

def defineSystemType(isGall: bool):
	if isGall:
		messages.append(
			{"role": "system", "content": "あなたは令和のギャル口調の、街のゴミ回収ロボット。50文字以内で返せ"},
		)
	else:
		messages.append(
			{"role": "system", "content": "あなたは少女型街のゴミ拾いロボット。50文字以内で返せ"},
		)


def select_translate():
	dic = {'y': True, 'yes': True, 'n': False, 'no': False}
	while True:
		can_translated = dic.get(input('ENに翻訳して実行するか [Y]es/[N]o? >> ').lower(), -1)
		if type(can_translated) is bool:
				break
		print('Error! Input again.')
	return can_translated


# def save_chat(messages,response):
#     file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     print(file_name)
#     chat_file = open(f'./outputs/{file_name}.pickle','wb')
#     messages.append(response)
#     pickle.dump(messages,chat_file)
#     chat_file.close()


def speak_voicevox(text):
	vv = Voicevox()
	vv.speak(text=text)


def talk_with_robot(input_prompt, isTranslated=True, isGall=False):
	defineSystemType(isGall)

	if isTranslated:
		translator = deepl.Translator(deepl_api_key)
		input_to_chatgpt = translator.translate_text(input_prompt, source_lang='JA', target_lang='EN-US').text
	else:
		input_to_chatgpt = input_prompt

	messages.append(
		{"role": "user", "content": input_to_chatgpt}
	)

	res = openai.ChatCompletion.create(
		# model="gpt-3.5-turbo", # 遅い！
		model="gpt-4-1106-preview", # 速い！
		messages=messages,
		max_tokens=80,
		# response_format="b64_json",
	)

	print(input_prompt)
	print('→ {}', input_to_chatgpt)
	result = res['choices'][0]['message']['content']
	print('------------------------------------------')
	print(result)
	if isTranslated:
		translated_response = translator.translate_text(result, source_lang='EN',target_lang='JA')
		print(f"(translated)→ {translated_response}")
		speak_voicevox(translated_response)
	else:
		speak_voicevox(result)

	# save_chat(messages=messages,response={'response':res})
	print('------------------------------------------')
	print(res)
