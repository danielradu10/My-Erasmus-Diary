import datetime
import os
import random

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk
)

import tkinter as tkinter
from tkinter import *
from tkinter import ttk

from DataBaseManager import DataBaseManager
from BooksManager import BooksManager
from DataBaseManager import Verse
from BooksManager import Book
from LogIn import LogIn
from WebScraper import WebScraper


luni = {
    "1":"Ianuarie",
    "2":"Februarie",
    "3":"Martie",
    "4":"Aprilie",
    "5":"Mai",
    "6":"Iunie",
    "7":"Iulie",
    "8":"August",
    "9":"Septembrie",
    "10":"Octombrie",
    "11":"Noiembrie",
    "12":"Decembrie"
}





class MyRoot(tkinter.Tk):

    def __init__(self, logIn: LogIn, dataBase: DataBaseManager):
        super().__init__()
        print("Incepem jurnalul")

        self.logIn = logIn
        self.dataBase = 0


        self.frame = tkinter.Frame(self, width=600, height=650)
        self.frame.pack()

        self.frame2 = Frame2(self.logIn, self, dataBase)




        # container pentru alte widget

        self.project_name1 = ttk.Label(master=self.frame, text="Daniel's Daily Activity", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=155, y=0)


        self.username_label = ttk.Label(master=self.frame, text="Bine ai venit!\nIntrodu username:",
                                   font=("Times New Roman", 12))
        self.username_label.place(x=20, y=100)

        self.username_text = tkinter.StringVar()

        self.submitted = False

        self.username_box = ttk.Entry(master=self.frame, textvariable=self.username_text)
        self.username_box.place(x=20, y=160)



        self.submit_button = ttk.Button(master=self.frame, text="Submit",
                                   command=lambda: self.logIn.get_the_username(self.username_text, self.frame, self.frame2))
        self.submit_button.place(x=100, y=185)

        self.button = ttk.Button(master=self.frame, text="Quit", command=self.destroy)
        self.button.place(x=500, y=600)






class Frame2(tkinter.Frame):

    def __init__(self, logIn, root, dataBase):
        super().__init__(width=600, height=650)

        self.frame3 = Frame3(root, dataBase)

        self.logIn = logIn
        self.project_name1 = ttk.Label(master=self, text="Daniel's Daily Activity", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=155, y=0)

        self.username_label = ttk.Label(master=self, text="Bine ai venit, Daniel!\nIntrodu parola, pentru a fi siguri ca esti tu:",
                                        font=("Times New Roman", 12))
        self.username_label.place(x=20, y=100)

        self.username_text = tkinter.StringVar()
        self.submitted = False

        self.username_box = ttk.Entry(master=self, textvariable=self.username_text)
        self.username_box.place(x=20, y=160)

        self.submit_button = ttk.Button(master=self, text="Submit",
                                        command=lambda: self.logIn.get_the_pass(self.username_text, self,
                                                                                    self.frame3))
        self.submit_button.place(x=100, y=185)

        self.button = ttk.Button(master=self, text="Quit", command=self.destroy)
        self.button.place(x=500, y=600)

class Frame3(tkinter.Frame):
    def __init__(self, root: tkinter.Tk, database: DataBaseManager):
        super().__init__(width=600, height=650)

        self.root = root
        self.faithFrame = FaithfFrame(database, self)
        self.programmingFrame = ProgrammingFrame(self)
        self.project_name1 = ttk.Label(master=self, text="Daniel's Daily Activity", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=155, y=0)

        self.menu = Menu(root)
        self.root.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=False)


    def new_day(self):

        self.faith_button = Button(self, text="Faith", command=lambda : self.faith())
        self.faith_button.place(x=100, y=150)

        self.programming_button = Button(self, text="Programming", command=self.programming)
        self.programming_button.place(x=250, y=150)

        self.business = Button(self, text="Business")
        self.business.place(x=450, y=150)

        self.sport = Button(self, text="Sport")
        self.sport.place(x=175, y=250)

        self.reading = Button(self, text = "Books", command=self.books)
        self.reading.place(x=375, y=250)

    def add_menu(self):
        self.file_menu.add_command(label='New day', command=self.new_day)
        self.file_menu.add_command(label='Modify an old day')
        self.file_menu.add_command(label='Save the day')

        self.menu.add_cascade(label="File", menu=self.file_menu, underline=0)

    def faith(self):
        self.faithFrame.pack()
        self.pack_forget()

    def programming(self):
        self.programmingFrame.pack()
        self.pack_forget()

    def books(self):
        self.pack_forget()
        self.books = BooksFrame()
        self.books.pack()




