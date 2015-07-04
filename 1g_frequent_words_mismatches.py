import pattern_to_number
import itertools

dna='GGTCCAGGTGATGCTACTGATGCTACTTATGAGACGGTCCAGGTGGTCCAGGTGATGCTACTGGTCCAGGTCCGTGGCGACTATGAGACGGTCCAGGTTATGAGACCCGTGGCGACCCGTGGCGACTATGAGACGGTCCAGGTTATGAGACGATGCTACTGGTCCAGGTGATGCTACTCCGTGGCGACCGCCCAACCGCCCAACGGTCCAGGTCCGTGGCGACTATGAGACCGCCCAACCCGTGGCGACCGCCCAACGATGCTACTGATGCTACTTATGAGACTATGAGACGGTCCAGGTGATGCTACTTATGAGACTATGAGACCCGTGGCGACTATGAGACCCGTGGCGACGATGCTACTCCGTGGCGACCGCCCAACTATGAGACGATGCTACTCGCCCAACTATGAGACCGCCCAACCGCCCAACGGTCCAGGTTATGAGACTATGAGACCGCCCAACTATGAGACCGCCCAACGATGCTACTCGCCCAACGGTCCAGGTCGCCCAACGATGCTACTCCGTGGCGACCGCCCAACGATGCTACTCCGTGGCGACGGTCCAGGTTATGAGACGATGCTACTGGTCCAGGTCGCCCAACCGCCCAACGGTCCAGGTGGTCCAGGTGGTCCAGGTTATGAGACGGTCCAGGTCCGTGGCGACTATGAGACTATGAGACGGTCCAGGTCGCCCAACTATGAGACCCGTGGCGACCGCCCAACTATGAGACTATGAGACGATGCTACTCGCCCAACCGCCCAACCCGTGGCGACTATGAGACTATGAGACCCGTGGCGACTATGAGACGATGCTACTGATGCTACTGATGCTACTCGCCCAACCCGTGGCGACCGCCCAACGATGCTACTTATGAGACGATGCTACTCCGTGGCGACTATGAGACCGCCCAACCGCCCAACTATGAGACCGCCCAACGGTCCAGGT'

def score_kmer(kmer1, kmer2, d):
	"""Returns 1 if kmer1 matches kmer2 with at most d mismatches.  Returns 0 if not"""
	count = 0
	for i in range(len(kmer1)):
		if kmer1[i] == kmer2[i]:
			count = count + 1
	if count >= len(kmer1) - d:
		return 1 
	else:
		return 0 

def search_matches(pattern, k, d):
	kmers = pattern_to_number.list_kmer(k)
	matches = []
	for kmer in kmers:
		if score_kmer(kmer, pattern, d) == 1:
			matches.append(kmer)
	return matches	

def frequent_words_mismatches(dna, k, d):
	combinations = []
	possible = []
	scores = []
	answer = []
	for i in range(0, len(dna)-k+1):
		combinations.append(dna[i:i+k])
	for i in combinations:
		possible.append(search_matches(i, k, d))
	flattened_possibilities = [i for sublist in possible for i in sublist]
	#return combinations
	#return possible 
	#return flattened_possibilities
	set_possibilities = list(set(flattened_possibilities))
	#return set_possibilities
	for motif in set_possibilities:
		count = 0
		for i in range(0, len(dna)-k+1):
			window = dna[i:i+k]
			if score_kmer(window, motif, d) == 1:
				count += 1
		scores.append(count)
	for i in range(len(scores)):
		if scores[i] == max(scores):
			answer.append(set_possibilities[i])
	return answer
			

print frequent_words_mismatches(dna, 5, 3)
#answer = GATG(5), ATGC(4), ATGT

