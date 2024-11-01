import datetime
import tkinter as tk

window = tk.Tk()
window.geometry("620x780")
window.title("Age Calculator App")


name_label = tk.Label(text="Name")
name_label.grid(column=0,row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0,row=3)

date_label = tk.Label(text="Day")
date_label.grid(column=0, row=4)


name_entry = tk.Entry()
name_entry.grid(column=1,row=1)

year_entry = tk.Entry()
year_entry.grid(column=1,row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=3)


date_entry = tk.Entry()
date_entry.grid(column=1, row=4)

def get_input():
    name = name_entry.get().strip()
    year = year_entry.get().strip()
    month = month_entry.get().strip()
    date = date_entry.get().strip()
    
    if not year or not month or not date:
        text_area = tk.Text(master=window, height=5, width=50)
        text_area.insert(tk.END,"Please fill in all field" )
        text_area.grid(column=0, row=6, columnspan=2)
        return
    
    try:
        birthdate = datetime.date(int(year), int(month), int(date))
        tiger = Person(name, birthdate)
        
        text_area = tk.Text(master=window, height=10, width=50)
        answer = "Hey {tiger} !!! You are {age} years old!!!".format(tiger=name, age=tiger.age())
        text_area.insert(tk.END, answer)
        text_area.grid(column=0, row=6, columnspan=2)
    except ValueError:
        text_area = tk.Text(master=window, height=5, width=50)
        text_area.insert(tk.END, "Please enter valid numeric values for year, month, and day.")
        text_area.grid(column=0, row=6, columnspan=2)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

button = tk.Button(window, text="Calculate Age", command=get_input, bg="white")
button.grid(column=1, row=5)

window.mainloop()

        