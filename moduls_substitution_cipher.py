def input_user_str() -> str:
    print(f'Hello, please enter your string for codding: ')
    c = 0
    while True:
        inp_user = input()
        if inp_user.isalpha():
            return inp_user
        else:
            if c < 5:
                print("Do me a favor enter a string with no numbers!")
            else:
                print("What a ***&, what you didn't understood! Oooo boy enter a f*** string!")
            c += 1


def input_user_lang() -> str:
    print('Please enter what language you choose, English or Russian: ')
    c = 0
    while True:
        try:
            inp_user = input().strip()
            if not inp_user:
                raise ValueError("Empty input, please try again.")
            if inp_user[0].lower() in ['e', 'r', 'р', 'а']:
                return inp_user
            else:
                if c < 5:
                    print("Please choose either English or Russian!")
                else:
                    print("You seem to have trouble understanding! Please choose a language already!")
                c += 1
        except ValueError as e:
            print(e)


def input_user_code_key(lang) -> int:
    if lang[0].lower() in ['e', 'а']:
        print('Please enter your key code, it is a number between 0 to 26: ')
    elif lang[0].lower() in ['r', 'р']:
        print('Пожалуйста введите ключь кода, это цыфра от 0 до 33: ')
    while True:
        try:
            res_input = int(input())
            if not res_input:
                raise ValueError("Empty input, please try again.")
            return res_input
        except ValueError as e:
            print("Error:", e)
