

def superstack(steps):
    '''
        @summary : This method stores the top element of the stack after every operation and returns the result once all operations are completed 
        @param : Input steps to perform stack operation
        @return: list
    '''
    stack = []
    result = []
#     import pdb;pdb.set_trace()
    try:
        for i in steps:
            i = i.split()
            
            if i[0] == 'push':
                stack.append(int(i[1]))
                result.append(stack[-1])
            elif i[0] == 'pop':
                val = stack.pop()
                if stack:
                    result.append(stack[-1])
                else:
                    result.append("EMPTY")
            elif i[0] == 'inc':
                for j in range(int(i[1])):
    #                 import pdb;pdb.set_trace()
                    stack[j] = stack[j] + int(i[2]) 
                if stack:
                    result.append(stack[-1])
                else:
                    result.append("EMPTY")
        print "========================================"           
        print "Result:"            
        for i in result:
            print i
    except:
        print "Invalid Input:Inputs should be a number %s"%(i)




print "Enter the Number of Inputs",
no_of_instructions = raw_input()
steps = []
for i in range(int(no_of_instructions)):
#     import pdb;pdb.set_trace()
    steps.append(raw_input())
    
superstack(steps)



###Sample Input
'''
Enter the Number of Inputs 12
push 4
pop
push 3
push 5
push 2
inc 3 1
pop
push 1
inc 2 2
push 4
pop
pop

'''