class FaithfFrame(tkinter.Frame):
    def __init__(self, database, backframe):
        super().__init__(width=600, height=650)

        self.backframe = backframe
        self.database = database

        self.categories = []

        self.choose_frame = ChooseFrame(database, self)

        self.project_name1 = ttk.Label(master=self, text="Faith", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=250, y=0)

        self.choose_button = tkinter.Button(master=self, text="Choose", command=self.choose, width=30)
        self.choose_button.place(x=200, y=140)


        self.date = ttk.Label(master=self, text=str(datetime.datetime.now().date()), font=("Arial", 20))
        self.date.config(foreground="grey")
        self.date.place(x=220, y=50)

        self.project_name2 = ttk.Label(master=self, text="Daniel, ai nevoie de un verset astazi?", font=("Arial", 16))
        self.project_name2.config(foreground="Black")
        self.project_name2.place(x=150, y=100)

        self.label = ttk.Label(master=self, text="Ce verset ai remarcat astazi?",
                                        font=("Times New Roman", 12))
        self.label.place(x=40, y=200)

        self.verse_text = StringVar()
        self.verse = ttk.Entry(self, textvariable=self.verse_text, width=30)
        self.verse.place(x=40, y=220)

        self.label2 =  ttk.Label(master=self, text="De unde este acest verset?",
                                        font=("Times New Roman", 12))
        self.label2.place(x=40, y=240)

        self.author_text = StringVar()
        self.author = ttk.Entry(self, textvariable=self.author_text, width=30)
        self.author.place(x=40, y=260)

        self.label3 = ttk.Label(master=self, text="Din ce capitol?",
                                font=("Times New Roman", 12))
        self.label3.place(x=360, y=200)

        self.chapter_text = StringVar()
        self.chapter = ttk.Entry(self, textvariable=self.chapter_text, width=30)
        self.chapter.place(x=360, y=220)

        self.label4 = ttk.Label(master=self, text="Care versete?",
                                font=("Times New Roman", 12))
        self.label4.place(x=360, y=240)

        self.number_text = StringVar()
        self.number = ttk.Entry(self, textvariable=self.number_text, width=30)
        self.number.place(x=360, y=260)

        self.label5 = ttk.Label(master=self, text="Categoria:",
                                font=("Times New Roman", 12))
        self.label5.place(x=240, y=290)

        self.credinta_var = tkinter.BooleanVar()
        self.dragoste_var = tkinter.BooleanVar()
        self.putere_var = tkinter.BooleanVar()
        self.fericire_var = tkinter.BooleanVar()
        self.mandrie_var = tkinter.BooleanVar()
        self.perioada_var = tkinter.BooleanVar()



        self.credinta =ttk.Checkbutton(self, text="Credinta", variable=self.credinta_var, onvalue=tkinter.TRUE, offvalue=False)
        self.credinta.place(x=60, y=320)

        self.dragoste = ttk.Checkbutton(self, text="Dragoste",  variable=self.dragoste_var, onvalue=tkinter.TRUE, offvalue=tkinter.FALSE)
        self.dragoste.place(x=140, y=320)

        self.putere = ttk.Checkbutton(self, text="Putere",  variable=self.putere_var, onvalue=tkinter.TRUE, offvalue=tkinter.FALSE)
        self.putere.place(x=220, y=320)

        self.fericire = ttk.Checkbutton(self, text="Fericire", variable=self.fericire_var, onvalue=tkinter.TRUE, offvalue=tkinter.FALSE)
        self.fericire.place(x=300, y=320)

        self.perioada_grea = ttk.Checkbutton(self, text="Perioada grea",  variable=self.perioada_var, onvalue=tkinter.TRUE, offvalue=tkinter.FALSE)
        self.perioada_grea.place(x=380, y=320)

        self.mandrie = ttk.Checkbutton(self, text="Mandrie",  variable=self.mandrie_var, onvalue=tkinter.TRUE, offvalue=tkinter.FALSE)
        self.mandrie.place(x=500, y=320)

        self.submit_verse = Button(self, text = "Add new verse ",command=self.submit_verse_command)
        self.submit_verse.place(x=450, y=360)



        self.rezumat_box = tkinter.Text(self, height=10, width=50)
        self.rezumat_box.place(x=100, y=430)



        self.submit_rezumat = tkinter.Button(self, text="Submit Ideas", command=self.submit_rezumat_command)
        self.submit_rezumat.place(x=450, y=610)

        self.back = Button(self, text="Back", command=self.goback)
        self.back.place(x=20, y=610)

    def goback(self):
        self.forget()
        self.backframe.pack()


    def submit_verse_command(self):

        self.categories = []

        print(self.verse_text.get())
        print(self.chapter_text.get())
        print(self.author_text.get())
        print(self.number_text.get())

        if(self.mandrie_var.get()):
            self.categories.append("Mandrie")
        if(self.fericire_var.get()):
            self.categories.append("Fericire")
        if(self.credinta_var.get()):
            self.categories.append("Credinta")
        if(self.putere_var.get()):
            self.categories.append("Putere")
        if(self.dragoste_var.get()):
            self.categories.append("Dragoste")
        if(self.perioada_var.get()):
            self.categories.append("Perioada Grea")


        categorii = ' '.join(self.categories)

        print("Categorii: " + categorii)

        verse = Verse(None, self.verse_text.get(), self.author_text.get(), self.chapter_text.get(), self.number_text.get(), categorii, str(datetime.datetime.now().date()))


        self.database.insert(verse)

        print(verse)

    def submit_rezumat_command(self):
        print(self.rezumat_box.get("1.0", "end-1c"))


        parent_dir = "D:\JustMeDoinThings\desktopMyActivity\Activitate"


        day_path = os.path.join(parent_dir, str(datetime.datetime.now().date()))
        print(day_path)
        if(os.path.exists(day_path)):
            print("Pathul deja exista")
            os.chdir(day_path)
            faith_file = open("Faith", "a")
            faith_file.write(self.rezumat_box.get("1.0", "end-1c"))
        else:
            print("Pathul nu exista")
            os.mkdir(day_path)
            os.chdir(day_path)
            faith_file = open("Faith", "a")
            faith_file.write(self.rezumat_box.get("1.0", "end-1c"))

    def choose(self):
        self.choose_frame.pack()
        self.pack_forget()





