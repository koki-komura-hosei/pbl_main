from module.receive_from_flutter.receiver import runReceiver
# from module.talk.chat_gpt import select_translate
from module.talk.chat_gpt import talk_with_robot
from module.talk.voice_input.voice_input import voice_to_text

def talk_with_robot_in_text(isGall: bool=False):
	user_saying = input('ChatGPTに聞きたいことを入力: ')
	talk_with_robot(input_prompt=user_saying, isTranslated=False, isGall=isGall)

def talk_with_robot_in_voice(isGall: bool=False):
	talk_with_robot(input_prompt=voice_to_text(), isTranslated=False, isGall=isGall)

def talk_with_robot_from_flutter_input(isTranslated=False, isGall: bool=False):
	runReceiver(isTranslated=isTranslated, isGall=isGall)

if __name__ == "__main__":
	# isTranslated = select_translate() # 英訳はトークン節約できるが、再翻訳で意味がめちゃくちゃになるので却下
	while True:
		talk_with_robot_in_voice()
	# talk_with_robot_from_flutter_input(isGall=True)
