from task1.constants1 import TEXT_PARSE_PATH, YES, NO


def main_1():
    text = get_text()
    print(text)


def get_text():
    with open(TEXT_PARSE_PATH) as f:
        text = f.read()

    return text
