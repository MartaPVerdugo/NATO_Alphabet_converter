import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dataframe = pandas.DataFrame(alphabet)
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}


def generate_nato():
    while True:
        try:
            user_word = input("Enter a word: ").upper()
            user_list = [alphabet_dict[letter] for letter in user_word]
        except KeyError:
            print("Sorry, you must enter a letter of the alphabet.")
        else:
            print(user_list)
            break


generate_nato()
