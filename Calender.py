from tkinter import *
import calendar


def calendar_show():
    root = Tk()
    root.configure(background="White")
    root.title("Calendar")
    root.geometry("550x800")
    fetch_year = int(year_Field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(root, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    root.mainloop()


if __name__ == "__main__":
    new_root = Tk()
    new_root.configure(background="white")
    new_root.title("Calendar")
    new_root.geometry("160x150")

    cal = Label(new_root, text="Calendar", bg="dark grey", font=("times", 28, "bold"))
    year = Label(new_root, text="Enter Year", bg="light green")

    year_Field = Entry(new_root)

    Show = Button(new_root, text="Show Calendar", fg="Black", bg="Red", command=calendar_show)
    Exit = Button(new_root, text="Exit", fg="Black", bg="Red", command=exit)

    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)
    year_Field.grid(row=3, column=1)

    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)

    new_root.mainloop()
