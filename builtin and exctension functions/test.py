class A:
	def __init__(self, val):
		self.val = val

	def __index__(self):
		return self.val


class B:
	def __init__(self, val):
		self.val = val

	def __int__(self):
		return self.val


def main():
	a = A(65)
	b = B(65)
	print(chr(a))
	try:
		print(chr(b))
	except TypeError as err:
		print(err)


if __name__ == '__main__':
	main()