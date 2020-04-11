from tkinter import *
from tkinter import messagebox

#Function for clearing box

def clear():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)

    ThisDayField.delete(0, END)
    ThisMonthField.delete(0, END)
    ThisYearField.delete(0, END)

    ResultDayField.delete(0, END)
    ResultMonthField.delete(0, END)
    ResultYearField.delete(0, END)

#Function for checking error

def error_check():
    if (dayField.get()==" " or monthField.get()==" " or yearField.get()==" " or ThisDayField.get()==" " or ThisMonthField.get()==" " or ThisYearField.get()==" "):
        messagebox.showerror("Invalid Input")
        clear()
        return -1

#Calculate age

def calculate():
    value=error_check()
    if value == -1:
        return
    else:
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())
        #name = nameField.get()

        this_day = int(ThisDayField.get())
        this_month = int(ThisMonthField.get())
        this_year = int(ThisYearField.get())

        month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Given day or month can be smaller than birth day or month. To subtract easily we perform the below to condition.
        if (birth_day > this_day):
            this_month = this_month -1
            this_day = this_day+month[birth_month-1]

        if (birth_month>this_month):
            this_year=this_year-1
            this_month=this_month+12

            calculated_day = this_day - birth_day;
            calculated_month = this_month - birth_month;
            calculated_year = this_year - birth_year;

            ResultDayField.insert(10, str(calculated_day))
            ResultMonthField.insert(10, str(calculated_month))
            ResultYearField.insert(10, str(calculated_year))



#Tkinter


if __name__ == "__main__" :
    root = Tk()
    root.configure(background="pink")
    root.title("Age Calculator")
    root.geometry("525x260")

    dob = Label(root, text= "Date of Birth", bg="White")
    todays_date = Label(root, text="Today", bg="White")

    day = Label(root, text= "Day", bg="orange")
    month = Label(root, text="Month", bg="orange")
    year = Label(root, text="Year", bg="orange")

    ThisDay = Label(root, text="Day", bg="orange")
    ThisMonth = Label(root, text="Month", bg="orange")
    ThisYear = Label(root, text="Year", bg="orange")

    resultAge = Button(root, text="See Result",fg="Black", bg="Yellow", command=calculate)

    ResultYear = Label(root, text="Years", bg="orange")
    ResultMonth = Label(root, text="Months", bg="orange")
    ResultDay = Label(root, text="Days", bg="orange")

    #name=Label(root,text="name", bg="orange")

    clear = Button(root, text="Clear All", fg="Red", bg="black", command=clear)


    dayField = Entry(root)
    monthField = Entry(root)
    yearField = Entry(root)

    ThisDayField = Entry(root)
    ThisMonthField = Entry(root)
    ThisYearField = Entry(root)

    ResultYearField = Entry(root)
    ResultMonthField = Entry(root)
    ResultDayField = Entry(root)

    #nameField = Entry(root)


#Grid

    dob.grid(row=0, column=1)

    day.grid(row=1, column=0)
    dayField.grid(row=1, column=1)

    month.grid(row=2, column=0)
    monthField.grid(row=2, column=1)

    year.grid(row=3, column=0)
    yearField.grid(row=3, column=1)



    todays_date.grid(row=0, column=4)

    ThisDay.grid(row=1, column=3)
    ThisDayField.grid(row=1, column=4)

    ThisMonth.grid(row=2, column=3)
    ThisMonthField.grid(row=2, column=4)

    ThisYear.grid(row=3, column=3)
    ThisYearField.grid(row=3, column=4)



    resultAge.grid(row=4, column=2)

    ResultYear.grid(row=5, column=2)
    ResultYearField.grid(row=6, column=2)

    ResultMonth.grid(row=7, column=2)
    ResultMonthField.grid(row=8, column=2)

    ResultDay.grid(row=9, column=2)
    ResultDayField.grid(row=10, column=2)

    #name.grid(row=15, column=2)
    #nameField.grid(row=17, column=2)

    clear.grid(row=12, column=2)

    root.mainloop()