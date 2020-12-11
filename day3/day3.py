class slopes:
    def __init__ (self,right,down):
        self.right=right
        self.down=down


inputList=[]

with open('day3_input.txt','r') as reader :
    line = reader.readline()
    while line!='':
        line= line.rstrip('\n')
        inputList.append(line)
        line = reader.readline()

lenghtOfArr = len(inputList)
width = len(inputList[0])-1





slopesList = [
    slopes(1,1),
    slopes(3,1),
    slopes(5,1),
    slopes(7,1),
    slopes(1,2),
]



outputSlopes =[]


finalOut=1


for x in slopesList:
    horizontalPosition=0
    verticalPosition=0
    numberOfTrees=0
    verticalPosition+=x.down
    horizontalPosition+=x.right
    while verticalPosition<lenghtOfArr:
        if(horizontalPosition>=width):
            horizontalPosition = horizontalPosition - width - 1
        if(inputList[verticalPosition][horizontalPosition]=='#'):
            numberOfTrees+=1
        verticalPosition+=x.down
        horizontalPosition+=x.right

    outputSlopes.append(numberOfTrees)
    finalOut = finalOut*numberOfTrees
        
print(outputSlopes)
print(finalOut)

