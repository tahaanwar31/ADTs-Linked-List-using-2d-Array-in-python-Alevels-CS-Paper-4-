#DECLARE linkedList:ARRAY[0:9 , 0,1] OF INTEGER
linkedList=[[0]*2 for x in range(10)]
linkedList[0]=[1,1]
linkedList[1]=[5,4]
linkedList[2]=[6,7]
linkedList[3]=[7,-1]
linkedList[4]=[2,2]
linkedList[5]=[0,6]
linkedList[6]=[0,8]
linkedList[7]=[56,3]
linkedList[8]=[0,9]
linkedList[9]=[0,-1]
startPointer=0
emptyList=5
def addNode(currentPointer):
    global linkedList
    global startPointer
    global emptyList
    datatoadd = int(input("Please enter the data you want to add: "))
    if emptyList<0 or emptyList>9:
        return False
    else:
        freeList=emptyList
        emptyList=linkedList[emptyList][1]
        newNode=[datatoadd,-1]
        linkedList[freeList]=newNode
        previousPointer=currentPointer
        while currentPointer!=-1:
            previousPointer=currentPointer
            currentPointer=linkedList[currentPointer][1]
        linkedList[previousPointer][1]=freeList
        return True
def deleteNode():
    global linkedList
    global startPointer
    global emptyList
    currentPointer=startPointer
    datatodelete=int(input("Please enter the data you want to delete: "))
    previousPointer=currentPointer
    while currentPointer!=-1 and linkedList[currentPointer][0]!=datatodelete:
        previousPointer=currentPointer
        currentPointer=linkedList[currentPointer][1]
    linkedList[previousPointer][1]=linkedList[currentPointer][1]
    linkedList[currentPointer][1]=emptyList
    emptyList=currentPointer
def outputNodes(startPointer):
    global linkedList
    currentPointer=startPointer
    while currentPointer!=-1:
        print(linkedList[currentPointer][0])
        currentPointer=linkedList[currentPointer][1]
def findItem(startPointer,valueSearch):
    currentPointer=startPointer
    global linkedList
    while currentPointer!=-1:
        if linkedList[currentPointer][0]==valueSearch:
            return currentPointer
        else:
            currentPointer=linkedList[currentPointer][1]
    return currentPointer






