inputList = []
with open('program1_input.txt','r') as reader :
    line = reader.readline()
    while line!='':
        line = reader.readline()
        if line.rstrip('\n')!= '':
            inputList.append(int(line.rstrip('\n')))



for i in range(len(inputList)):
    for j in range(i,len(inputList)):
        for k in range(j,len(inputList)):
            if ((i!=j) and (i!=k)):
                if(inputList[i]+inputList[j]+inputList[k]==2020):
                    print(inputList[i]*inputList[j]*inputList[k])



