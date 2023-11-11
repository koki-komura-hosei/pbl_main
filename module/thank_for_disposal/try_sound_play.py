from playsound import playsound
import random
from time import sleep

sound_path = "module/thank_for_disposal/thank_for_disposal_"

sound_num = random.randint(1, 2)

playsound(sound_path + str(sound_num) + ".wav")
sleep(1)
playsound(sound_path + str(sound_num) + ".wav")
