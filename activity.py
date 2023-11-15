import os

file_name = 'prime_numbers_from_1_to_250.txt'

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
                for number in range(1, 251):
                        if is_prime(number):
                                file.write(str(number) + '\n')
else:
        print("text file already existing")