class ChooseFrame(tkinter.Frame):
    def __init__(self, database, frame):
        super().__init__(width=600, height=400)


        self.siguranta = 0
        self.backframe = frame

        self.project_name1 = ttk.Label(master=self, text="Faith", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=250, y=0)

        self.date = ttk.Label(master=self, text=str(datetime.datetime.now().date()), font=("Arial", 20))
        self.date.config(foreground="grey")
        self.date.place(x=220, y=50)

        self.database = database
        self.webScraper = WebScraper()

        self.generateweb = Button(self, text="Generate from Web", command=self.generate_command)
        self.generateweb.place(x=100, y=200)

        self.generateweb = Button(self, text="Generate from Saved", command=self.generate_from_saved)
        self.generateweb.place(x=400, y=200)

        self.credinta_var = tkinter.BooleanVar()
        self.dragoste_var = tkinter.BooleanVar()
        self.putere_var = tkinter.BooleanVar()
        self.fericire_var = tkinter.BooleanVar()
        self.mandrie_var = tkinter.BooleanVar()
        self.perioada_var = tkinter.BooleanVar()

        self.credinta = ttk.Checkbutton(self, text="Credinta", variable=self.credinta_var, onvalue=tkinter.TRUE,
                                        offvalue=False)
        self.credinta.place(x=60, y=120)

        self.dragoste = ttk.Checkbutton(self, text="Dragoste", variable=self.dragoste_var, onvalue=tkinter.TRUE,
                                        offvalue=tkinter.FALSE)
        self.dragoste.place(x=140, y=120)

        self.putere = ttk.Checkbutton(self, text="Putere", variable=self.putere_var, onvalue=tkinter.TRUE,
                                      offvalue=tkinter.FALSE)
        self.putere.place(x=220, y=120)

        self.fericire = ttk.Checkbutton(self, text="Fericire", variable=self.fericire_var, onvalue=tkinter.TRUE,
                                        offvalue=tkinter.FALSE)
        self.fericire.place(x=300, y=120)

        self.perioada_grea = ttk.Checkbutton(self, text="Perioada grea", variable=self.perioada_var,
                                             onvalue=tkinter.TRUE, offvalue=tkinter.FALSE)
        self.perioada_grea.place(x=380, y=120)

        self.mandrie = ttk.Checkbutton(self, text="Mandrie", variable=self.mandrie_var, onvalue=tkinter.TRUE,
                                       offvalue=tkinter.FALSE)
        self.mandrie.place(x=500, y=120)


        self.versettext = StringVar()
        self.versettext.set("Versetul")
        self.verset = tkinter.Label(self, textvariable=self.versettext, font=("Arial", 10),wraplength=200)
        self.verset.place(x=30, y=270)

        self.verset_numar_text = StringVar()
        self.verset_numar_text.set("Versetul")
        self.verset_numar = tkinter.Label(self, textvariable=self.verset_numar_text, font=("Arial", 10),wraplength=500)
        self.verset_numar.place(x=30, y=290)

        self.back = Button(self, text="Back", command=self.goback)
        self.back.place(x=20, y=330)
    def generate_command(self):

        self.siguranta = self.siguranta + 1


        self.categories  = ""
        if (self.mandrie_var.get()):
            self.categories = "mandrie"
        if (self.fericire_var.get()):
            self.categories = "fericire"
        if (self.credinta_var.get()):
            self.categories = "credinta"
        if (self.putere_var.get()):
            self.categories = "putere"
        if (self.dragoste_var.get()):
            self.categories = "dragoste"
        if (self.perioada_var.get()):
            self.categories = "perioada grea"

        rez = self.webScraper.generate_verse(self.categories)
        self.versettext.set(rez[1])
        self.verset_numar_text.set(rez[0])



    def generate_from_saved(self):
        self.categories = ""
        if (self.mandrie_var.get()):
            self.categories = "Mandrie"
        if (self.fericire_var.get()):
            self.categories = "Fericire"
        if (self.credinta_var.get()):
            self.categories = "Credinta"
        if (self.putere_var.get()):
            self.categories = "Putere"
        if (self.dragoste_var.get()):
            self.categories = "Dragoste"
        if (self.perioada_var.get()):
            self.categories = "Perioada Grea"

        verses = self.database.select_by_category(self.categories)
        numar = random.randint(0, len(verses)-1)
        verset = verses[numar].author + "\n" + verses[numar].chapter + ":" + verses[numar].verse
        verset_text = verses[numar].verse
        print(verset)
        print(verset_text)

    def goback(self):
        self.forget()
        self.backframe.pack()



