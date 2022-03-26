def rev_string(str):
    rev_string = ''
    index = len(str)
    while index > 0:
        rev_string = rev_string + str[index-1]
        index -=1
    return rev_string

print(rev_string("1234abcd"))