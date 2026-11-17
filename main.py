import types

class FlatIterator:
# принимает список списков и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer = 0
        self.inner = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.outer < len(self.list_of_list) and self.inner >= len(self.list_of_list[self.outer]):
            self.outer += 1
            self.inner = 0
            if self.outer >= len(self.list_of_list):
                raise StopIteration
        
        item = self.list_of_list[self.outer][self.inner]
        self.inner += 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item, "Что-то не так, списки не совпадают"

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], "Решение не совпадает с ответом"



def flat_generator(list_of_lists):

    for inner_list in list_of_lists:
        for item in inner_list:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item, "Что-то не так, списки не совпадают"

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], "Решение не совпадает с ответом"

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType), "Кажется, это не генератор 0_0"


if __name__ == '__main__':
    test_1()
    test_2()
