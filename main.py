fs=open('input.txt','r')

print(fs.read())
myDict={"Fitbit Plus": 7980, "IPods": 22349, "MI Band": 999,"Cult Pass": 2799,
"Macbook Pro": 229900,"Digital Camera": 11101,"Alexa": 9999,
"Sandwich Toaster": 2195,"Microwave Oven": 9800,"Scale": 4999}
sorted = {k: v for k, v in sorted(myDict.items(), key=lambda item: item[1])}
listt = zip(sorted.keys(), sorted.values()) 
listt = list(listt)
numOfEmp =int(input("Number of the employees:"))
index = 0
diff = listt[numOfEmp-1][1] - listt[0][1]
i = 1
while(i < len(listt) - numOfEmp+1):
    if listt[i+numOfEmp-1][1] - listt[i][1] < diff:
        index = i
        diff = listt[i+numOfEmp-1][1] - listt[i][1]
    i += 1
print('Goodies that are selected for distribution are:')
j = 0
while(j < numOfEmp):
    print(listt[index+j][0]+':', listt[index+j][1])
    j += 1
print()
print('And the difference between the chosen goodie with highest price and the lowest price is', diff)
