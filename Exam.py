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
	
# Find all ATG indexs	
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
		ind=[]
		return ind
		
	
				
def find_orf(sequence,n):
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
		orf = []
		mark = 0
		for i in range(0,len(start_indexs)):
			for j in range(0, len(stop_indexs)):
				if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
					orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
					mark = stop_indexs[j]+3
					break
		return orf

	
#############################################################

#How many records are in the file? 
def contar(fa): 
	f= open(fa, "r")
	file = f.read()
	return file.count('>')	
	
#What are the lengths of the sequences in the file?
#What is the longest sequence and what is the shortest sequence? 


def longuitud(fa):
	sequences=sequ(fa)

	lengths = [len(i) for i in sequences]
	#print lengths
	print "Maximo y minimo:",max(lengths),' ',min(lengths)

#What is the length of the longest ORF in the file?
def OpenReadingFrame(fa):
	sequences=sequ(fa)

	#  [len(i) for i in sequences]
	n = 1
	lengths = []
	for i in sequences:
		orfs = find_orf(i,2)
		for j in orfs:
			lengths.append(len(j))

	# orf_lengths = [len(i) for i in orf_2 if i]
	print 'El maximo Orf es de ',max(lengths)


#What is the starting position of the longest ORF in reading frame 3 in any of the sequences?
def Orf3(fa):
	sequences=sequ(fa)

	# Find orf 3
	def find_orf_3(sequence):
		# Find all ATG indexs
		start_position = 2
		start_indexs = []
		stop_indexs = []
		for i in range(2, len(sequence), 3):
			if sequence[i:i+3] == "ATG":
				start_indexs.append(i)

		# Find all stop codon indexs
		for i in range(2, len(sequence), 3):
			stops =["TAA", "TGA", "TAG"]
			if sequence[i:i+3] in stops:
				stop_indexs.append(i)

		orf = []
		mark = 0
		start_position = {}
		for i in range(0,len(start_indexs)):
			for j in range(0, len(stop_indexs)):
				if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
					orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
					start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
					mark = stop_indexs[j]+3
					break
		return start_position


	#  [len(i) for i in sequences]

	n = 1
	lengths = []
	for i in sequences:
		print("["+str(n)+"]")
		orfs = find_orf_3(i)
		print(orfs)
		n += 1


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
	
#Punto 1
print 'Punto 1'	
HowMany = contar(fa) 
print ("Hay:" + str(HowMany))

#Punto 2
print 'Punto 2'
longuitud(fa)

#Punto 3 y 4
print 'Punto 3 y 4'
OpenReadingFrame(fa)

#Punto 5
print 'Punto 5'
Orf3(fa)

#Punto 6
print 'Punto 6'
punto6(fa)



