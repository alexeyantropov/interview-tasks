#!/Users/aleksey.antropov/miniconda/bin/python3

# Task: Convert the string 'this_is_the_text' to the string 'thisIsTheText' and vice versa.

input_strings = ['this_is_the_text', 'thisIsTheText', 'thereIsA_mistake!']

def cam_or_under (s: str) -> str:
    # A var for collecting an output string.
    ret = str()
    # A pointer initial value. It points to the start of the line.
    i = 0
    # Two boolean variables for a wrong input line detection. The wrong line сontains signs of the camelCase and the underscored style at same time.
    is_under = False
    is_camel = False
    while i < len(s):
        if s[i] == '_':                     # Convert to the camelCase.
            ret = ret + s[i+1].capitalize()
            i += 2
            is_under = True
            
        if s[i] == s[i].capitalize():       # Convert to the underscored style.
            ret = ret + '_' + s[i].lower()
            i += 1
            is_camel = True
            
        if s[i].isalnum():                  # Just add a simlpe letter to the output var.
            ret = ret + s[i]
            i += 1
        if is_under and is_camel:           # Return an error when the line is wrong.
            return('Err! The line has both styles!')
    return(ret)

for line in input_strings:
    print('Input: {}, Output: {}'.format(line, cam_or_under(line)))
