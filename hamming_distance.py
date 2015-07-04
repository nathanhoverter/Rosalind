def hamming_distance(string1, string2):
	count = 0
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			count = count + 1
	return count 

#print hamming_distance('CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT', 'CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG') 