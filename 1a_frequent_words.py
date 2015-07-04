import pattern_count

def frequent_words(text, k):
	"""Returns the most frequent kmer of length k found in text"""	
	frequent_patterns = set()
	count = []
	for i in range(len(text)-k):
		pattern = text[i:i+k]
		count.append(pattern_count.pattern_count(text, pattern))
	#return count
	max_count = max(count)
	#return max_count
	for i in range(len(text)-k):
		if count[i] == max_count:
			frequent_patterns.add(text[i:i+k])
	return frequent_patterns

#with open ("rosalind_1a.txt", "r") as myfile:
    #data=myfile.read().replace('\n', '')

print frequent_words('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA', 3)

