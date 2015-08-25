#!/usr/bin/env python

f = open("dna1.fasta", "r")
file = f.read()
print(file.count('>'))
