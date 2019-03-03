

def counting_pairs(input,k):
    '''
        @summary : This method find the unique pair of elements where 1st element and identify the pairs where element 2 - element 1 = k 
        @param : Input list and k value
        @return: list o tuples
    '''
    pair = []
    for i in input:
        for j in input:
            if (i,j) not in pair and i < j:
                pair.append((i,j))
    
    result = []
    for i in pair:
        if (i[1] - i[0]) == k:
            result.append(i)
    
    print result
        
print "Enter the K value:",
try:
    k = int(raw_input())
    input = []
    print "Please enter the Nnumber of Inputs:"
    n = int(raw_input())

    for i in range(n):
        input.append(int(raw_input()))
    counting_pairs(input,k)
except:
    print "Invalid input"



##Sample input
'''
Enter the K value: 1
Please enter the Nnumber of Inputs:
6
1
1
2
2
3
3

'''