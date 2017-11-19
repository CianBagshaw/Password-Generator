from random import randint

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def random_letter ():
    letter = randint(0, len(alphabet) - 1)
    letter = alphabet[letter]

    return letter

def random_number ():
    number = randint(1, 9)

    return str(number)

def create_password (lenght, numbers = True, letters = True):
    minimum_lenght, maximum_lenght = lenght
    lenght = randint(minimum_lenght, maximum_lenght)

    password = str('')
    
    for loop in range(lenght):

        #Letters and numbers
        if numbers == True and letters == True:

            character = randint(1, 2)

            if character == 1: #Letter
                password = password + random_letter()

            if character == 2: #number
                password = password + random_number()

        #Just letters
        if numbers == False and letters == True:
            password = password + random_letter()

        #Just numbers
        if numbers == True and letters == False:
            password = password + random_number()

    return password

if __name__ == '__main__':
    while True:
        minimum_lenght = int(input('Minimum lenght: '))
        maximum_lenght = int(input('Maximum lenght: '))

        use_numbers = input('Use numbers(True/False): ')
        use_letters = input('Use letters(True/False): ')

        if use_numbers == 'True':
            use_numbers = True
        else:
            use_numbers = False

        if use_letters == 'True':
            use_letters = True
        else:
            use_letters == False

        password = create_password(lenght = (minimum_lenght, maximum_lenght), numbers = use_numbers,
                                   letters = use_letters)

        print(password)
