import math
import os


def read_dir(dirn):
    cont_l = []
    for fn in os.listdir(dirn):
        with open(os.path.join(dirn, fn), encoding="latin-1") as f:
            words = [w.strip()
                for w in f.read().replace("\n", " ").split(" ")
                    if not stopword(w)
            ]
            cont_l.append(words)
    return cont_l


def stopword(wstr):
    w = wstr.strip()
    if len(w) < 4:
        return True
    return False


def count_words(doc):
    count = 0
    dict = {}
    for letter in doc:
        for word in letter:
            count += 1
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return count, dict


def probability_of_word(word, dict, total):
    dict_word_count = len(dict)
    if word in dict:
        count = dict[word]
        return math.log((count + 1) / (total + dict_word_count))
    else:
        return 0


if __name__ == '__main__':
    ham_l = read_dir("enron6\\ham")
    spam_l = read_dir("enron6\\spam")

    ham_doc_count = len(ham_l)
    spam_doc_count = len(spam_l)
    total_doc_count = ham_doc_count + spam_doc_count

    p_ham = ham_doc_count / total_doc_count
    p_spam = spam_doc_count / total_doc_count

    ham_word_count, ham_dict = count_words(ham_l)
    spam_word_count, spam_dict = count_words(spam_l)

    V = set(ham_dict)  # all_spam_words: spam docs joined together
    V.update(spam_dict)

    # DATA FOR LETTERS
    letters = read_dir("letters")
    unique = set()

    for letter in letters:
        for word in letter:
            unique.add(word)

    fake_unique = unique.copy()
    for word in fake_unique:
        if word not in ham_dict or word not in spam_dict:
            unique.remove(word)

    # LETTER 1
    h_ham_1 = math.log(p_ham)
    h_spam_1 = math.log(p_spam)

    for word in letters[0]:
        h_ham_1 += probability_of_word(word, ham_dict, ham_word_count)

    for word in letters[0]:
        h_spam_1 += probability_of_word(word, spam_dict, spam_word_count)

    print(h_ham_1, h_spam_1)

    # LETTER 2
    h_ham_2 = math.log(p_ham)
    h_spam_2 = math.log(p_spam)

    for word in letters[1]:
        h_ham_2 += probability_of_word(word, ham_dict, ham_word_count)

    for word in letters[1]:
        h_spam_2 += probability_of_word(word, spam_dict, spam_word_count)

    print(h_ham_2, h_spam_2)
