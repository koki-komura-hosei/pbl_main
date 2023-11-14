import speech_recognition as sr

# 音声認識器のインスタンスを作成
recognizer = sr.Recognizer()

# マイクから音声を取得
with sr.Microphone(device_index=3) as source:
	print("話してください...")
	print(str(recognizer.energy_threshold))
	recognizer.adjust_for_ambient_noise(source, duration=5)  # ノイズの除去
	print(str(recognizer.energy_threshold))
	try:
		audio = recognizer.listen(source, timeout=20)  # 音声を取得
	except sr.WaitTimeoutError:
		print("音声を拾えませんでした")

	try:
		print("音声認識中...")
		text = recognizer.recognize_google(audio, language="ja-JP")  # Googleの音声認識APIを使用して音声をテキストに変換
		print(f"認識されたテキスト: {text}")
	except sr.UnknownValueError:
		print("音声を認識できませんでした")
	except sr.RequestError as e:
		print(f"エラーが発生しました: {e}")