class ProgrammingFrame(tkinter.Frame):
    def __init__(self, frame):
        super().__init__(width=600, height=450)
        self.backframe = frame


        self.back = Button(self, text="Back", command=self.goback)
        self.back.place(x=20, y=400)

        self.project_name1 = ttk.Label(master=self, text="Programming", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=190, y=0)

        self.date = ttk.Label(master=self, text=str(datetime.datetime.now().date()), font=("Arial", 20))
        self.date.config(foreground="grey")
        self.date.place(x=220, y=50)

        self.label = ttk.Label(master=self, text="Cate ore ai reusit sa lucrezi astazi?",
                               font=("Times New Roman", 12))
        self.label.place(x=40, y=100)

        self.ore_text = StringVar()
        self.ore = ttk.Entry(self, textvariable=self.ore_text, width=30)
        self.ore.place(x=40, y=120)

        self.graph = Button(self, text="See Progress", command=self.generate_progress)
        self.graph.place(x=40, y=150)

        self.label2 = ttk.Label(master=self, text="Ce ai invatat astazi?",
                               font=("Times New Roman", 12))
        self.label2.place(x=230, y=200)

        self.rezumat_box = tkinter.Text(self, height=10, width=50)
        self.rezumat_box.place(x=100, y=230)

        self.submit_rezumat = tkinter.Button(self, text="Submit Ideas", command=self.submit_rezumat_command)
        self.submit_rezumat.place(x=450, y=410)


    def generate_progress(self):
        self.forget()
        self.graphframe = GraphFrame(self, self.ore_text.get())
        self.graphframe.pack()


    def goback(self):
        self.forget()
        self.backframe.pack()

    def submit_rezumat_command(self):
        print(self.rezumat_box.get("1.0", "end-1c"))

        parent_dir = "D:\JustMeDoinThings\desktopMyActivity\Activitate"

        day_path = os.path.join(parent_dir, str(datetime.datetime.now().date()))
        print(day_path)
        if (os.path.exists(day_path)):
            print("Pathul deja exista")
            os.chdir(day_path)
            faith_file = open("Programming", "a")
            faith_file.write(self.rezumat_box.get("1.0", "end-1c"))
        else:
            print("Pathul nu exista")
            os.mkdir(day_path)
            os.chdir(day_path)
            faith_file = open("Programming", "a")
            faith_file.write(self.rezumat_box.get("1.0", "end-1c"))

