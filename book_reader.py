import tkinter as tk
import os.path


def create_name_from_num(num):
    name = str(num)
    name = (3-len(name))*"0" + name + ".txt"
    return name


def get_file_names():
    more_files = True
    file_number = 1

    while more_files and file_number <= 999:
        file_name = create_name_from_num(file_number)
        if os.path.isfile(file_name):
            file_number += 1
            yield file_name
        else:
            more_files = False


def display_next_chapter():
    chapter_lines = next(chapters)
    chapter_text = "".join(chapter_lines)
    print(chapter_text)


def get_next_chapter():
    files = get_file_names()
    for file in files:
        chapter_lines = []
        try:
            with open(file) as current_file:
                for line in current_file:
                    if "#" in line and len(chapter_lines) > 0:
                        yield chapter_lines
                        chapter_lines = [line]
                    else:
                        chapter_lines.append(line)
                yield chapter_lines
        except IOError as e:
            print(e)

    while True:
        yield "Book Finished, press E to exit"


def on_space_pressed(event):
    display_next_chapter()


def on_e_pressed(event):
    root.destroy()

print("Press the Space key to start reading and to display the next chapter. Press E to exit\n")

chapters = get_next_chapter()
root = tk.Tk()
root.bind('<space>', on_space_pressed)
root.bind('<e>', on_e_pressed)
root.withdraw()
root.mainloop()
