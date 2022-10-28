#!/Users/aleksey.antropov/miniconda/bin/python3

# Task: Convert the string 'this_is_the_text' to the string 'thisIsTheText' and vice versa.

input_strings = ['this_is_the_text', 'thisIsTheText', 'thereIsA_mistake!']

def cam_or_under (s: str) -> str:
    ret = str()
    i = 0
    is_under = False
    is_camel = False
    while i < len(s):
        if s[i] == '_':
            i += 1
            ret = ret + s[i].capitalize()
            i += 1
            is_under = True
            continue
        if s[i] == s[i].capitalize():
            ret = ret + '_' + s[i].lower()
            i += 1
            is_camel = True
            continue
        if s[i].isalnum():
            ret = ret + s[i]
            i += 1
        if is_under and is_camel:
            return('Err! The line has both styles!')
    return(ret)

for line in input_strings:
    print('Input: {}, Output: {}'.format(line, cam_or_under(line)))