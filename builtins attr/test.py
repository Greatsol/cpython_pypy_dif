def foo():
	pass


def main():
	try:
		print(f"{('print' in foo.__builtins__)=}")
		print(f"{('ord' in foo.__builtins__)=}")
	except AttributeError as err:
		print(err)


if __name__ == '__main__':
	main()