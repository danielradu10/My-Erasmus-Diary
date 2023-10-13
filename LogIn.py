import tkinter as tkinter
from DataBaseManager import DataBaseManager

class LogIn:
    def get_the_username(self, username: tkinter.StringVar, oldframe: tkinter.Frame, newframe: tkinter.Frame):
        pass

    def get_the_pass(self, password: tkinter.StringVar, oldframe: tkinter.Frame, newframe: tkinter.Frame):
        pass


class LogInProxy(LogIn):
    def __init__(self, database: DataBaseManager):
        self.database = database

    def get_the_username(self, username: tkinter.StringVar, oldframe: tkinter.Frame, newframe: tkinter.Frame):
        newframe.pack()
        oldframe.pack_forget()

    def get_the_pass(self, password: tkinter.StringVar, oldframe: tkinter.Frame, newframe: tkinter.Frame):
        newframe.pack()
        oldframe.pack_forget()




class LogInManager(LogIn):
    def __init__(self, logInProxy: LogIn):
        self.logInProxy = logInProxy
        self.username = ""

    def get_the_username(self, username: tkinter.StringVar, oldframe: tkinter.Frame, newframe: tkinter.Frame):
        text = username.get()
        if(text == ""):
            self.logInProxy.get_the_username(username, oldframe, newframe)

    def get_the_pass(self, password: tkinter.StringVar, oldframe: tkinter.Frame, newframe: tkinter.Frame):
        text = password.get()
        if(text == ""):
            self.logInProxy.get_the_pass(password, oldframe, newframe)
            newframe.add_menu()


