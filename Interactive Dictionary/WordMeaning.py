# Importing json and get_close_matches
import json
from difflib import get_close_matches

# Loading json to a python3 dictionary
data_dict = json.load(open('data.json'))


def translate(w):
    """
    This function finds the meaning of word given by user and suggest similar words if not typed correctly
    :param w: word
    :return: info
    """
    if w in data_dict:
        return data_dict[w]
    elif len(get_close_matches(w, data_dict.keys())) > 0:
        print("\nDo you mean...\n\t1. {suggestion_1}\n\t2. {suggestion_2}\n\t3. {suggestion_3}\ninstead?\n".format(
            suggestion_1=get_close_matches(w, data_dict.keys())[0],
            suggestion_2=get_close_matches(w, data_dict.keys())[1],
            suggestion_3=get_close_matches(w, data_dict.keys())[2],
        )
        )
        answer_1 = input("If Yes then enter 'Y' and if No then enter 'N': ")
        answer_1 = answer_1.upper()
        if answer_1 == 'Y':
            answer_2 = input("Enter the word number '1', '2' or '3': ")
            if answer_2 == 1:
                return data_dict[get_close_matches(w, data_dict.keys())[0]]
            elif answer_2 == 2:
                return data_dict[get_close_matches(w, data_dict.keys())[1]]
            else:
                return data_dict[get_close_matches(w, data_dict.keys())[2]]
        else:
            return "OOPS! Word doesn't exist in database. Please enter another word"
    else:
        return "OOPS! Word doesn't exist in database. Please enter another word"


def main():
    print('\n---------------------------- * Dictionary * -----------------------------\n'
          '------------- * Find meaning of any word with auto suggest * ------------\n')
    word = input(
        'Enter word: ')
    word = word.lower()
    translated = translate(word)
    if type(translated) == list:
        print('\n', word, ':\n')
        for meaning in translated:
            print("- ", meaning)
        layout()
    else:
        print(translated)
        layout()


def layout():
    start = input("\nEnter 'Q' to quit or any other key to continue: ")
    start = start.upper()
    if start == 'Q':
        exit(0)
    else:
        main()


layout()
