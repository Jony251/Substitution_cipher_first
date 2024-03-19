def input_user_str() -> str:
    """
    The function asking for input from user and checking it
    :return: tuple with no numbers
    """
    print(f'Hello, please enter your string for coding: ')
    c = 0
    while True:
        inp_user = input()
        res = ""
        num_s = ""
        for char in inp_user:
            if not char.isdigit():
                res += char
            else:
                num_s += char
        if res:
            return res
        else:
            if c < 5:
                print("Please enter a string with at least one non-digit character!")
            else:
                print("You seem to have trouble understanding! Please enter a valid string!")
            c += 1


def input_user_lang() -> str:
    """
    The function asking for input of language from user and checking if it's a right input
    :return: string with language
    """
    print('Please enter what language you choose, English or Russian: ')
    c = 0
    while True:
        try:
            inp_user = input().strip()
            if not inp_user:
                raise ValueError("Empty input, please try again.")
            if inp_user[0].lower() in ['r', 'р']:
                res = 'r'
                return res
            elif inp_user[0].lower() in ['e', 'а']:
                res = 'e'
                return res
            else:
                if c < 5:
                    print("Please choose either English or Russian!")
                else:
                    print("You seem to have trouble understanding! Please choose a language already!")
                c += 1
        except ValueError as e:
            print(e)


def input_user_code_key(lang) -> int:
    """
     The function asking for input of a key (number) from user and checking if it's number
    :param lang: a string for choosing language and prints with chose one
    :return: key (number) for continuation
    """
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
        # TODO: need to solve the problem with ValueError
        # TODO: checking of numbs between n&n


def looping_of_substitution_cipher(inp_str, loop) -> str:
    """
       The function is coding the inp_str depending on the loop_num
       :param inp_str: the input (tuple) from a user
       :param loop_num: key (int) of the coding
       :return: coded user string
       """
    loop_num = str_to_int(loop)
    alphabets = {
        'e': {
            'lower': 'abcdefghijklmnopqrstuvwxyz',
            'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        },
        'r': {
            'lower': "абвгдежзийклмнопрстуфхцчшщъыьэюя",
            'upper': "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        }
    }

    res = ""
    lang = 'e' if any(97 <= ord(c.lower()) <= 122 for c in inp_str) else 'r'
    alphabet = alphabets[lang]
    for char in inp_str:
        if char.islower() and char in alphabet['lower']:
            index = (alphabet['lower'].index(char) + loop_num) % len(alphabet['lower'])
            res += alphabet['lower'][index]
        elif char.isupper() and char in alphabet['upper']:
            index = (alphabet['upper'].index(char) + loop_num) % len(alphabet['upper'])
            res += alphabet['upper'][index]
        else:
            res += char
    return res


def str_to_int(str) -> int:
    try:
        return int(str)
    except Exception as e:
        print("Exception occurred:", e)


def encode_coded_str(user_input, key_in) -> str:
    """
    The function getting an input from user (coded string) & key for uncode it
    :param user_input: a user input (str)
    :param key: key for uncoding the user input
    :return: (str) uncoded user input
    """
    key = str_to_int(key_in)
    if 97 <= (ord(user_input[0].lower())) <= 122:
        in_lang = 'e'
    else:
        in_lang = 'r'
    return looping_of_substitution_cipher(user_input, (-key))


def encoding_of_substitution_cipher_using_loop_coding(inp_str) -> str:
    """
    The function gets input
    :param inp_str: string from the user input
    :return: codes every word of input string where is a key length of the current word
    """
    list_length_words = []
    ind = 0
    res = ""

    alphabets = {
        'e': {
            'lower': 'abcdefghijklmnopqrstuvwxyz',
            'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        },
        'r': {
            'lower': "абвгдежзийклмнопрстуфхцчшщъыьэюя",
            'upper': "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        }
    }

    lang = 'e' if any(97 <= ord(c.lower()) <= 122 for c in inp_str) else 'r'
    alphabet = alphabets[lang]

    for i in inp_str:
        if i.isalpha():
            ind += 1
        else:
            if ind != 0:
                list_length_words.append(ind)
                ind = 0
    list_length_words.append(ind)
    ind = 0
    for char in inp_str:
        current_word_length = list_length_words[ind]
        if current_word_length > 0 and char in alphabet['lower'] and char.isalpha:
            index = (alphabet['lower'].index(char) + list_length_words[ind]) % len(alphabet['lower'])
            res += alphabet['lower'][index]
        elif current_word_length > 0 and char.isalpha and char in alphabet['upper']:
            index = (alphabet['upper'].index(char) + list_length_words[ind]) % len(alphabet['upper'])
            res += alphabet['upper'][index]
        else:
            res += char
        if char == ' ':
            ind += 1
    return res
