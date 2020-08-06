def no_dups(s):
    # generate dictionary
    d = {}

    # split words by whitespace
    s = s.split()

    # iterate over words in list
    for w in s:
        # only add in words that are not in dict
        if w not in d:
            d[w] = 1

    final_string = ""

    for k, v in d.items():
        final_string += f"{k} "

    return final_string.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
