import tkinter as tk


def get_cursor_pos():
    while True:
        yield root.winfo_pointerxy()

cursor_pos = get_cursor_pos()


def on_space_pressed(event):
    x,y = next(cursor_pos)
    print(x,y)
    if (x, y) == (0, 0):
        # this makes a Beep sound in the command prompt/terminal, but might not work if run from an IDE
        print('\a')


def on_e_pressed(event):
    root.destroy()

print("Press space to check mouse position. Press E to exit")

root = tk.Tk()
root.bind('<space>', on_space_pressed)
root.bind('<e>', on_e_pressed)
root.withdraw()
root.mainloop()





