import numpy as np
from pydub import AudioSegment
import soundfile as sfile
# from math_utils im

def	convertToDecibels(arr):
	ref = 1
	if arr != 0:
		return 20 * np.log10(abs(arr) / ref)
	return -60

def	getFirstNoise(_list: list) -> list:
	result = []
	for i in range(len(_list)):
		result.append(_list[i])
	while(1):
		if result[0] != 0:
			break
		result.pop(0)
	return (result)

def	getNormalisedList(_list: list) -> list:
	result = []
	_min = min(_list)
	_max = max(_list)
	for i in _list:
		result.append((i - _min) / (_max - _min))
	return result

def	calcAmplitude(maxPitch: float, minPitch: float) -> float:
	return (maxPitch - minPitch) / 2

def	compareLeftWaves(list1: list, index1: int, list2: list, index2: int) -> int:
	count = 0
	if index1 <= index2:
		while index1 > 0:
			if round(round(list1[index1], 4) -
			round(list2[index2], 4), 4) < 0.1 and round(round(list1[index1], 4) -
			round(list2[index2], 4), 4) > -0.1:
				count += 1
			index1 -= 1
			index2 -= 1
	return count

def	compareRightWaves(list1: list, index1: int, list2: list, index2: int) -> int:
	if (index1 + 1 - len(list1)) >= 0 or (index2 + 1 - len(list2)) >= 0:
		return 0
	count = 0
	while index1 < len(list1):
		if round(round(list1[index1], 4) -
        	round(list2[index2], 4), 4) < 0.1 and round(round(list1[index1], 4)
            - round(list2[index2], 4), 4) > -0.1:
			count += 1
		index1 += 1
		index2 += 1
	return count

def	getWaves(filename: str) -> tuple:
    audio0 = AudioSegment.from_mp3(filename)
    signal0, sr0 = sfile.read(filename)
    samples0 = audio0.get_array_of_samples()
    return samples0, sr0, signal0
