Если object.__ipow__() возвращает NotImplemented, оператор кореектно перейдёт к object.__pow__() и object.__rpow__().
Тест одинаково срабатывает для pypy3.9 и cpython3.10.

Команды для запуска
Cpython: python3.10 test.py
Pypy: pypy3.9 test.py