import moduls_substitution_cipher


def test_input_user_str():
    """
    :return: print the string that it's get
    """
    print(moduls_substitution_cipher.input_user_str())


def test_input_user_lang():
    """
    :return: prints the language
    """
    print(moduls_substitution_cipher.input_user_lang())


def test_input_user_code_key():
    """
    :return: prints the texts of a key bey the langauge
    """
    print(moduls_substitution_cipher.input_user_code_key('e'))
    print(moduls_substitution_cipher.input_user_code_key('Eeqweqe'))
    print(moduls_substitution_cipher.input_user_code_key("rRR"))
    print(moduls_substitution_cipher.input_user_code_key("Rsdadas"))


def test_looping_of_substitution_cipher():
    """
    :return: test looping_of_substitution_cipher coding by key and language
    """
    print(moduls_substitution_cipher.looping_of_substitution_cipher("Блажен, кто верует,123 тепло ему на свете!", 10,
                                                                    "r"))
    print(moduls_substitution_cipher.looping_of_substitution_cipher("To be, or not to be, that is the question!", 17,
                                                                    "e"))


def test_encode_coded_str():
    print(moduls_substitution_cipher.encode_coded_str("Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.", 7))
    print(
        moduls_substitution_cipher.encode_coded_str("Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.", 25))
    for i in range(1, 26):
        print(moduls_substitution_cipher.encode_coded_str("Hawnj pk swhg xabkna ukq nqj.", i))


def test_encoding_of_substitution_cipher_using_loop_coding():
    print(moduls_substitution_cipher.encoding_of_substitution_cipher_using_loop_coding(
        "Day, mice. \"Year\" is a mistake!"))
    print("Gdb, qmgi. \"Ciev\" ku b tpzahrl!")
    print(moduls_substitution_cipher.encoding_of_substitution_cipher_using_loop_coding(
        "To be, or not to be, that is the question"))
    print("Vq dg, qt qrw vq dg, xlex ku wkh ycmabqwv")
