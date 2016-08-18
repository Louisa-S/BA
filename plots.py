import sys
import matplotlib.pyplot as plt


f1 = "results/non-result1-2-2-1"
f2 = "results/result1-2-2-1"

nons = []
reals = []

with open(f1) as g1:
	next()
	for line in g1:
		line = line.split()
		nons.append(line[1])
		
		
with open(f2) as g2:
	next()
	for line in g2:
		line = line.split()
		reals.append(line[1])
		
			
y = range(22)

plt.plot(y,nons[:22], y, reals[:22])
plt.show()
