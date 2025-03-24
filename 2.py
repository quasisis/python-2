def count_ones_in_binary_expression():
    # Вычисляем значение выражения
    value = 8*2020 + 4*2017 + 26 - 1

    # Преобразуем значение в двоичную систему и считаем количество единиц
    binary_representation = bin(value)
    ones_count = binary_representation.count('1')

    return ones_count

if __name__ == "__main__":
    result = count_ones_in_binary_expression()
    print(f"Количество единиц в двоичной записи: {result}")
