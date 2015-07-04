import pattern_to_number

dna = ['TTGGAGTACGCGTGATACCACTGTTCGTCACGCTTATCGTCA', 'TAGGCATATGGCTTAACGAGGAGATTTGAGAATCTATGCTCC', 'GTTATTTTTTCGCTGACGAAGACGTAGCAGTTCGAGGACACC', 'GCTGACCCTTGTGGATGCGTACACTTAGAGACACAGGTTGTT', 'ACGTGAGGTCGCTTTGAGTCAGGAATGCGAAGAAAACTCCAG', 'CATATATGGCTCTTAGAGAGGCCTCGGATCAGGTAATTGCGC', 'TCTACGCAATATTTCGAGGAGACGAGGCAACCTGCACTTGTG', 'TTGGAGTCGAAGGCTCGCGTGTACCTCACGCAGTAGTGGAGC', 'TATGATGTACGTACGCCTTTCGAGAGGTTCCCGAGCATTGGT', 'GAACTAGCGGTGTTATCGAAAAAATTGGAGATACACAACATC']




def score(pattern1, pattern2):
	""" 
	Returns the number of mismatches between pattern1 and pattern2
	
	score('GCA', 'ATA') --> 2
	"""
	count = 0
	for i in range(len(pattern1)):
		if pattern1[i] != pattern2[i]:
			count = count + 1
	return count

def d(pattern, dna):
	""" 
	Finds the best match of pattern to each substring in dna and returns the total number 
	of mismatches of the resulting best matches.
	   
	d('AAA', ['ttaccttAAC', 'gATAtctgtc', 'ACGgcgttcg'] --> 4
	"""
	kmers = []
	scores = []
	k = len(pattern)
	for oligo in dna:
		for i in range(0, len(oligo)-k+1):
			kmers.append(oligo[i:i+k])
	for i in kmers:
		scores.append(score(pattern, i))
	comparisons = len(dna[0]) - k + 1
	index_min_scores = []
	min_scores = []
	scores2 = []
	kmers2 = []
	for i in range(0, len(kmers), comparisons):
		kmers2.append(kmers[i:i+comparisons])
	for i in range(0, len(scores), comparisons):
		scores2.append(scores[i:i+comparisons])
	for i in scores2:
		min_scores.append(min(i))
	return sum(min_scores)

def median_string(dna, k):
	"""
	Iterates through every possible kmer of length k and returns a kmer that minimizes d(pattern, dna).
	This is a faster version of the motif_finding problem.
	"""
	kmers = pattern_to_number.list_kmer(k)
	best_pattern = kmers[0]
	for kmer in kmers:
		if d(kmer, dna) < d(best_pattern, dna):
			best_pattern = kmer
	return best_pattern

		

print median_string(dna, 6)
	
	
	
		 



	