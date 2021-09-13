def bubbleSort(nList):
    for i in range(len(nList)-1,0,-1):
        for j in range(i):
            if nList[j]>nList[j+1]:
                temp = nList[j]
                nList[j] = nList[j+1]
                nList[j+1] = temp
    print("\nSort:",nList)
    
nList=[int(i) for i in input("Enter list(Use '1,3,2'): ").split(',')]
bubbleSort(nList)