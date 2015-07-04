import pattern_to_number



def count_mismatches(word1, word2):
	"""compares two sequences of same length and returns the number of mismatches"""
	count = 0
	for i in range(len(word1)):
		if word1[i] != word2[i]:
			count = count + 1
	return count
#print count_mismatches('GCA', 'GAA')



def mutate_bases(word, m):
	"""returns every possible mutation of word with number of possible mutations m""" 
	legal_mutations =[]
	possibilities = pattern_to_number.list_kmer(len(word))
	for i in possibilities:
		if count_mismatches(i, word) <= m:
			legal_mutations.append(i)
	return legal_mutations
#print mutate_bases('AAA', 1)




