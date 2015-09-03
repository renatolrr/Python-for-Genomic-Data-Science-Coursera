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


#What is the length of the longest ORF that appears in the sequence with the identifier gi|142022655|gb|EQ086233.1|97?

# Find the sequence with the identifier num
def find_idenfitier(num):
	f = open(fa, "r")
	file = f.readlines()
	seq = ""
	identifier = 0
	for i in range(0, len(file)):
		if num in file[i]:
			identifier = i

	for f in file[identifier+1:]:
		if not f.startswith('>'):
			f = f.replace(" ", "")
			f = f.replace("\n", "")
			seq = seq + f
		else:
			break
			
	lengths = []
	orfs = find_orf(seq,1) + find_orf(seq,2) + find_orf(seq,3)
	for j in orfs:
		lengths.append(len(j))

	print(max(lengths))
	
	
#Find the most frequently occurring repeat of length 6 in all sequences. How many times does it occur in all?
def find_length(num):
	f = open(fa, "r")
	file = f.readlines()

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

	def get_all_repeats(sequence):
		length = len(sequence)
		repeats = []
		for i in range(length):
			repeats.append(sequence[i:i + (num*2)])
		return repeats

	all_six_repearts = []
	for i in sequences:
		repeats_list = get_all_repeats(i)
		for j in repeats_list:
			all_six_repearts.append(j)

	def most_common(lst):
		return max(set(lst), key=lst.count)

	print(most_common(all_six_repearts))
	print(all_six_repearts.count(most_common(all_six_repearts)))

###########################################
	

#Punto 6
print 'Punto 6'
punto6(fa)

#Punto 7
print 'gi|142022655|gb|EQ086233.1|97'
print 'Hay que cambiar la cadena que se busca'
num="gi|142022655|gb|EQ086233.1|97"
find_idenfitier(num)

#Punto 8,9 y 10
print 'Modificar el numero en la busqueda de string, dependiendo de la pregunta'
num=6
find_length(num)



