# from module.talk.voice_input.voice_input import voice_to_text
from playsound import playsound
import random
import time

#【トーク内容】
# You「ジャンケンしよう」
# AI「いいよ！ジャンケンしよう！」
# AI「いくよ、最初はグー。ジャンケン」
# You「グー」
# AI「パー」（with ライト点灯）
# AI「あなたはグーを出して、私はパーを出しました」（この間に勝敗を計算）
# AI「僕が勝ったね！残念無念また来年」or「君が勝ったね！おめでとう！」or「あいこだね！もう一度できるよ」

# 【ファイル名一覧】
# lets_janken.wav
# go_ahead_janken.wav
# rock.wav
# scisor.wav
# paper.wav
# result_1.wav
# result_2.wav
# result_3.wav
# user_won.wav
# ai_won.wav
# aiko.wav

base_path = "module/mini_game/"
suffix = ".wav"

lets_janken_path = base_path + "lets_janken" + suffix
go_ahead_janken_path = base_path + "go_ahead_janken" + suffix
rock_path = base_path + "rock" + suffix
scisor_path = base_path + "scisor" + suffix
paper_path = base_path + "paper" + suffix
result_1_path = base_path + "result_1" + suffix
result_2_path = base_path + "result_2" + suffix
result_3_path = base_path + "result_3" + suffix
user_won_path = base_path + "user_won" + suffix
ai_won_path = base_path + "ai_won" + suffix
aiko_path = base_path + "aiko" + suffix

def lets_janken():
	print('いいよ！ジャンケンしよう！')
	playsound(lets_janken_path)
	time.sleep(1)
	print('いくよ、最初はグー。ジャンケン')
	playsound(go_ahead_janken_path)

def input_janken(voice_input):
	print("input→ ", voice_input)
	if "グー" in voice_input:
		print('あなた: グー')
		return "グー"
	elif "チョキ" in voice_input:
		print('あなた: チョキ')
		return "チョキ"
	elif "パー" in voice_input:
		print('あなた: パー')
		return "パー"

def ai_janken():
	janken_num = random.randint(1, 3)
	if janken_num == 1:
		print('AI: グー')
		playsound(rock_path)
		return "グー"
	elif janken_num == 2:
		print('AI: チョキ')
		playsound(scisor_path)
		return "チョキ"
	elif janken_num == 3:
		print('AI: パー')
		playsound(paper_path)
		return "パー"

def calculateWinner(user, ai):
	if user == ai:
		# print('あいこ')
		return "none"
	if user == "グー":
		if ai == "チョキ":
			return "user"
		elif ai == "パー":
			return "ai"
	if user == "チョキ":
		if ai == "パー":
			return "user"
		if ai == "グー":
			return "ai"
	if user == "パー":
		if ai == "グー":
			return "user"
		elif ai == "チョキ":
			return "ai"



def play_janken(voice_input):
	janken_input = input_janken(voice_input)
	print("→ ", janken_input)
	ai = ai_janken()

	winner = calculateWinner(janken_input, ai)

	print(f"あなたは{janken_input}を出して、わたしは{ai}を出しました")
	playsound(result_1_path)

	if janken_input == "グー":
		playsound(rock_path)
	elif janken_input == "チョキ":
		playsound(scisor_path)
	elif janken_input == "パー":
		playsound(paper_path)

	playsound(result_2_path)

	if ai == "グー":
		playsound(rock_path)
	elif ai == "チョキ":
		playsound(scisor_path)
	elif ai == "パー":
		playsound(paper_path)

	playsound(result_3_path)

	if winner == "user":
		playsound(user_won_path)
	elif winner == "ai":
		playsound(ai_won_path)
	elif winner == "none":
		playsound(aiko_path)
