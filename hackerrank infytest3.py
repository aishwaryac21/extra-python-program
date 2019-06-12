##infy_10
def string_both_ends(input_string):
    if(len(input_string)<2):
        return -1
    else:
        s=""
        s=input_string[0:2]+input_string[len(input_string)-2:len(input_string)]
        return s

input_string=input("")
print(string_both_ends(input_string))
