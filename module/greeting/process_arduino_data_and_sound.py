from playsound import playsound


def print_data_and_sound(data, sound_path):
	# データを処理するための関数
	# この関数内でデータに基づいた処理を行います
	playsound(sound_path)
	print("Received data:", data)
