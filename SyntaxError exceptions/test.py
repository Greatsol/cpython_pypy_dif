def foo(x, z, t, w):
	pass


def main():
	try:
		foo(0, z for z in range(10), 0, 0)
	except SyntaxError as err:
		print(err)


if __name__ == '__main__':
	main()