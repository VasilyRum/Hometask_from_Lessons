test_string = input('Enter string')
if len(test_string) < 2:
    output_string = ''
else:
    output_string = test_string[0]+test_string[1]+test_string[-2]+test_string[-1]
print (output_string)