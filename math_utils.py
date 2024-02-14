import math
import numpy as np

def	getAverage(_list: list) -> float:
    return sum(_list) / len(_list)

def	getDistance(diff_x: float, y1: float, y2: float) -> float:
    return (round(math.sqrt(math.pow(y2 - y1, 2) + math.pow(diff_x, 2)), 3))

def	getPercentile(data: list, percent: float) -> float:
    return np.percentile(data, percent)

def	getMean(data: list) -> float:
    return np.mean(data)

def	getMedian(data: list) -> float:
    return np.median(data)

def	getStandardDeviation(data: list) -> float:
    return np.std(data)

def	getVariance(data: list) -> float:
    return np.var(data)