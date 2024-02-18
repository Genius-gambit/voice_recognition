import pyaudio
import wave
from time import sleep

def	startRecording(filename: str):

	"""
	Records a user and stores the signal waves .wav file with passed filename.
	
	Arg: filename: str
	"""

	while(1):
		sleep(2)
		break

	FRAMES_PER_BUFFER = 3200
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 16000

	print("--> Started Recording <--\n")
	p = pyaudio.PyAudio()

	seconds = 5
	frames = []
	stream = p.open(
		format=FORMAT,
		channels=CHANNELS,
		rate=RATE,
		input=True,
		frames_per_buffer=FRAMES_PER_BUFFER
	)
	for i in range(0, int(RATE / FRAMES_PER_BUFFER
        	* seconds)):
		data = stream.read(FRAMES_PER_BUFFER)
		frames.append(data)
		print(f"\r{(int(seconds - ((i + 1) / 5))):02d} \
Seconds Left", end="", flush=True)
	print("\n\n--> Finished Recording <--")
	stream.stop_stream()
	stream.close()
	p.terminate()

	obj = wave.open(filename, "wb")
	obj.setnchannels(CHANNELS)
	obj.setsampwidth(p.get_sample_size(FORMAT))
	obj.setframerate(RATE)
	obj.writeframes(b"".join(frames))
	obj.close()
