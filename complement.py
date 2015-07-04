def complement(dna):
	"""Returns the complement of a DNA string"""
	list_complement = []
	for i in dna:
		if i == 'A':
			list_complement.append('T')
		elif i == 'T':
			list_complement.append('A')
		elif i == 'G':
			list_complement.append('C')
		elif i == 'C':
			list_complement.append('G')
	complement = ''.join(list_complement)
	return complement