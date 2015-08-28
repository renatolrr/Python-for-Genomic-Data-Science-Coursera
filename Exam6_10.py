#!/usr/bin/env python

fa="dna.example.fasta"

#Funcion sequencia
def sequ(fa):
	f= open(fa, "r")
	file = f.readlines()
	#print file
	sequences = []
	seq = ""
	for f in file:
		if not f.startswith('>'):
			f = f.replace(" ", "")
			f = f.replace("\n", "")
			seq = seq + f
		else:
			sequences.append(seq)
			seq = ""

	# Add the last seq
	sequences.append(seq)

	sequences = sequences[1:]
	
	return sequences
	
# Find all indexs	
def find_index(sequence,n):
		start_position = n-1
		start_indexs = []
		stop_indexs = []
		for i in range(n-1, len(sequence), 3):
			if sequence[i:i+3] == "ATG":
				start_indexs.append(i)
		

		# Find all stop codon indexs
		for i in range(n-1, len(sequence), 3):
			stops =["TAA", "TGA", "TAG"]
			if sequence[i:i+3] in stops:
				stop_indexs.append(i)
		ind=[start_position,start_indexs,stop_indexs]
		#print ind
		return ind
		
				
def find_orf(sequence,n):
		ind=find_index(sequence,n)
		start_position = ind[0]
		start_indexs = ind[1]
		stop_indexs = ind[2]
		orf = []
		mark = 0
		for i in range(0,len(start_indexs)):
			for j in range(0, len(stop_indexs)):
				if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
					orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
					mark = stop_indexs[j]+3
					break
		return orf


	
############################################################

#What is the length of the longest ORF appearing in any sequence in any of the 3 forward reading frames?
def punto6(fa):
	sequences=sequ(fa)

	n = 1
	lengths = []
	for i in sequences:
		# print("["+str(n)+"]")
		orfs = find_orf(i,1) + find_orf(i,2) + find_orf(i,3)
		for j in orfs:
			lengths.append(len(j))
		n += 1
	print(max(lengths))


###########################################
	

#Punto 6
print 'Punto 6'
punto6(fa)



