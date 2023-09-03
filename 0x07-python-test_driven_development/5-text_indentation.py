#!/usr/bin/python3
"""define function that handle text indentation."""


def text_indentation(text):
    """text_indentation function
        Args:
            @text: text to be handled
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    list_char = ["?", ".", ":"]
    line = ""
    for char in text:
        line += char
        if char in list_char:
            line = line.strip()
            print("{}\n".format(line))
            line = ""
    else:
        line = line.strip()
        print("{}".format(line), end="")
