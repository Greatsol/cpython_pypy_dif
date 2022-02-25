test_numbers = [15, -17, 123435885, 0]


def main():
    for number in test_numbers:
        try:
            print(f"{number=}")
            print(f"{number.bit_count()=}")     
        except AttributeError as err:
            print(err)


if __name__ == "__main__":
	main()
