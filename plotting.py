import matplotlib.pyplot as plt

def	plotting(data: list):

	"""
	Plots the signal waves on the graph
	
	Arg: data: list
	"""

	plt.figure()
	plt.subplot(3, 1, 1)
	plt.plot(data[0])
	plt.xlabel('Samples')
	plt.ylabel('Data: AudioSegment')

	plt.subplot(3, 1, 2)
	plt.plot(data[1])
	plt.xlabel('Samples')
	plt.ylabel('Data: Soundfile')
	plt.subplot(3, 1, 3)
	plt.plot(data[2])
	plt.xlabel('Samples')
	plt.ylabel('dB Full Scale (dB)')
	plt.tight_layout()
