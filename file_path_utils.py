import os
from record_mic import startRecording
import shutil

def	getPath(filename) -> str:
	
	"""
	Fetches the path of the file.
	
	Arg: filename: str

	Returns the path of the file in string
	"""
	
	return os.path.join(os.path.dirname(__file__),
                    filename)

def	getFilesCount(path: str) -> int:
	
	"""
	Returns the number of files in a given directory
	
	Arg: path: str

	Returns the int
	"""

	if os.path.exists(path) == False:
		return 0
	count = 0
	for _path in os.listdir(path):
		count += 1 if os.path.isfile(os.path.join(path,
                	_path)) else 0
	return count

def	createRecordingFiles(path: str) -> None:
	
	"""
	Records the user and store the file in a given directory
	
	Arg: path: str
	"""

	if os.path.exists(path) == False:
		os.mkdir(path)
	if getFilesCount(path + "/") == 0:
		for i in range(1, 6):
			_file = i.__str__() + ".wav"
			startRecording(_file)
			shutil.move(getPath(_file), getPath(path))
