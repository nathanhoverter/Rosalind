import re
def find_string(substring, string):
	"""Returns the index(es) that a substring are found in string"""
	return [match.start() for match in re.finditer(substring, string)]

#print find_string('tt', 'tttatt')
	