from sound_utils import *
from math_utils import *
# from plotting import plotting

import matplotlib.pyplot as plt
from file_path_utils import *

def	VoiceValidation() -> bool:
	
	"""
	Fetches the wave signals of both registered user
	and the current user.

	Returns the boolean value true if the accuracy of
	both voice patterns is 90%, else false.
	"""
	
	src = 'voices/Munavar/Recording2.wav'
	_user = input("Name of the User: ")
	if os.path.exists(_user) == False:
		os.mkdir(_user)
	_command = input("Which command would you\
	like to do? -> ")

	createRecordingFiles(_user + "/" + _command)
	
	_valid = []
	filename = 'Output.wav'
	startRecording(filename)
	for i in range(1, 6):
		src = getPath(_user + "/" + _command + "/"
				+ i.__str__() + ".wav")

		samples0, sr0, signal0 = getWaves(filename)
		samples_sf0 = 0

		try:
			samples_sf0 - signal0[:, 0]
		except:
			samples_sf0 = signal0
			
		samples1, sr1, signal1 = getWaves(src)
		samples_sf1 = 0

		try:
			samples_sf1 - signal1[:, 0]
		except:
			samples_sf1 = signal1

		samples0, samples_sf0, data0 = filteringNoise(samples0,
			samples_sf0, [convertToDecibels(i) for i in samples_sf0])
		samples1, samples_sf1, data1 = filteringNoise(samples1,
			samples_sf1, [convertToDecibels(i) for i in samples_sf0])

		nt0 = getNormalisedList(samples0)
		nt1 = getNormalisedList(samples1)
		count = ComparingWaves(nt0, nt1)

		print(f"{count/len(data0) * 100:2.2f}%")
		_valid.append(True if count/len(data0) * 100\
			> 85.0 else False)
		if (i == 5):
			return True if len([i for i in _valid if i == True])\
			>= 3 else False

if __name__ == '__main__':
	print(VoiceValidation())
