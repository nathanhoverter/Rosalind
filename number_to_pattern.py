#Returns the indexth string in a list of alphabetically sorted kmers of length k
import pattern_to_number

def number_to_pattern(index, k):
	list_of_kmers = pattern_to_number.list_kmer(k)
	return list_of_kmers[index]
	
"""print number_to_pattern(5437, 8)"""