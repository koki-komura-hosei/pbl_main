import requests, json
import io
import wave
import pyaudio
import time
from moviepy.editor import AudioFileClip
import tempfile
import os


class Voicevox:
	speaker_id = 3 # VOICEVOX:ずんだもん
	# speaker_id = 5 # VOICEVOX:ずんだもん（セクシー）

	def __init__(self, host="127.0.0.1", port=50021):
		self.host = host
		self.port = port

	def speak(self, text=None, speaker=speaker_id):
		params = (
			("text", text),
			("speaker", speaker) # 音声の種類をInt型で指定
		)

		init_q = requests.post(
			f"http://{self.host}:{self.port}/audio_query",
			params=params
		)

		res = requests.post(
			f"http://{self.host}:{self.port}/synthesis",
			headers={"Content-Type": "application/json"},
			params=params,
			data=json.dumps(init_q.json())
		)

		# メモリ上で展開
		audio = io.BytesIO(res.content)

		if res.status_code == 200:
			# 音声時間取得
			temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
			temp_file.write(res.content)
			temp_file.close()

			try:
				audioFile = AudioFileClip(temp_file.name)
				# 音声ファイルの長さ（秒）を取得する
				duration = audioFile.duration
				print(f"音声ファイルの長さは {duration} 秒です。")
			finally:
				os.unlink(temp_file.name)

			with wave.open(audio, 'rb') as f:
				# 以下再生用処理
				p = pyaudio.PyAudio()

				def _callback(in_data, frame_count, time_info, status):
					data = f.readframes(frame_count)
					return (data, pyaudio.paContinue)

				stream = p.open(format=p.get_format_from_width(width=f.getsampwidth()),
								channels=f.getnchannels(),
								rate=f.getframerate(),
								output=True,
								stream_callback=_callback)

				# Voice再生
				stream.start_stream()
				while stream.is_active():
					time.sleep(0.1)

				stream.stop_stream()
				stream.close()
				p.terminate()
		else:
			print("音声の取得に失敗しました。")


# def main():
# 	vv = Voicevox()
# 	vv.speak(text='こんにちはです！聞こえてますか？')


# if __name__ == "__main__":
# 	main()
