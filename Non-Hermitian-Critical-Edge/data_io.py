"""CSV loading and complete complex-number parsing for analysis scripts."""


def load_data(file_path):
    import pandas as pd
    with open(file_path, "r") as file:
        return pd.read_csv(file)


def parse_complex_string(value):
    """Parse a full real/complex literal, including scientific notation.

    Whitespace and one surrounding pair of parentheses are accepted, as in
    mpmath CSV strings. A final i is accepted as an alternative to j. Invalid
    trailing text raises ValueError rather than silently accepting a prefix.
    The result remains a Python complex value, as in the original reader.
    """
    text = "".join(str(value).split())
    if text.startswith("(") and text.endswith(")"):
        text = text[1:-1]
    if text.endswith(("i", "I")):
        text = text[:-1] + "j"
    try:
        return complex(text)
    except ValueError as error:
        raise ValueError("无法解析的复数字符串: {}".format(value)) from error
