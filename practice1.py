#Take user input (string)
#if the length of the string is greater than 3
#add "ing" as a suffix in the original string
#else print the same string given by the user

x=str(input(""))
y=len(x)
if y>3:
    print(x+"ing")
else:
    print(x)

