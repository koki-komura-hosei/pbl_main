from module.talk.chat_gpt import select_translate
from module.talk.chat_gpt import talk_with_robot
from module.talk.voice_input import voice_to_text

def talk_with_robot_in_text():
	user_saying = input('ChatGPTに聞きたいことを入力: ')
	talk_with_robot(input_prompt=user_saying, isTranslated=False)

def talk_with_robot_in_voice():
	talk_with_robot(input_prompt=voice_to_text(), isTranslated=False)

if __name__ == "__main__":
	# isTranslated = select_translate() # 英訳はトークン節約できるが、再翻訳で意味がめちゃくちゃになるので却下
	talk_with_robot_in_voice()
