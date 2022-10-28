class Int(int):
    """
    Класс дополняет встроенный тип int возможностью складывать int со строкой
    """
    numbers = {'нуль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5}

    def __add__(self, other):
        if isinstance(other, str):
            if other.isdigit():
                other = int(other)
            else:
                if other.lower() in self.numbers:
                    other = self.numbers[other.lower()]
                else:
                    try:
                        other = float(other)
                        return self.__int__() + other
                    except ValueError:
                        pass
                    raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 0 по 5.')
        return super().__add__(other)


if __name__ == '__main__':
    x = Int(5)
    print(x + 10)  # 15
    print(x + '5')  # 10
    print(x + '12.5')  # 17.5
    print(x + 'один')  # 6
    print(x + 'пять')  # 10
    # print(x + 'шесть')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    # print(x + 'a')  # TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.
    print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'
