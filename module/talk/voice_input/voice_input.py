import speech_recognition as sr
from io import BytesIO
import openai
from module.mini_game.janken import lets_janken, play_janken


def get_audio_from_mic():
	with sr.Microphone(sample_rate=16000) as source:
		r = sr.Recognizer()
		r.adjust_for_ambient_noise(source) #雑音対策
		try:
			print("なにか話してください")
			audio = r.listen(source, timeout=20)
		except sr.WaitTimeoutError:
			print("音声を取得できませんでした")
			return False

	try:
		print("音声認識中...")
		result_by_google = r.recognize_google(audio, language='ja-JP')
		print("google: ", result_by_google)

		# 'ジャンケン’という単語を認識したら始める
		if 'ジャンケン' in result_by_google or 'じゃんけん' in result_by_google:
			lets_janken()
			def user_janken():
				voice_input = voice_to_text_by_google()
				# if voice_input == False:
				# 	return False
				if "グー" in voice_input or "チョキ" in voice_input or "パー" in voice_input:
					play_janken(voice_input)
					return False
				else:
					user_janken()
			user_janken()

		# "ストップ" と言ったら音声認識を止める
		if result_by_google == "ストップ" :
			print("end")
			exit()

		return audio
	except sr.UnknownValueError:
		print("音声を認識できませんでした")
		return False
	except sr.RequestError as e:
		print(f"エラーが発生しました: {e}")
		return False


def voice_to_text_by_google():
	with sr.Microphone(sample_rate=16000) as source:
		r = sr.Recognizer()
		r.adjust_for_ambient_noise(source) #雑音対策
		try:
			print("なにか話してください")
			audio = r.listen(source, timeout=20)
		except sr.WaitTimeoutError:
			print("音声を取得できませんでした")
			return False

	try:
		print("音声認識中...")
		result_by_google = r.recognize_google(audio, language='ja-JP')
		# "ストップ" と言ったら音声認識を止める
		if result_by_google == "ストップ" :
			print("end")
			exit()
		return result_by_google
	except sr.UnknownValueError:
		print("音声を認識できませんでした")
		return False
	except sr.RequestError as e:
		print(f"エラーが発生しました: {e}")
		return False


def voice_to_text():
	audio = get_audio_from_mic()
	if audio == False:
		return False
	else:
		audio_data = BytesIO(audio.get_wav_data())
		audio_data.name = 'from_mic.wav'
		transcript = openai.Audio.transcribe('whisper-1', audio_data)
		return transcript['text']


if __name__ == "__main__":
	voice_to_text()
