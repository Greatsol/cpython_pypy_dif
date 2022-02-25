test_dict = {
        'key1': 15,
        'key2': 'test_string',
        'key3': [1, 2, 3]
        }


def test_dict_mapping():
    dv = test_dict.values()
    dk = test_dict.keys()
    di = test_dict.items()
    for el in (dv, dk, di):
        print(el)
        try:
            print(f'{el.mapping=}')
        except AttributeError as err:
            print(err)
        try:
            print(f'size of element: {el.__sizeof__()}')
        except AttributeError as err:
            print(err)
        print('\n')


if __name__ == '__main__':
    test_dict_mapping()
