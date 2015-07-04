import generating_theoretical_spectrum
import itertools
import pprint

integer_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
# get unique aa masses from integer_mass dict
integer_masses = integer_mass.values()
unique_masses = list(set(integer_masses))

mass_to_aa =  {v: k for k, v in integer_mass.items()}

def score_peptide(peptide, spectrum):
	#pep_spectrum = generating_theoretical_spectrum.generating_theoretical_spectrum(peptide)
	#matches = [i for i pep_spectrum if i in spectrum]
	matches = [i for i in list(set(peptide)) if i in spectrum]
	return len(matches)
	
	
def format(spectrum):
	"""Given a Rosalind problem 2E format of a list of aa masses (spectrum), return 
	spectrum in python list format"""
	# place rosalind format for spectrum in list
	spectrum_list = spectrum.split(' ')
	spectrum_ints = map(int, spectrum_list)
	#return matches between spectrum_ints and integer_masses
	return spectrum_ints
	
def root(spectrum):
	"""Returns every permutation of the first 2 aa matches that are consistent with spectrum"""
	combos = []
	possibilities = [i for i in unique_masses if i in formatted_input]
	for i in possibilities:
		for aa in unique_masses:
			combos.append([i, aa])	
	return combos

def get_leaderboard(peptide_list, spectrum, m):
	"""Compares a list of peptides to spectrum and gets the highest m scores, including ties"""
	scores = []
	leaders = []
	count = 0
	for i in peptide_list:
		scores.append(score_peptide(i, spectrum))
	for i in range(len(scores)):
		if scores[i] == max(scores):
			count = count + 1
			leaders.append(peptide_list[i])
	if len(leaders) < m:
		for i in range(len(scores)):
			if scores[i] + 1 == max(scores):
				leaders.append(peptide_list[i])
	return leaders
	#return scores

def max_score(peptide_list, spectrum, m):
	"""Compares a list of peptides to spectrum and gets the highest m scores, including ties"""
	scores = []
	leaders = []
	count = 0
	for i in peptide_list:
		scores.append(score_peptide(i, spectrum))
	for i in range(len(scores)):
		if scores[i] == max(scores):
			leaders.append(peptide_list[i])
	return scores
	
def expand(spectrum):	
	"""Expands the aa matches by exactly 1 of every possible aa"""
	combos = []
	formatted = []
	new = []
		#expand by one aa mass 
	for i in itertools.product(spectrum, unique_masses):
		combos.append(i)
	final = [list(elem) for elem in combos]
	for i in range(len(final)):
		new.append(final[i][0][:])
	for i in range(len(new)):
		new[i].append(final[i][1])
	return sorted(new)

def chop(spectrum):
	"""Removes peptides that are not consistent with spectrum masses"""
	matches = []
	length = len(spectrum[0])
	for i in range(len(spectrum)):
		if spectrum[i][length-1] in formatted_input and sum(spectrum[i]) in formatted_input and spectrum[i].count(spectrum[i][length-1]) <= formatted_input.count(spectrum[i][length-1]):
			matches.append(spectrum[i])	
	unique_matches = [list(elem) for elem in matches]
	return sorted(unique_matches)

def cyclopeptidesequencing(spectrum, m):
	potentials = chop(root(formatted_input))
	potentials2 = potentials
	circular = []
	circular_scores = []
	circular_peptides = []
	peptides = []	
	circular_aa = []
	circular_masses = []
	highest_score = []
	#while sum(potentials2[0]) != max(formatted_input):
	while len(potentials2[0]) != 4:
		potentials2 = expand(potentials2)
		potentials2 = get_leaderboard(potentials2, spectrum, m)
		#potentials2 = chop(potentials2)	
	for i in potentials2:
		for aa in i:
			peptides.append(str(mass_to_aa[aa]))
	peptide_length = len(potentials2[0])
	for i in range(0, len(peptides), peptide_length):
		y = ''.join(peptides[i:peptide_length+i])
		z=generating_theoretical_spectrum.generating_theoretical_spectrum(y)
		#if z == formatted_input:
		circular.append(z)
		circular_peptides.append(y)
	max_scores = max_score(circular, formatted_input, 10)
	for i in range(len(max_scores)):
		if max_scores[i]==max(max_scores):
			highest_score.append(potentials2[i])
			
		
	return highest_score
	#return potentials2
	"""for i in circular:
		for aa in i:
			circular_aa.append(integer_mass[aa])
	for i in range(0, len(circular_aa), peptide_length):
		circular_masses.append(circular_aa[i:i+ peptide_length])
	dashes = []
	for i in circular_masses:
		y = '-'.join([str(a) for a in i])
		dashes.append(y)"""
	#return circular_masses
	#return circular
	#return y
	return len(circular)
	#return ' '.join([str(i) for i in dashes])
	
	

