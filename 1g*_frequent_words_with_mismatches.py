import itertools
import mutate_bases

def frequent_approximate_pattern2(m, k, genome):
	"""Returns most frequent kmers with length k, with number of mismatches m in genome"""
	list_of_mutations = []
	match_count = []
	max_match = []
	for i in range(0, len(genome)-k+1):
		kmer = genome[i:i+k]
		list_of_mutations.append(mutate_bases.mutate_bases(kmer, m))
	
	combined_list = list(itertools.chain(*list_of_mutations))
	count_l=[]
	for i in combined_list:
		count_l.append(combined_list.count(i))
	m = max(count_l)
	x = [i for i, j in enumerate(count_l) if j==m]
	final = set()
	for i in range(len(x)):
		y=x[i]
		final.add(combined_list[y])
	return final
	
	
		

			
		
