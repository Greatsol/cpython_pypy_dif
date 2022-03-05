def main():
	test_tuple = (1, 2, 3, 4)
	test_list = list(test_tuple)

	print(f"{({x:=10})=}, {({x := y for y in test_list})=}")

	print(f"{test_tuple=}, {(test_tuple[x:=0])=}")
	print(f"{test_list=}, {(test_list[x:=2])=}")


if __name__ == '__main__':
	main()