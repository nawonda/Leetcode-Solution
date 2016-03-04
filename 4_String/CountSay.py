'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

'''
def count_say(n):
    result = [1]
    
    for i in range(1,n):

        previous = result
        result = []
        count = 1
        num = previous[0]
        
        for j in range(1,len(previous)):
            if previous[j] == num:
                count += 1
            else:                       
                result.append(str(count))
                result.append(str(num))
                num = previous[j]
                count = 1

        result.append(str(count))
        result.append(str(num))

    return result
                  
print count_say(6)