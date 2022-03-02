from decimal import Decimal


def main():
	float_nan_hash = hash(float('NaN'))
	decimal_nan_hash = hash(Decimal('NaN'))
	print(f"{float_nan_hash=}\n{decimal_nan_hash=}\n{(float_nan_hash == decimal_nan_hash)=}")


if __name__ == '__main__':
	main()
