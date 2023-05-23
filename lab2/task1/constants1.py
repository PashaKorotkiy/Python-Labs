# Path to files

TEXT_PARSE_PATH = "data/text_parse.txt"
TESTS = "tests/"

# Shortcuts

YES = "y"
NO = "n"

# Abbreviations

APPEAL_ABBREVIATIONS = (r"\bMr\.", r"\bMrs\.", r"Dr\.", r"St\.", r"Blvd\.", r"Ave\.", r"Sq\.", r"Rd\.", r"Bldg\.",
                        r"B\.Sc\.", r"M\.A\.", r"Ph\.D\.", r"M\.D\.", r"LT\.", r"Mx\.", r"Esq\.", r"Dr\.", r"KC\.",
                        r"Fr\.", r"Pr\.", r"Br\.", r"Sr\.", r"Ph\.D\.")

ABBREVIATIONS = (r"etc\.", r"Re\.", r"p\.", r"exp\.", r"err\.", r"et\.al\.", r"ex\.", r"e\.g\.", r"fin\.", r"i\.e\.",
                 r"vs\.", r"N\.B\.", r"P\.S\.", r"P\.P\.S\.", r"P\.S\.S\.", r"ft\.", r"oz\.", r"pt\.", r"in\.",
                 r"sec\.", r"\bg\.", r"cm\.", r"qt\.", r"p\.m\.")

# Regular expr

BEGINNING_OF_THE_SENTENCE = r"\s[A-Z]"
END_OF_THE_SENTENCE = r"\w[.!?]"
END_OF_NOT_DECLARATIVE_SENTENCE = r"\w[!?]"
NUMBERS = r"\b\d+e[+-]\d+|\b\d+[.,]?\d+|\b\d+"
ODD_CHARACTERS = r"[!.?\",']"
INITIALS = r"[A-Z]\. [A-Z]\. [A-Z]"
FILE_NAME = r"\w+\.\w+"
THREE_DOTS = r"\.\.\."
BEGINNING_OF_THE_DIRECT_SPEECH = r'\"[\w\d\s,\'!?.]*,\"'
DIFFERENT_BEGINNING_OF_THE_DIRECT_SPEECH = r'\"[\w\d\s,\'!?.]*[?!]\"\s[a-z]'
END_OF_THE_DIRECT_SPEECH = r', \"[\w\d\s,\'!?.]*[?!.]\"'
DIRECT_SPEECH = r'\"[\w\d\s,\'!?.]*[?!.]\"'

