import itertools

def is_valid(code):
    # Проверяем, что буква Й не стоит на первом или последнем месте
    if code[0] == 'Й' or code[-1] == 'Й':
        return False
    # Проверяем, что буква Й не стоит рядом с буквой Е
    if 'ЕЙ' in code or 'ЙЕ' in code:
        return False
    return True

def generate_codes():
    letters = ['А', 'Н', 'Д', 'Р', 'Е', 'Й']
    valid_codes = set()

    # Генерируем все возможные комбинации длиной 6
    for code in itertools.product(letters, repeat=6):
        code_str = ''.join(code)
        # Проверяем, что буква Й используется не более одного раза
        if code_str.count('Й') <= 1 and is_valid(code_str):
            valid_codes.add(code_str)

    return len(valid_codes)

if __name__ == "__main__":
    total_codes = generate_codes()
    print(f"Количество различных кодов: {total_codes}")
