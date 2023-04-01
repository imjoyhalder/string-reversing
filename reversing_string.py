def str_reversing(string):
    reversed_string = ""
    for char in string:
        
        reversed_string = char + reversed_string
        print(reversed_string)  # output: dlrow olleh

str_reversing(input("Input String: "))

