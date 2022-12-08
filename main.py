
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
##Create employee.db file if it does not exist
engine = create_engine('sqlite:///employee.db', echo=True)
Base = declarative_base()


#Employee class which orders the employee by ID, Name, Job, Birthday
##Because of formatting restrictions, the Birthday field accepts anything as a string 
###TODO: Improve the input validation for the Birthday field to only accept valid date format
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    job = Column(String)
    birthday = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class App:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.label_name = Label(self.frame, text="Name")
        self.label_name.grid(row=0, column=0)
        self.entry_name = Entry(self.frame)
        self.entry_name.grid(row=0, column=1)

        self.label_job = Label(self.frame, text="Job")
        self.label_job.grid(row=1, column=0)
        self.entry_job = Entry(self.frame)
        self.entry_job.grid(row=1, column=1)

        self.label_birthday = Label(self.frame, text="Birthday")
        self.label_birthday.grid(row=2, column=0)
        self.entry_birthday = Entry(self.frame)
        self.entry_birthday.grid(row=2, column=1)

        self.button_save = Button(self.frame, text="Save", command=self.save)
        self.button_save.grid(row=3, column=0)
        self.button_show = Button(self.frame, text="Show", command=self.show)
        self.button_show.grid(row=3, column=1)

        self.tree = ttk.Treeview(self.frame, columns=("name", "job", "birthday"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("job", text="Job")
        self.tree.heading("birthday", text="Birthday")
        self.tree.column("#0", width=50)
        self.tree.column("name", width=100)
        self.tree.column("job", width=100)
        self.tree.column("birthday", width=100)
        self.tree.grid(row=4, column=0, columnspan=2)

    def save(self):
        name = self.entry_name.get()
        job = self.entry_job.get()
        birthday = self.entry_birthday.get()
        if name == "" or job == "" or birthday == "":
            messagebox.showwarning("Warning", "Please fill all the fields")
        else:
            employee = Employee(name=name, job=job, birthday=birthday)
            session.add(employee)
            session.commit()
            messagebox.showinfo("Success", "Data saved")
            self.entry_name.delete(0, END)
            self.entry_job.delete(0, END)
            self.entry_birthday.delete(0, END)

    def show(self):
        self.tree.delete(*self.tree.get_children())
        for employee in session.query(Employee).all():
            self.tree.insert("", "end", text=employee.id, values=(employee.name, employee.job, employee.birthday))

root = Tk()
app = App(root)
root.mainloop()