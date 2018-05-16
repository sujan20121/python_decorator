import time

def time_it(func):
	''' 
this is the decorator
decorators help prevent code duplication
they also help reduce the clutter in the functions, allowing for better
code readability.
	'''
	def wrapper(*args,**kwargs):
	'''
	Here the wrapper() function holds the core components
	of the decorator.
	'''
		start = time.time()
		result = func(*args,**kwargs)
		end = time.time()
		print(func.__name__ + " took " + str((end-start)*1000) + " milli seconds")
		return result
	return wrapper
	
@time_it #this step is called decoration
def calc_square(numbers):
	result = []
	for number in numbers:
		result.append(number**2)
	return result
	
@time_it	
def calc_cube(numbers):
	result = []
	for number in numbers:
		result.append(number**3)
	return result

array = range(1,19000)
out_square = calc_square(array)
	'''
	Upon calling the function calc_square(), the decorator
	is called first
	'''
out_cube = calc_cube(array)
	
