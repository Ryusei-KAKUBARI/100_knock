#! usr/bin/env python
# _*_ cording utf-8 _*_

import random

def get_random(sentence):
    result = []

    for word in sentence.split():
        if len(word) <= 4:
            result.append(word)
        else:
            head = word[0]
            middle = list(word[1:-1])
            end = word[-1]
            random.shuffle(middle)

            result.append(head + "".join(middle) + end)
    return result

def main():
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    random_text = get_random(sentence)
    print(" ".join(random_text))

if __name__ == "__main__":
    main()
