def option1():
	print "Hello world"

def option2():
	print "Hello florida"

print "What option do you want 1 or 2?"
option = raw_input()

if option == "1":
    option1()

elif option == "2":
	option2()

else:
	print "Invalid input"
