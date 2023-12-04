from module.talking.talking import talk_with_robot_in_voice

if __name__ == "__main__":
	while True:
		talking = talk_with_robot_in_voice()
		if talking == False:
			continue