import speech_recognition as sr

# 音声認識器を作成
recognizer = sr.Recognizer()

# マイクから音声を取得
with sr.Microphone() as source:
	print("何か話してください...")
	audio = recognizer.listen(source)

	try:
		print("認識中...")
		# 音声をテキストに変換
		text = recognizer.recognize_google(audio, language="ja-JP")  # 言語は適宜変更可能
		print("認識結果:", text)

	except sr.UnknownValueError:
		print("音声が認識できませんでした")
	except sr.RequestError:
		print("Google Speech Recognition サービスが利用できません")
