import pattern_to_number
import itertools

dna = ['AAGTGGATCGTAGTGGCAGGTGTAA','ATTTTCAAATGATCGATGGTTTGAA', 'TTACGAAACAGACCGCAACTCGTCA', 'GACTGCCGGGGTGGGGCAAATACGG', 'TATGCCACGATTAGCGACCGAGCAA', 'TCTTTCGGGTCCATTTGCTGGAACG']

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

def motif_enumeration(dna, k, d):
	patterns = []
	formatted_combinations = []
	combinations = []
	possible = []
	count = 0
	for oligo in dna:
		for i in range(0, len(oligo)-k+1):
			combinations.append(oligo[i:i+k])
	slice_length = len(combinations)/len(dna)
	for i in range(0, len(combinations), slice_length):
		formatted_combinations.append(combinations[i:i+slice_length])
	flattened_combinations = [i for sublist in formatted_combinations for i in sublist]
	#return flattened_combinations
	for i in flattened_combinations:
		possible.append(search_matches(i, k, d))
	#return possible
	flattened_possibilities = [i for sublist in possible for i in sublist]
	set_possibilities = list(set(flattened_possibilities))
	comparisons = []
	for i in set_possibilities:
		for j in flattened_combinations:
			comparisons.append(score_kmer(i, j, d))
	#return set_possibilities
	#return comparisons
	skip_count = len(dna[0])-k+1
	#return skip_count
	"""for i in range(0, len(comparisons), skip_count):
		counter = len(dna)"""
	true_comparisons = []
	for i in range(0, len(comparisons),skip_count):
		if 1 in comparisons[i:i+skip_count]:
			true_comparisons.append(1)
		else:	
			true_comparisons.append(0)
	final_cut = []
	for i in range(0, len(true_comparisons),len(dna)):
		if all(true_comparisons[i:i+len(dna)]) == 1:
			final_cut.append(1)
		else: 
			final_cut.append(0)
	answer = []
	for i in range(len(final_cut)):
		if final_cut[i] == 1:
			answer.append(set_possibilities[i])
	return answer 
	
			

print motif_enumeration(dna, 5, 2)


