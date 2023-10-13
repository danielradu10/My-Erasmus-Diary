import datetime
from MyRoot import MyRoot
from LogIn import *
from DataBaseManager import DataBaseManager

if __name__ == '__main__':
    print('PyCharm')
    print(str(datetime.datetime.now().date()))

    database = DataBaseManager()

    logIn = LogInProxy(database)

    logInManager = LogInManager(logInProxy=logIn)

    window = MyRoot(logInManager, database)

    window.mainloop()



