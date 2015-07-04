def circular_peptides(ex):
	"""returns the possible subpeptides of circular protein ex."""
	count = 1
	peptides = []
	count2 = 0	
	#forward peptides
	while count <= len(ex):
		for i in range(len(ex)):
			peptides.append(ex[i:count])
		count = count + 1
	#reverse peptides
	for i in range(2, len(ex)):
		count = i - 1
		while count >= 1:
			peptides.append(ex[i:]+ ex[:count])
			count = count - 1
	final_list = filter(None, peptides)
	return final_list


# idea behind getting reverse peptides:
# GASPTCI
# SPTCIG, PTCIGA, PTCIG, TCIGAS, TCIGA, TCIG, CIGASP, CIGAS, CIGA, CIG, IGASPT, IGASP, IGAS, IGA, IG 
# 6,      6, 5           6, 5, 4              6, 5, 4, 3                6, 5, 4, 3, 2
#[2:]+[:1], [3:]+[:2][:1] [4:]+[:3][:2][:1] [5:]+[:4][:3][:2][:1]  [6:]+[:5][:4][:3][:2][:1]