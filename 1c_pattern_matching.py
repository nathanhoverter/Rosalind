import open_file

def pattern_match(text, pattern):
	"""Returns the position(s) that a specific pattern are found in text"""
	match_list = []
	for i in range(len(text)-len(pattern)):
		if text[i:i+len(pattern)] == pattern:
			match_list.append(str(i))
	formatted_list = ' '.join(match_list)
	return formatted_list

#data = open_file.open_file("rosalind_1c.txt")
#example = pattern_match(data,'GAACTTCGA')
#print example
