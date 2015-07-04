import pattern_to_number
import itertools
reverse_complement = __import__('1b_reverse_complement')

dna='CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT'

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

def frequent_words_mismatches_revcomp(dna, k, d):
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
	rev_comp = []
	for i in answer:
			rev_comp.append(reverse_complement.reverse_complement(i))
	scores_rev_comp = []
	for i in rev_comp:
		for m in combinations:
			scores_rev_comp.append(score_kmer(i, m, d))
	#return rev_comp
	#return scores_rev_comp
	rev_comp_count = []
	for i in range(0, len(scores_rev_comp), len(combinations)):
		sum_score = sum(scores_rev_comp[i:i+len(combinations)])
		rev_comp_count.append(sum_score)
	final_answer=[]
	for i in range(len(rev_comp_count)):
		if rev_comp_count[i]==max(rev_comp_count):
			final_answer.append(answer[i])
			final_answer.append(rev_comp[i])
	return final_answer
		
			

print frequent_words_mismatches_revcomp(dna, 9, 3)
#answer = ATGT ACAT