#test = '0 71 113 129 147 200 218 260 313 331 347 389 460'
test2 =  '0 71 71 71 87 97 97 99 101 103 113 113 114 115 128 128 129 137 147 163 163 170 184 184 186 186 190 211 215 226 226 229 231 238 241 244 246 257 257 276 277 278 299 300 312 316 317 318 318 323 328 340 343 344 347 349 356 366 370 373 374 391 401 414 414 415 419 427 427 431 437 441 446 453 462 462 462 470 472 502 503 503 511 515 529 530 533 533 540 543 547 556 559 569 574 575 584 590 600 600 604 612 616 617 630 640 640 643 646 648 660 671 683 684 687 693 703 703 719 719 719 729 730 731 737 740 741 745 747 754 774 780 784 790 797 800 806 818 826 827 832 833 838 846 846 847 850 868 869 877 884 889 893 897 903 908 913 917 930 940 947 956 960 960 961 964 965 966 983 983 985 1002 1009 1010 1011 1021 1031 1031 1036 1053 1054 1058 1059 1062 1063 1074 1076 1084 1092 1103 1113 1122 1124 1130 1133 1134 1145 1146 1146 1149 1150 1155 1156 1171 1173 1174 1187 1191 1193 1200 1212 1221 1233 1240 1242 1246 1259 1260 1262 1277 1278 1283 1284 1287 1287 1288 1299 1300 1303 1309 1311 1320 1330 1341 1349 1357 1359 1370 1371 1374 1375 1379 1380 1397 1402 1402 1412 1422 1423 1424 1431 1448 1450 1450 1467 1468 1469 1472 1473 1473 1477 1486 1493 1503 1516 1520 1525 1530 1536 1540 1544 1549 1556 1564 1565 1583 1586 1587 1587 1595 1600 1601 1606 1607 1615 1627 1633 1636 1643 1649 1653 1659 1679 1686 1688 1692 1693 1696 1702 1703 1704 1714 1714 1714 1730 1730 1740 1746 1749 1750 1762 1773 1785 1787 1790 1793 1793 1803 1816 1817 1821 1829 1833 1833 1843 1849 1858 1859 1864 1877 1886 1890 1893 1900 1900 1903 1904 1918 1922 1930 1930 1931 1961 1963 1971 1971 1971 1980 1987 1992 1996 2002 2006 2006 2014 2018 2019 2019 2032 2042 2059 2060 2063 2067 2077 2084 2086 2089 2090 2093 2105 2110 2115 2115 2116 2117 2121 2133 2134 2155 2156 2157 2176 2176 2187 2189 2192 2195 2202 2204 2207 2207 2218 2222 2243 2247 2247 2249 2249 2263 2270 2270 2286 2296 2304 2305 2305 2318 2319 2320 2320 2330 2332 2334 2336 2336 2346 2362 2362 2362 2433'
formatted_input = format(test2)
print cyclopeptidesequencing(formatted_input, 325)
#two_aa_masses = root(formatted_input)

#wrong_answer = [[71, 129, 113, 147], [71, 129, 147, 113], [71, 147, 113, 129], [71, 147, 129, 113], [113, 147, 71, 129], [113, 147, 129, 71], [129, 71, 113, 147], [129, 71, 147, 113], [147, 71, 113, 129], [147, 71, 129, 113], [147, 113, 71, 129], [147, 113, 129, 71]]

#print get_leaderboard(wrong_answer, formatted_input, 10)
trial = [[0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 184, 200, 260, 276, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 184, 218, 242, 276, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 184, 200, 260, 276, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 184, 200, 260, 276, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 184, 218, 242, 276, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 184, 200, 260, 276, 313, 331, 347, 389, 460], [0, 71, 113, 129, 147, 200, 218, 242, 260, 313, 331, 347, 389, 460]]
#print max_score(trial, formatted_input, 10)








	

