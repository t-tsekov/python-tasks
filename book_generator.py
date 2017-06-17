import random
import string
import os


def generate_word():
    alphabet = string.ascii_lowercase
    min_chars = 2
    max_chars = 14
    word = []
    for _ in range(random.randint(min_chars, max_chars)):
        char = random.choice(alphabet)
        word.append(char)

    return "".join(word)


def add_punctuation(word):
    num = random.randint(0, 18)
    if num == 0 or num == 1:
        word += "."
    if num == 2:
        word += ","

    return word


def generate_chapter(min_words, max_words):
    num_chapters = 1
    while True:
        words = ["# Chapter " + str(num_chapters) + "\n"]
        num_words = random.randint(min_words, max_words)
        should_capitalize = True

        for _ in range(num_words):
            new_word = add_punctuation(generate_word())
            if should_capitalize:
                new_word = new_word.capitalize()
            if new_word.endswith("."):
                should_capitalize = True
            else:
                should_capitalize = False
            words.append(new_word)

            # add random new lines if there isn't a comma:
            if not (new_word.endswith(",")):
                rand_num = random.randint(0, 20)
                if rand_num == 0:
                    words.append("\n")

        num_chapters += 1
        yield " ".join(words)


def get_file_name():
    for num in range(1, 1000):
        name = str(num)
        file_name = (3 - len(name)) * "0" + name + ".txt"
        if not os.path.isfile(file_name):
            return file_name
    raise Exception("All possible files with requested format already present")


def generate_book(num_chapters, min_words = 100, max_words = 200):
    chapters = generate_chapter(min_words = min_words, max_words = max_words)
    try:
        file_name = get_file_name()
    except Exception as e:
        print(e)
    for _ in range(num_chapters):
        chapter = next(chapters)

        try:
            with open(file_name, "a") as file:
                file.write(chapter)
                file.write("\n\n")
        except IOError as e:
            print(e)


if __name__ == "__main__":
    generate_book(7)
