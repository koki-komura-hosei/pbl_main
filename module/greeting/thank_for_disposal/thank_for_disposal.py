import serial
import random
from module.greeting import print_data_and_sound

# ArduinoのCOMポートに合わせてポート名を変更
arduino_port = '/dev/tty.usbmodem101'
# [ls /dev/cu.*] で確認可

# シリアルポートを開く
ser = serial.Serial(arduino_port, 9600)

# sound_fileのパス名
sound_path_prefix = "module/greeting/thank_for_disposal/thank_for_disposal_"
sound_num = random.randint(1, 2) # soundの数だけ増える
sound_path = sound_path_prefix + str(sound_num) + ".wav"

def thank_for_disposal():
	data: bytes = b''

	try:
		while True:
			data = ser.readline()  # シリアルポートから1バイトのデータを読み込む
			if data != b'':
				print_data_and_sound(data, sound_path)  # データを処理する関数を呼び出す

	except KeyboardInterrupt:
		ser.close()  # シリアルポートを閉じる

if __name__ == "__main__":
	thank_for_disposal()
