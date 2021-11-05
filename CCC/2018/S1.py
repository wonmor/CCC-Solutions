numVil = int(input())
yourMom = []
dick = []
asian = []
final = []
bossBaby = 1000000000.0

for i in range(numVil):
    gay = int(input())
    yourMom.append(gay)

yourMom.sort()

for i in range(1, len(yourMom) - 1):
    dick.append(float(yourMom[i] - yourMom[i - 1]) / 2)
    asian.append(float(yourMom[i + 1] - yourMom[i]) / 2)

for i in range(len(asian)):
    final.append(float(dick[i] + float(asian[i])))
    
bossBaby = float(min(final))
print(bossBaby)