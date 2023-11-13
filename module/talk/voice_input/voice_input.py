import speech_recognition as sr
from io import BytesIO
import openai


def get_audio_from_mic():
	with sr.Microphone(sample_rate=16000) as source:
		print("なにか話してください")
		r = sr.Recognizer()
		r.adjust_for_ambient_noise(source) #雑音対策
		audio = r.listen(source)
		print("考え中...")
		print(r.recognize_google(audio, language='ja-JP'))

		# while True:
		# 	try:
		# 		print(r.recognize_google(audio, language='ja-JP'))

		# 		# "ストップ" と言ったら音声認識を止める
		# 		if r.recognize_google(audio, language='ja-JP') == "ストップ" :
		# 			print("end")
		# 			break

		# 	# 以下は認識できなかったときに止まらないように。
		# 	except sr.UnknownValueError:
		# 		print("could not understand audio")
		# 	except sr.RequestError as e:
		# 		print("Could not request results from Google Speech Recognition service; {0}".format(e))

		return audio

def voice_to_text():
	audio = get_audio_from_mic()
	audio_data = BytesIO(audio.get_wav_data())
	audio_data.name = 'from_mic.wav'
	transcript = openai.Audio.transcribe('whisper-1', audio_data)
	return transcript['text']
