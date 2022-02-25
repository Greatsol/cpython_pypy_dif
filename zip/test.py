test_list = [5, 6, 7]
test_tuple = ("a", "b", "c")
test_set = {1, 2, 3, 4}


def main():
    try:
        for number in zip(test_list, test_tuple, test_set, strict=True):
            print(number)
    except ValueError as err:
        print(err)
    except TypeError as err:
        print(err)

    # default value for strist is False
    for number in zip(test_list, test_tuple, test_set):
        print(number)


if __name__ == "__main__":
	main()
