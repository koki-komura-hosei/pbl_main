import speech_recognition as sr
from io import BytesIO
import openai


def get_audio_from_mic():
	with sr.Microphone(sample_rate=16000) as source:
		print("なにか話してください")
		r = sr.Recognizer()
		r.adjust_for_ambient_noise(source) #雑音対策
		try:
			audio = r.listen(source, timeout=20)
			print("音声取得完了")
		except sr.WaitTimeoutError:
			print("音声を取得できませんでした")

	try:
		print("音声認識中...")
		result_by_google = r.recognize_google(audio, language='ja-JP')
		print("google: ", result_by_google)
	except sr.UnknownValueError:
		print("音声を認識できませんでした")
	except sr.RequestError as e:
		print(f"エラーが発生しました: {e}")

	# "ストップ" と言ったら音声認識を止める
	if result_by_google == "ストップ" :
		print("end")
		exit()

	return audio

def voice_to_text():
	audio = get_audio_from_mic()
	audio_data = BytesIO(audio.get_wav_data())
	audio_data.name = 'from_mic.wav'
	transcript = openai.Audio.transcribe('whisper-1', audio_data)
	return transcript['text']

if __name__ == "__main__":
	voice_to_text()
