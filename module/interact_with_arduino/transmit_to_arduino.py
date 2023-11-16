import serial
import time

# Arduinoとのシリアル通信の設定
arduino_port = '/dev/tty.usbmodem101'  # Arduinoが接続されているポートに置き換えてください
baud_rate = 9600  # Arduinoのシリアル通信のボーレートに合わせてください

def transmit_to_arduino(sent_data):
	arduino = serial.Serial(arduino_port, baud_rate)
	time.sleep(2)  # Arduinoとの接続を確立するために少し待つ

	# 送信する整数データ
	data_to_send = sent_data  # 送信したい整数データに置き換えてください

	# 整数データをArduinoに送信
	arduino.write(str(data_to_send).encode())
	print(f"Sent data: {data_to_send}")

	arduino.close()  # 通信を閉じる
