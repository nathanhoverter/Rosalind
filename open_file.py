def open_file(filename):
	with open (filename, "r") as myfile:
		data = myfile.read().replace('\n', '')
	return data 


