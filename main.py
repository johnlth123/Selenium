import threading
from tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class App(threading.Thread):
    def __init__(self):
        super().__init__()
        self.opt = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.opt)
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login&GPage=https%3A%2F%2Ftickets.interpark.com"
        self.driver.get(self.url)
        self.dp = Tk()
        self.dp.geometry("500x500")
        self.dp.title("인터파크 매크로")
        self.dp.configure(bg="gray")  # GUI 배경색 변경

        self.object_frame = Frame(self.dp, bg="gray") 
        self.object_frame.pack()

        self.id_label = Label(self.object_frame, text = "ID")
        self.id_label.grid(row=1, column=0)
        self.id_entry = Entry(self.object_frame, width=40)
        self.id_entry.grid(row=1, column=1)
        self.pw_label = Label(self.object_frame, text = "PASSWORD")
        self.pw_label.grid(row=2, column=0)
        self.pw_entry = Entry(self.object_frame, width=40)
        self.pw_entry.grid(row=2, column=1)
        self.login_button = Button(self.object_frame, text="Login", width=3, height=2)
        self.login_button.grid(row=3, column=1)
        
        self.dp.mainloop()


    # def login_go(self):
    #     def task():
    #         self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
    #         self.driver.find_element_by_name('userID')
app = App()
app.start()
        
