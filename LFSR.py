import random


class Generator:
    def __init__(self, links=None):
        # по-умолчанию берем значения для регистра длиной 10
        # считаем, что первый символ самый большой
        self.links = links or (9, 4, 0)
        self.buffer = []

        self.__init_buffer()

    def next(self):
        self.__shift_bits()
        return self.__convert_to_int()

    def __shift_bits(self):
        value = self.__form_bit()
        del self.buffer[len(self.buffer) - 1]
        self.buffer.insert(0, value)

    def __convert_to_int(self):
        value = "".join([str(item) for item in self.buffer])
        return int(value, 2)

    def __form_bit(self):
        # возвращает значение следующего бита
        value = 0

        for index in self.links:
            value += self.buffer[index]

        return value % 2

    def __init_buffer(self):
        # предзаполнение буфера
        for _ in range(self.links[0] + 1):
            self.buffer.append(random.randint(0, 1))


p=Generator()
for _ in range(10):
    print(p.next())
