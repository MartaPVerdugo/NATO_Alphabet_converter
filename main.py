import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dataframe = pandas.DataFrame(alphabet)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}
print(alphabet_dict)

user_word = input("Enter a word: ").upper()

user_list = [alphabet_dict[letter] for letter in user_word if letter in alphabet_dict.keys()]

print(user_list)
