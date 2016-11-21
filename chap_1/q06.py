#! usr/bin/env python
# _*_ cording utf-8 _*_

def get_bi_gram(sentence, n=2):
    result = []
    for i in range(len(sentence)):
        bi_gram = sentence[i:i+n]
        if bi_gram not in result:
            result.append(bi_gram)
    print(result)
    return result

def main():
    sentence1 = "paraparaparadise"
    sentence2 = "paragraph"

    X = set(get_bi_gram(sentence1))
    Y = set(get_bi_gram(sentence2))

    print("Xの集合\n{}\n".format(X))
    print("Yの集合\n{}\n".format(Y))

    print("XとYの和集合\n{}\n".format(X|Y))
    print("XとYの積集合\n{}\n".format(X&Y))
    print("X-Yの差集合\n{}\n".format(X-Y))
    print("Y-Xの差集合\n{}\n".format(Y-X))

    print("以下の集合に\"se\"が含まれているか。")
    print("X:{}".format("se" in X))
    print("Y:{}".format("se" in Y))

if __name__ == "__main__":
    main()