class GraphFrame(tkinter.Frame):

    def __init__(self, backframe, oretext):
        super().__init__(width=600, height=450)
        self.backframe = backframe
        self.back = Button(self, text="Back", command=self.goback)
        self.back.place(x=20, y=420)

        self.oretext = oretext

        file1 = open("ore.txt", 'a')
        file1.write(", " + self.oretext)
        file1.close()
        file1 = open("ore.txt", 'r')
        hours = []

        print(hours)
        for number in file1.read().split(", "):
            if (number != ''):
                print(number)
                hours.append(float(number))

        used_hours = hours[len(hours) - 7:len(hours)]
        print(used_hours)

        file2 = open("zile.txt", 'a')
        file2.write(", " + str(datetime.datetime.now().date()))
        file2.close()

        file2 = open("zile.txt", 'r')
        days = file2.read().split(", ")
        used_days = days[len(days) - 7:len(days)]
        print(used_days)

        figure = Figure(figsize=(7, 5), dpi=70)
        figure_canvas = FigureCanvasTkAgg(figure, self)

        axes = figure.add_subplot()
        axes.bar(used_days, hours)
        axes.set_title('Productivitate')
        axes.set_xlabel('Zile')
        axes.set_ylabel('Ore')
        figure_canvas.get_tk_widget().place(x=55, y=50)



    def goback(self):
        self.forget()
        self.backframe.pack()


class BooksFrame(tkinter.Frame):
    def __init__(self):
        super().__init__(width=600, height=450)
        self.project_name1 = ttk.Label(master=self, text="Books", font=("Arial", 25))
        self.project_name1.config(foreground="grey")
        self.project_name1.place(x=190, y=0)

        self.date = ttk.Label(master=self, text=str(datetime.datetime.now().date()), font=("Arial", 20))
        self.date.config(foreground="grey")
        self.date.place(x=220, y=50)

        self.booksmanager = BooksManager()

        self.luna = datetime.datetime.now().date().month
        print(self.luna)

        the_monthly_book = self.booksmanager.select_by_luna(luni[str(self.luna)])
        print(the_monthly_book)
        if(len(the_monthly_book) == 0):
            print("Nu ai carte pentru august")
            self.label = ttk.Label(master=self, text="Nu ai nici un target pentru " + luni[str(self.luna)] + "! Ce carte iti propui sa citesti luna aceasta?",
                                   font=("Times New Roman", 12), wraplength=230)
            self.label.place(x=40, y=100)

            self.nume_carte = StringVar()
            self.nume = ttk.Entry(self, textvariable=self.nume_carte, width=40)
            self.nume.place(x=40, y=160)

            self.authortext = StringVar()
            self.label2 = ttk.Label(master=self, text="Introdu autorul!",
                                   font=("Times New Roman", 12), wraplength=230)
            self.label2.place(x=400, y=130)

            self.author = ttk.Entry(self, textvariable=self.authortext, width=30)
            self.author.place(x=400, y=160)

            self.label3 =  ttk.Label(master=self, text="Cate pagini are?",
                                   font=("Times New Roman", 12), wraplength=230)
            self.label3.place(x=40, y=190)

            self.paginitext = StringVar()
            self.pagini = ttk.Entry(self, textvariable=self.paginitext, width=30)
            self.pagini.place(x=40, y=220)

            self.button = Button(self, text="Submit New Target", command=self.submitbook)
            self.button.place(x=400, y=220)

        else:
            target_curent = the_monthly_book[0].nume
            pagini_citite = the_monthly_book[0].pagina
            zi = datetime.datetime.now().date().day
            medie_per_zi = pagini_citite/zi

            print(medie_per_zi)

            self.label = ttk.Label(master=self, text="Iata targetul din aceasta luna: \""  +
                                                     target_curent + "\" de " + the_monthly_book[0].author + "!"+
                                                     "\nAi citit in medie " + str(medie_per_zi) + " pagini pe zi!\n"+
                                                     "Ieri erai la pagina: " + str(pagini_citite) + " din " + str(the_monthly_book[0].total_pagini) +"\n"+
                                                      "La ce pagina ai ajuns astazi?",
                                   font=("Times New Roman", 12))
            self.label.place(x=40, y=100)





    def submitbook(self):
        nume = self.nume.get()
        autor = self.author.get()
        pagini = int (self.pagini.get())
        self.booksmanager.insert(Book(None, nume, autor, 62, pagini, luni[str(self.luna)]))




























