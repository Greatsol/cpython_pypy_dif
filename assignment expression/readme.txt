Assignment expressions can now be used unparenthesized within set literals and set comprehensions, as well as in sequence indexes (but not slices).(https://docs.python.org/3/whatsnew/3.10.html)
Выражения присваивания теперь можно не обрамлять в скобки при создании множества и в генераторах множеств,
также в индексах последовательностей. Отличий от pypy3.9 я не нашёл и pull request на bugs.python.org тоже.
Подробннее о assignment expressions в PEP-572.

Команды для запуска
Cpython: python3.10 test.py
Pypy: pypy3.9 test.py