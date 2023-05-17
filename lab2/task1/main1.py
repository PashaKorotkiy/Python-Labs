from task1.constants1 import TEXT_PARSE_PATH, YES, NO

from task1.functions1 import sentences_amount, not_declarative_sentences_amount, \
    average_sentence_length, average_word_length, n_grams


def main_1():

    text = get_text()
    print(text)

    sentences_amount2(text)

    not_declarative_sentences_amount2(text)

    average_sentence_length2(text)

    average_word_length2(text)

    ngrams(text)


def get_text():
    with open(TEXT_PARSE_PATH) as f:
        text = f.read()

    return text


def sentences_amount2(text):
    print(f"{sentences_amount(text)} - amount of sentences in the text")


def not_declarative_sentences_amount2(text):
    print(f"{not_declarative_sentences_amount(text)} - amount of non-declarative sentences in the text ")


def average_sentence_length2(text):
    print(f"{average_sentence_length(text)} - average length of the sentence in characters. Counts only words")


def average_word_length2(text):
    print(f"{average_word_length(text)} - average length of the word in the text in characters")


def ngrams(text):

    while True:
        inp = input(f"Do you want to enter N and K? ({YES}/{NO})\n")

        print(type(inp))
        print(type(YES))
        print(inp != YES)

        if inp != YES and inp != NO:
            print("Incorrect input. Please, try again\n")
        elif inp == YES:
            N = input_N()
            K = input_K()
            break
        else:
            N = 4
            K = 10
            break

    n_grams_list = n_grams(text, N, K)

    if len(n_grams_list) < K:
        print("K is bigger, then amount of  N-grams\n")

    print(f"top-{K} repeated {N}-grams in the text:")

    for n_gram in n_grams_list:
        print(n_gram)


def input_N():
    while True:
        try:
            N = int(input(f'Enter N: '))
        except ValueError:
            print(f"Wrong Input.\n")
        else:
            if N <= 0:
                print(f"N must be an positive integer.\n")
            else:
                return N


def input_K():
    while True:
        try:
            K = int(input(f'Enter K: '))
        except ValueError:
            print(f"Wrong input.\n")
        else:
            if K <= 0:
                print(f"K must be an positive integer.\n")
            else:
                return K

