import serial
# import random
from module.greeting import print_data_and_sound

# ArduinoのCOMポートに合わせてポート名を変更
arduino_port = '/dev/tty.usbmodem101'
# [ls /dev/cu.*] で確認可

# シリアルポートを開く
ser = serial.Serial(arduino_port, 9600)

# sound_fileのパス名
sound_path_prefix = "module/greeting/departure"
sound_path = sound_path_prefix + ".wav"



def saying_at_departure():
	data: bytes = b''

	try:
		while True:
			data = ser.readline()  # シリアルポートから1バイトのデータを読み込む
			if data != b'': # データがある場合
				print_data_and_sound(data, sound_path)  # データを処理する関数を呼び出す

	except KeyboardInterrupt:
		ser.close()  # シリアルポートを閉じる

if __name__ == "__main__":
	saying_at_departure()
