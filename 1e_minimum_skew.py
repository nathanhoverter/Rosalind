import open_file

def minimum_skew(genome):
	"""Returns position(s) in genome where the cumulative difference between the number of 
	G's and C's are minimized """
	skew_list =[]
	min_position = []
	count = 0
	for i in genome:
		if i == 'G':
			count = count + 1
			skew_list.append(count)
		elif i == 'C':
			count = count - 1
			skew_list.append(count)
		else:
			skew_list.append(count)
	#return skew_list
	for i in range(len(skew_list)):
		if skew_list[i] == min(skew_list):
			min_position.append(i+1)
	return min_position

#data = open_file.open_file("rosalind_1e.txt")
print minimum_skew('GATACACTTCCCGAGTAGGTACTG')
		
