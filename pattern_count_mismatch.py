
def pattern_count_mismatch(genome, string, d):
	"""returns the number of occurrences of string in genome with mismatches d"""
	final_count = 0
	windows = []
	for i in range(len(genome)-len(string)+1):
		window = genome[i:i+len(string)]
		for i in range(len(window)):
			count = 0
			if window[i] != string[i]:
				count = count + 1
			windows.append(count)
	#return windows
	for i in range(0, len(windows), len(string)):
		if sum(windows[i:i+len(string)]) <= d:
			final_count = final_count + 1
	return final_count
print pattern_count_mismatch('AACAAGCATAAACATTAAAGAG', 'AAAAA', 2)