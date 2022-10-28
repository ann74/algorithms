class Int(int):
    """
    Класс дополняет встроенный тип int возможностью складывать int со строкой
    """
    def __add__(self, other):
        if isinstance(other, str):
            numbers = {'нуль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5}
            if other.isdigit():
                return self.__int__() + int(other)
            other = other.lower()
            if other in numbers:
                return self.__int__() + numbers[other]
            raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 0 по 5.')
        return super().__add__(other)


if __name__ == '__main__':
    x = Int(5)
    print(x + 10)  # 15
    print(x + '5')  # 10
    print(x + 'один')  # 6
    print(x + 'пять')  # 10
    # print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    # print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
