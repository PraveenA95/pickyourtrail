

def find_unique_elements(input):
    '''
        @summary : This method finds the duplicate elements in the list and increment the value until the value is unique in the list. 
        @param : Input list
        @return: int
    '''
    for i in range(len(input)):
        if input[:i+1].count(input[i]) == 1:
            continue
        else:
            while input[:i+1].count(input[i]) != 1:
                input[i] = input[i]+1

    return sum(input)
print "Please enter the number of Inputs:"
input = []
try:
    n = int(raw_input())
    for i in range(n):
        input.append(int(raw_input()))
    result = find_unique_elements(input)
    print "Result :",
    print result

except:
    print "Please enter a valid Input"
 

##Sample Input
'''
Please enter the number of Inputs:
3
1
2
2

'''
