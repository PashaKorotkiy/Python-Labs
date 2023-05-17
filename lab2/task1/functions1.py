import re
from task1.constants1 import APPEAL_ABBREVIATIONS, ABBREVIATIONS, BEGINNING_OF_THE_SENTENCE, END_OF_THE_SENTENCE, \
                            END_OF_NOT_DECLARATIVE_SENTENCE, NUMBERS, ODD_CHARACTERS, FILE_NAME, INITIALS, THREE_DOTS, \
                            BEGINNING_OF_THE_DIRECT_SPEECH, DIFFERENT_BEGINNING_OF_THE_DIRECT_SPEECH, \
                            END_OF_THE_DIRECT_SPEECH, DIRECT_SPEECH


def simplify_text(text):
    substring = text

    for abbreviation in APPEAL_ABBREVIATIONS:
        substring = re.sub(abbreviation, " ", substring)

    substring = re.sub(FILE_NAME, " ", substring)

    substring = re.sub(THREE_DOTS, " ", substring)

    substring = re.sub(DIFFERENT_BEGINNING_OF_THE_DIRECT_SPEECH, "A,", substring)

    substring = re.sub(END_OF_THE_DIRECT_SPEECH, ".", substring)

    substring = re.sub(BEGINNING_OF_THE_DIRECT_SPEECH, "A,", substring)

    substring = re.sub(DIRECT_SPEECH, "A.", substring)

    substring = re.sub(INITIALS, " ", substring)

    for abbreviation in ABBREVIATIONS:
        substring = re.sub(abbreviation + BEGINNING_OF_THE_SENTENCE, ". ", substring)
        substring = re.sub(abbreviation, " ", substring)

    return substring


def sentences_amount(text):
    return len(re.findall(END_OF_THE_SENTENCE, simplify_text(text)))


def not_declarative_sentences_amount(text):
    return len(re.findall(END_OF_NOT_DECLARATIVE_SENTENCE, simplify_text(text)))


def average_sentence_length(text):
    words_length = 0
    s_amount = sentences_amount(text)

    if not s_amount:
        return 0

    for word in split_into_words(text):
        words_length += len(word)

    return round(words_length / s_amount)


def split_into_words(text):

    string = re.sub(NUMBERS, " ", text)
    string = re.sub(ODD_CHARACTERS, " ", string)
    string = re.sub(":", " ", string)

    return string.split()


def average_word_length(text):
    all_words = split_into_words(text)

    if not len(all_words):
        return 0

    words_length = 0

    for word in all_words:
        words_length += len(word)

    return round(words_length / len(all_words))


def n_grams(text, n, k):

    no_arg_text = text.lower()
    words = split_into_words(no_arg_text)
    ngrams = dict()

    for i in range(len(words) - (n - 1)):
        ngram = " ".join(words[i: i + n])

        if ngram in ngrams:
            ngrams[ngram] += 1
        else:
            ngrams[ngram] = 1

    return sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:k]
