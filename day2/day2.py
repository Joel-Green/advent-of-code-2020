class passwordChance:
    def __init__(self,minVal, maxVal, letter, password):
        self.minVal=minVal
        self.maxVal=maxVal
        self.letter=letter
        self.password=password



inputList = []

with open('day2_input.txt','r') as reader :
    line = reader.readline()
    while line!='':
        if line.rstrip('\n')!= '':
            inputList.append( passwordChance(int(line[0:line.find('-')]), int(line[line.find('-')+1:line.find(' ')]), line[line.find(' ')+1:line.find(':')], line[line.find(': ')+2:-1]))
        line = reader.readline()

# numberOfValidPasswords=0
# for val in inputList:
#     temp = val.password.count(val.letter)
#     if(temp<=val.maxVal and temp>=val.minVal):
#         numberOfValidPasswords = numberOfValidPasswords +1

# level 2
numberOfValidPasswords=0
for i,val in enumerate(inputList, start=0):
    temp = val.password.count(val.letter)
    try:
        print(i)
        print(val.password[val.minVal-1])
        print(val.password[val.maxVal-1])
        if((val.password[val.minVal-1]==val.letter and val.password[val.maxVal-1]!=val.letter)or(val.password[val.minVal-1]!=val.letter and val.password[val.maxVal-1]==val.letter)):
            numberOfValidPasswords = numberOfValidPasswords +1
    except:
        print('skip;',i)
        if(i==0):
            print (val.password[0],val.password[1],val.password[2],val.password[3],val.password[4],val.password[5],val.password[6],val.password[7],val.password[8],val.minVal,val.maxVal)
            break

print(numberOfValidPasswords)

