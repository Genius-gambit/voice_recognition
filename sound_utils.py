import numpy as np
from pydub import AudioSegment
import soundfile as sfile

CONF_INT = 0.05

def	convertToDecibels(arr) -> float:

	"""
	Converts the given data to decibels which is the unit\
	scale of sound waves.
	
	Arg: arr

	Returns the float value.
	"""

	ref = 1
	if arr != 0:
		return 20 * np.log10(abs(arr) / ref)
	return -60

def	getFirstNoise(_list: list) -> list:

	"""
	Iterates through each and every element and breaks after\
	receiving the first noise from the sound wave.
	
	Arg: _list: list

	Returns the list.
	"""

	result = []
	for i in range(len(_list)):
		result.append(_list[i])
	while(1):
		if result[0] != 0:
			break
		result.pop(0)
	return (result)

def	getNormalisedList(_list: list) -> list:

	"""
	Normalizes the value of elements of the passed list.
	
	Arg: _list: list

	Returns the list.
	"""

	result = []
	_min = min(_list)
	_max = max(_list)
	for i in _list:
		result.append((i - _min) / (_max - _min))
	return result

def	calcAmplitude(maxPitch: float, minPitch: float) -> float:

	"""
	Calculates the amplitude of the sound wave which is
	(_max - _min) / 2
	
	Arg: maxPitch: float, minPitch: float

	Returns the float value.
	"""

	return (maxPitch - minPitch) / 2

def	compareLeftWaves(list1: list, index1: int, list2: list,
                     index2: int) -> int:

	"""
	Starts from the maximum pitch with given data and
	compares each value towards the left side until any
	index values reaches 0 or less than 0. Count increases
	if the difference of two elements belongs to the range
	of (-0.05, 0.05)
	
	Arg: list1: list, index1: int, list2: list, index2: int

	Returns the int value.
	"""

	count = 0
	if index1 <= index2:
		while index1 > 0:
			if round(round(list1[index1], 4) -
			round(list2[index2], 4), 4) < CONF_INT\
			and round(round(list1[index1], 4) -
			round(list2[index2], 4), 4) > -CONF_INT:
				count += 1
			index1 -= 1
			index2 -= 1
	return count

def	compareRightWaves(list1: list, index1: int, list2: list,
                      index2: int) -> int:
	
	"""
	Starts from the maximum pitch with given data and compares
	each value towards the right side until any index values reaches
	outside the length of the data. Count increases if the difference
	of two elements belongs to the range of (-0.05, 0.05)
	
	Arg: list1: list, index1: int, list2: list, index2: int

	Returns the int value.
	"""

	if (index1 + 1 - len(list1)) >= 0\
		or (index2 + 1 - len(list2)) >= 0:
		return 0
	count = 0
	while index1 < len(list1):
		if round(round(list1[index1], 4) -
			round(list2[index2], 4), 4) < CONF_INT\
			and round(round(list1[index1], 4)
			- round(list2[index2], 4), 4) > -CONF_INT:
			count += 1
		index1 += 1
		index2 += 1
	return count

def	filteringNoise(samples, samples_sf, data) -> tuple:

	"""
	Filtering the Noise and returning the data.
	
	Arg: samples, samples_sf, data

	Returns the tuple value.
	"""

	return(samples[4300:], samples_sf[4300:], data[4300:])

def	getWaves(filename: str) -> tuple:
	
	"""
	Starts from the maximum pitch with given data and compares
	each value towards the right side until any index values
	reaches outside the length of the data. Count increases if
	the difference of two elements belongs to the range
	of (-0.05, 0.05)
	
	Arg: list1: list, index1: int, list2: list, index2: int

	Returns the tuple value.
	"""

	audio0 = AudioSegment.from_mp3(filename)
	signal0, sr0 = sfile.read(filename)
	samples0 = audio0.get_array_of_samples()
	return samples0, sr0, signal0

def	ComparingWaves(nt0: list, nt1: list) -> int:

	"""
	Normalising the data --> Compare the waves --> Calculating
	the similar patterns
	
	Arg: nt0: list, nt1: list

	Returns the int value.
	"""

	count = 0
	startPos0 = nt0.index(1.0)
	startPos1 = nt1.index(1.0)

	if startPos0 <= startPos1:
		count = compareLeftWaves(nt0, startPos0,
            nt1, startPos1)
	elif startPos0 > startPos1:
		count = compareLeftWaves(nt1, startPos1,
            nt0, startPos0)
		
	iterators0 = len(nt0) - startPos0
	iterators1 = len(nt1) - startPos1

	if iterators0 <= iterators1:
		count += compareRightWaves(nt0, startPos0
        	+ 1, nt1, startPos1 + 1)
	elif iterators0 > iterators1:
		count += compareRightWaves(nt1, startPos1
            + 1, nt0, startPos0 + 1)
	return count
