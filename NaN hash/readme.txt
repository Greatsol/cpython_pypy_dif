Ранее хеш от любого объекта со значением NaN был равен 0, 
даже если значения NaN не равны дру другу, что приводило к большому количеству коллизий при создании
словарей и множеств, содержащих большое количество NaN-ов.

Команды для запуска
Cpython: python3.10 test.py
Pypy: pypy3.9 test.py