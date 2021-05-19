import os

def calculating(cal):

	value = cal[0]

	for i in range(1,len(cal)):

		if cal[i] == '+':

			i += 1

			if cal[i] == '+' or cal[i] == '-':

				print("Syntax Error ; Double operator")
				exit(0)

			value += cal[i]


		elif cal[i] == '-':

			i += 1

			if cal[i] == '+' or cal[i] == '-':

				print("Syntax Error ; Double operator")
				exit(0)

			value -= cal[i]


	cal.clear()

	return value



# ";"
def gmr_1( stack , cal , n , isN ):

	if isN:

		cal.append(n)
		n = 0
		isN = False

	stack.append(calculating(cal))

	return stack , cal , n , isN 



# ":"
def gmr_2( stack , cal , n , isN ):

	im = stack[len(stack)-1]

	if isN:

		cal.append(str(n)+im)
		n = 0
		isN = False

	else:

		cal.append(im)

	return stack , cal , n , isN 



# "."
def gmr_3( stack , cal , n , isN ):

	if isN:

		cal.append(n)
		n = 0
		isN = False

	stack.pop()	

	return stack , cal , n , isN 



# "+"
def gmr_4( stack , cal , n , isN ):

	if isN:

		cal.append(n)
		n = 0
		isN = False

	cal.append('+')

	return stack , cal , n , isN 


# "-"
def gmr_5( stack , cal , n , isN ):

	if isN:

		cal.append(n)
		n = 0
		isN = False

	cal.append('-')

	return stack , cal , n , isN



# "!"
def gmr_6( stack , cal , n , isN ):

	if isN:

		cal.append(n)
		n = 0
		isN = False

	print(calculating(cal))

	return stack , cal , n , isN



def lexer(code):


	stack = []
	cal = []
	n = 0
	isN = False


	gmr_list = {

		";" : gmr_1,
		":" : gmr_2,
		"." : gmr_3,
		"+" : gmr_4,
		"-" : gmr_5,
		"!" : gmr_6

	}


	if code[-1] != "!":
		print("Error")
		exit(0)


	for i in range(0,len(code)):

			grm_run = gmr_list.get(code[i],"False")

			if grm_run == "False":

				pass


			else:

					stack , cal , n , isN = grm_run(stack , cal , n , isN)


			if '0' <= code[i] <= '9':

				n = n*10 + int(code[i])
				isN = True




if __name__ == "__main__":

	code = input("semi > ")

	lexer(code)
    
