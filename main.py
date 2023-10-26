from random import shuffle

with open('private_keys.txt') as file:
    private_keys = [i.strip() for i in file.readlines()]


class Key:
    def __init__(self, digits: list, symbols: list) -> None:
        self.digits = digits
        self.symbols = symbols
        self.first_part, self.second_part = {}, {}


    def main(self, private_keys: list) -> list:
        encrypted_keys = []
        self.second_symbols = self.symbols.copy()

        shuffle(self.second_symbols)

        for key in private_keys:
            encrypted = self.encrypting(key)
            encrypted_keys.append(encrypted)

        self.configure_decrypt()

        return encrypted_keys


    def encrypting(self, key: str) -> str:
        half = len(key)//2

        key_first_part = key[:half]
        key_second_part = key[half:]

        for num in range(len(self.digits)):
            self.first_part[self.symbols[num]] = self.digits[num]
            self.second_part[self.second_symbols[num]] = self.digits[num]
            key_first_part = key_first_part.replace(self.digits[num], self.symbols[num])
            key_second_part = key_second_part.replace(self.digits[num], self.second_symbols[num])

        encrypted_key = key_first_part + key_second_part

        return encrypted_key


    def configure_decrypt(self) -> None:
        print('\n' + '='*150 + '\n\n' + ' '*60 + '|||Your decrypt function`s below|||\n\n' + '='*150)
        print(rf'''
first_part = {self.first_part}
second_part = {self.second_part}


def decrypt(key):
    half = len(key)//2

    first_part_keys = list(first_part.keys())

    key_first_part = key[:half]
    key_second_part = key[half:]

    for symbol in first_part_keys:
        key_first_part = key_first_part.replace(symbol, first_part[symbol])
        key_second_part = key_second_part.replace(symbol, second_part[symbol])

    encrypted_key = key_first_part + key_second_part

    return encrypted_key


with open('encrypted_keys.txt') as file:
    private_keys = [decrypt(i.strip()) for i in file.readlines()]

#   ^^^^^^^^^^^^ change this variable to variable in your code
#   |||||||||||| ex: KEYS

# code below is just for decrypt. if you need to paste this code in your script, just delete code below

with open('private_keys.txt', 'w') as file:
    file.write('\n'.join(private_keys))
''')


if __name__ == '__main__':

    # each digit only once. ex: 0123 or 6234 or 435216 etc. No more than 10
    digits = [i for i in input('Type the digits for replace:\n')]

    [exit(print('You chose equal digits twice'))
        for i in digits if digits.count(i) > 1]

    # each symbol only once. ex: $<:>|#@! . No more than 10
    # must be equal to the count of digits. 
    symbols = [i for i in input("\n" + r"Type the symbols (don`t use '\'):" + "\n")]
    
    [exit(print('You chose equal symbols twice'))
        for i in symbols if symbols.count(i) > 1]

    [exit(print('You chose symbols&symbols or digits&digits'))
        for i in symbols if i in digits]

    if len(digits) != len(symbols):
        exit(print('Digits count must be equal to symbols'))
    elif 1 > len(digits) > 10:
        exit(print('You chose wrong digits count'))
    else:
        print(f'\nYou chose these digits {digits}\n'
              f'You chose these symbols: {symbols}')

    encrypted_keys = Key(digits, symbols).main(private_keys)

    with open('encrypted_keys.txt', 'w') as file:
        file.write('\n'.join(encrypted_keys))
