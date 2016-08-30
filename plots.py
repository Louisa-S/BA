import sys
import matplotlib.pyplot as plt

def curves():
	f1 = "results/non-result1-2-2-1.txt"
	f2 = "results/result1-2-2-1.txt"

	nons = []
	reals = []

	with open(f1) as g1:
		next(g1)
		for line in g1:
			line = line.split()
			nons.append(line[1])
			
			
	with open(f2) as g2:
		next(g2)
		for line in g2:
			line = line.split()
			reals.append(line[1])
			
				
	y = range(22)

	plt.plot(y,nons[:22], "-r", label="non targets")
	plt.plot(y, reals[:22], "-b", label="true targets")
	plt.xlabel("nucleotides")
	plt.ylabel("complementarity")
	plt.legend(loc="upper right")
	plt.savefig("results/curves1-2-2-1.png")


def scores():
	x = dict()
	
	with open("results/scores.txt") as f:
		for line in f:
			if line == "\n":
				break
			else:
				if int(line[:-1) in x:
					x[int(line[:-1)) += 1
				else:
					x[int(line[:-1)] = 1
					
	yvals = range(max(x.keys()))
	
	plt.plot(yvals,
				
	
