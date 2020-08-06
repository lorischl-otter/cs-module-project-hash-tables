def word_count(s):

    # initialize dictionary
    d = {}

    # split words from string on whitespace
    words = s.split()

    # loop through words
    for w in words:
        # strip characters to ignore
        w = w.strip('":;,.-+=/\\|[]{}()*^&').lower()
        # pass on word if only ignored characters
        if w == "":
            continue
        # if word not already in dictionary, add to dict
        if w not in d:
            d[w] = 0
        # add 1 count to key in dict
        d[w] += 1

    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
