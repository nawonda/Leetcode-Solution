'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Subscribe to see which companies asked this question
'''

def new_palindrome(str):
    start = 0
    end = len(str)-1
    
    while start < end:
        #skip if not alnum
        while start < end and not str[start].isalnum():
            start+=1
        while start < end and not str[end].isalnum():
            end-=1
        if(start < end and str[start].lower() != str[end].lower()):
            return False
        
        start+=1
        end-=1
    
    return True
    
    
    
str = "A man, a plan, a canal: Panama"    
#print palindrome(str)
print new_palindrome(str)