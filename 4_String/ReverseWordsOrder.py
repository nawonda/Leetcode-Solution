# new way 
def new_reverse_world(s):
    revword = " ".join(s.split()[::-1])
    return revword

#old way
def reverse_word_in_string(s):
    
    result = []
    world = ''
    
    for i in s:

        if(i == ' ' or i == '\t'):
            result.append(world)
            world = ''            
        else:
            world = world + i
    
    if world:
        result.append(world)
    
    final_string = ''
    
    for j in result:        
        final_string = j + ' ' + final_string
                
    return final_string

    
s = "the sky is blue"
print reverse_word_in_string(s)