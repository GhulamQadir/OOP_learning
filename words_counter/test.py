from frequency_counter import WordCounter


def test():
    wc1 = WordCounter(
        "        apple mango orange apple banana papaya pomegranate guava banana           "
    )

    # Count occurrences of words in the input text
    frequency = wc1.words_frequency
    print(frequency)

    # Test __getitem__: directly access frequency of a specific word
    print(wc1["banana"])

    # Test __len__: get total number of unique words
    print(len(wc1))

    # Iterating over the object will call __iter__ and __next__ internally
    # Each iteration should yield a {word: frequency} dictionary
    for i in wc1:
        print(i)

    # Access cleaned input text using property
    print(wc1.input_text)

    # Access frequency dictionary directly
    print(wc1.words_frequency)

    # Update input text (this will clear old frequencies and keys automatically)
    wc1.input_text = "   red   blue   red   green   blue"

    # Recount word occurrences for new input
    occurences = wc1.words_frequency
    print(occurences)


if __name__ == "__main__":
    test()
