import itertools
import pprint
import generating_theoretical_spectrum

integer_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

mass_to_aa =  {v: k for k, v in integer_mass.items()}

# get unique aa masses from integer_mass dict
integer_masses = integer_mass.values()
unique_masses = list(set(integer_masses))

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

def cyclopeptidesequencing(spectrum):
	potentials = chop(root(formatted_input))
	potentials2 = potentials
	circular = []
	peptides = []	
	circular_aa = []
	circular_masses = []
	while sum(potentials2[0]) != max(formatted_input):
		potentials2 = expand(potentials2)
		potentials2 = chop(potentials2)	
	for i in potentials2:
		for aa in i:
			peptides.append(str(mass_to_aa[aa]))
	peptide_length = len(potentials2[0])
	for i in range(0, len(peptides), peptide_length):
		y = ''.join(peptides[i:peptide_length+i])
		z=generating_theoretical_spectrum.generating_theoretical_spectrum(y)
		if z == formatted_input:
			circular.append(y)
	for i in circular:
		for aa in i:
			circular_aa.append(integer_mass[aa])
	for i in range(0, len(circular_aa), peptide_length):
		circular_masses.append(circular_aa[i:i+ peptide_length])
	dashes = []
	for i in circular_masses:
		y = '-'.join([str(a) for a in i])
		dashes.append(y)
	#return circular_masses
	#return circular
	#return potentials2
	#return y
	#return peptide_length
	return ' '.join([str(i) for i in dashes])


	

test = '0 99 101 113 113 113 113 114 156 212 212 214 215 226 226 269 270 325 325 327 328 339 368 371 383 438 438 440 441 481 482 484 484 539 551 554 583 594 595 597 597 652 653 696 696 707 708 710 710 766 808 809 809 809 809 821 823 922'
#input = '0 113 128 186 241 299 314 427'
#formatted_input = format('0 113 128 186 241 299 314 427')
formatted_input = format(test)

print cyclopeptidesequencing(formatted_input)
