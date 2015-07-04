import itertools
#returns an alphabetically sorted list of all possible combinations of 
#A's, C's, T's, and G's in a kmer of length k
def list_kmer(k):
	list = []
	str = ''
	for i in itertools.product('ACGT', repeat = k):
		list.append(i)
	formatted_list = []
	for letters in list:
		formatted_list.append(''.join(letters))	
	return formatted_list
	
def pattern_to_number(string, k):
	list_of_kmers = list_kmer(k)
	return list_of_kmers.index(string)

#print pattern_to_number('AAT', 3)
	
	