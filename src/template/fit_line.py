"""
Code that can be extended to fit a line.

author: @arjunsavel
"""
import sys

def exp_func(base, power):
    """
	An exponential function.

	
	Inputs:
		:base: (float) The base of the exponent.
		:power: (float) The power of the exponent.


	Outputs:
		:exponented: (float) The result of the exponent base^power.

	"""
    exponented = pow(base, power)
    return exponented


# to call this as a script from command line with args
if __name__ == '__main__':
	def check_type(val):
		"""
		Checks whether an input is a float or integer.

		Inputs
		------
			:val: input to be checked.

		Outputs
		-------
			:allowed: (bool) whether the input is an allowed type.
		"""
		allowed_types = [int, float]
		try:
			allowed = type(eval(val)) in allowed_types

		# if there's a NameError, tried to evaluate a string that isn't a var
		except NameError:
			allowed = False

		return allowed



	# type check
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]

	

	if not check_type(arg1) or not check_type(arg2):
		raise ValueError('Make sure arguments are floats or integers!')

	base = eval(sys.argv[1])
	power = eval(sys.argv[2])

	result = exp_func(base, power)
	print(result)

