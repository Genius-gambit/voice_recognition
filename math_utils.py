import math
import numpy as np

def	getAverage(_list: list) -> float:
	
	"""
	Calculates the average of the given list.
	
	Arg: _list: list

	Returns the float value.
	"""

	return sum(_list) / len(_list)

def	getDistance(diff_x: float, y1: float, y2: float) -> float:
	
	"""
	Calculates the distance of two coordinates.
	
	Arg: diff_x: float, y1: float, y2: float

	Returns the float value.
	"""

	return (round(math.sqrt(math.pow(y2 - y1, 2)
        + math.pow(diff_x, 2)), 3))

def	getPercentile(data: list, percent: float) -> float:
	
	"""
	Calculates the percentile of the given data.
	
	Arg: data: list, percent: float

	Returns the float value.
	"""

	return np.percentile(data, percent)

def	getMean(data: list) -> float:

	"""
	Calculates the mean of the given list.
	
	Arg: data: list

	Returns the float value.
	"""

	return np.mean(data)

def	getMedian(data: list) -> float:

	"""
	Calculates the median of the given list.
	
	Arg: data: list

	Returns the float value.
	"""

	return np.median(data)

def	getStandardDeviation(data: list) -> float:

	"""
	Calculates the standard deviation of the given list.
	
	Arg: data: list

	Returns the float value.
	"""

	return np.std(data)

def	getVariance(data: list) -> float:

	"""
	Calculates the variance of the given list.
	
	Arg: data: list

	Returns the float value.
	"""

	return np.var(data)
