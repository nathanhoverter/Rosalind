import circular_peptides

integer_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def generating_theoretical_spectrum(protein):
	mass_list = [0]
	sub_peps = circular_peptides.circular_peptides(protein)
	for i in sub_peps:
		if len(i) > 1:
			count = 0
			for aa in i:
				count = count + integer_mass[aa]
			mass_list.append(count)					
		else:
			mass_list.append(integer_mass[i])
	sorted_list = sorted(mass_list)
	#out = '[' + ' '.join(str(item) for item in sorted_list)+ ']'
	return sorted_list
#print generating_theoretical_spectrum('LQW')





