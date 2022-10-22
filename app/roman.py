import re
from typing import Dict

SINGLE_DIGIT_ROMANS: Dict[str, int] = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def is_valid(roman: str) -> bool:
    return len(roman) > 0 and re.match(r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman) is not None


class Roman:
    @classmethod
    def convert(cls, roman: str) -> int:
        if is_valid(roman):
            if len(roman) == 1:
                return SINGLE_DIGIT_ROMANS[roman]
            else:
                first = cls.convert(roman[0])
                second = cls.convert(roman[1])
                rest = cls.convert(roman[1:])
                if first >= second:  # addition
                    return first + rest
                else:  # subtraction
                    return rest - first
        else:
            return -1
