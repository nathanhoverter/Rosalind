#coding: utf-8
import computing_frequencies
import number_to_pattern
import open_file

def faster_frequent_words(text, k):
	"""Returns the most frequent kmer of length k found in text"""	
	frequent_patterns = set()
	frequency_array = computing_frequencies.computing_frequencies(text, k)
	maxcount = max(frequency_array)
	for i in range(0, 4**k - 1):
		if frequency_array[i] == maxcount:
			pattern = number_to_pattern.number_to_pattern(i, k)
			frequent_patterns.add(pattern)
	return frequent_patterns		

#quiz_string = open_file.open_file("rosalind_1a.txt")
#print faster_frequent_words(quiz_string, 12)
