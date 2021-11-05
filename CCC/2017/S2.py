lowTide, highTide, resultTide = [], [], []

numAttempt = int(input())
value = [int(x) for x in input().split()]

value.sort() 

if len(value) % 2 == 0:
    divVar = int(len(value) / 2) - 1

else:
    divVar = int(len(value) / 2)

for i in range(divVar, -1, -1):
    lowTide.append(value[i])
    
for j in range(divVar + 1, len(value)):
    highTide.append(value[j])

for k in range(int(numAttempt / 2)):
    print(str(lowTide[k]) + " " + str(highTide[k]) + " ", end = "")

if len(value) % 2 != 0:
    print(lowTide[-1])