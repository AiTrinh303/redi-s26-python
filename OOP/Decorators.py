def a_new_decorator(a_func):

	def wrapTheFunction():

		print("I am doing some boring work before executing a_func()")

		a_func()

		print("I am doing some boring work after executing a_func()")

	return wrapTheFunction

# def a_function_without_decoration():
# 	print("Hello world!")

@a_new_decorator

def a_function_requiring_decoration():
	print("Hello world!")
	
a_function_requiring_decoration()    