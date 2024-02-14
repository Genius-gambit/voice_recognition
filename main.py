from sound_utils import *
from math_utils import *
from record_mic import startRecording

import matplotlib.pyplot as plt
import numpy as np

def	VoiceValidation() -> bool:
    
	src = 'src.wav'
	startRecording('src.wav')
	filename = 'Output.wav'
	startRecording('Output.wav')

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
		
	data0 = [convertToDecibels(i) for i in samples_sf0]
	data1 = [convertToDecibels(i) for i in samples_sf0]

	nt0 = getNormalisedList(samples0)
	nt1 = getNormalisedList(samples1)

	count = 0
	startPos0 = nt0.index(1.0)
	startPos1 = nt1.index(1.0)

	if startPos0 <= startPos1:
		count = compareLeftWaves(nt0, startPos0, nt1, startPos1)
	elif startPos0 > startPos1:
		count = compareLeftWaves(nt1, startPos1, nt0, startPos0)
		
	iterators0 = len(nt0) - startPos0
	iterators1 = len(nt1) - startPos1

	if iterators0 <= iterators1:
		count += compareRightWaves(nt0, startPos0 + 1, nt1, startPos1 + 1)
	elif iterators0 > iterators1:
		count += compareRightWaves(nt1, startPos1 + 1, nt0, startPos0 + 1)

	print(f"{count/len(data0) * 100}%")
	return True if count/len(data0) * 100 > 80.0 else False

if __name__ == '__main__':
	print(VoiceValidation())