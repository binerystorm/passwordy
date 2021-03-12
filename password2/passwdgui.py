# imports
from tkinter import *
import random

#defineing class for all buttons and labels
class Btn_Lbl:
    def __init__(self, rootwin):
        #importing files
        self.word_list = []
        with open("word_list.txt", "r") as file:
            for line in file:
                self.word_list.append(line.strip("\n"))
 
        self.word_list_d = []
        with open("dutch_word_list.txt","r") as filed:
            for line in filed:
                self.word_list_d.append(line.strip("\n"))

        #global vars
        self.coming_from = ""
        self.ent_range = ["3","4","5","6","7"]
        self.error_count = 0
        
        #making of the password
        self.password = Label(rootwin)
        self.ent_instructoins = Label(rootwin, text = "how many words?")
        self.ent_error = Label(rootwin, text = "somthing went wrong try using a number in the recommended range \n and make sure the number not the word of the number")
        self.yes_no_intstructions = Label(rootwin, text = "multilanguige? (yes or no)")
        self.lblpassword = Label(rootwin, text = "your password is:")

        #main buttons
        self.rootwin = rootwin
        self.lbltitle = Label(self.rootwin, text = 'password genorator \npassword type?')
        self.btnpathetick = Button(self.rootwin, text = "pathetick", command = self.pathetick)
        self.btnweak = Button(self.rootwin, text = "weak", command = self.weak)
        self.btnstrong = Button(self.rootwin, text = "strong", command = self.strong)
        self.btnverystrong = Button(self.rootwin, text = "very strong", command = self.verystrong)

        self.btnyes = Button(self.rootwin, text = "yes", command = self.yes)
        self.btnno = Button(self.rootwin, text = "no", command = self.no)

        self.entword_count = Entry(self.rootwin)

        #other stuff

    #button functions
    def pathetick(self):
        self.password.destroy()
        self.password = Label(self.rootwin, text = "password123")
        self.password.grid(row = 7, column = 0, columnspan = 4)


    def weak(self):
        code = ''
        for t in range(4):
            code += str(random.randint(0, 9))

        self.password.destroy()
        self.password = Label(self.rootwin, text = code)
        self.password.grid(row = 7, column = 0, columnspan = 4)
        

    def strong(self):
        self.coming_from = "strong"
        self.error_count = 0

        self.ent_instructoins.grid(row = 2, column = 0, columnspan = 4)

        self.entword_count.grid(row = 3, column = 0, columnspan = 4)

        self.yes_no_intstructions.grid(row = 4, column = 0, columnspan = 4)

        self.btnyes.grid(row = 5, column = 1)

        self.btnno.grid(row = 5, column = 2)


    def verystrong(self):
        self.coming_from = "very strong"
        self.error_count = 0
        self.yes_no_intstructions.grid(row = 2, column = 0, columnspan = 4)

        self.btnyes.grid(row = 3, column = 1)

        self.btnno.grid(row = 3, column = 2)

    def yes(self):
        if self.coming_from == "strong":

            wordcount = self.entword_count.get()
            if wordcount in self.ent_range:
                wordcount = int(wordcount)
            elif self.error_count == 0:
                self.ent_instructoins.grid_forget()
                self.ent_error.grid(row = 2, column = 0, columnspan = 4)
                self.error_count += 1
                return
            elif self.error_count > 0:
                return

            password_key = self.multi_lang_code(wordcount)
            password = self.gen_password(password_key)

            if self.error_count == 0:
                self.ent_instructoins.grid_forget()
            else:
                self.ent_error.grid_forget()
            self.entword_count.grid_forget()
        else:
            wordcount = 7
            password_key = self.multi_lang_code(wordcount)
            password = self.hasher(self.gen_password(password_key))
        self.password.destroy()
        self.password = Label(self.rootwin, text = password)

        self.password.grid(row = 7, column = 0, columnspan = 4)

        self.btnyes.grid_forget()
        self.btnno.grid_forget()
        self.yes_no_intstructions.grid_forget()

    
    def no(self):
        if self.coming_from == "strong":
            wordcount = self.entword_count.get()
            if wordcount in self.ent_range:
                wordcount = int(wordcount)
            elif self.error_count == 0:
                self.ent_instructoins.grid_forget()
                self.ent_error.grid(row = 2, column = 0, columnspan = 4)
                self.error_count += 1
                return
            elif self.error_count > 0:
                return

            password = self.gen_password(wordcount)

            if self.error_count == 0:
                self.ent_instructoins.grid_forget()
            else:
                self.ent_error.grid_forget()
            self.entword_count.grid_forget()
        else:
            wordcount = 7 
            password = self.hasher(self.gen_password(wordcount))

        self.password.destroy()
        self.password = Label(self.rootwin, text = password)

        self.password.grid(row = 7, column = 0, columnspan = 4)

        self.btnyes.grid_forget()
        self.btnno.grid_forget()
        self.yes_no_intstructions.grid_forget()


    #other functions
    def multi_lang_code(self, length):
        langcode = []
        for x in range(length):
            langcode.append(random.randint(0,1))
        check = langcode.count(1)
        if check == 0:
            langcode[random.randint(0, 6)] = 1
        elif check == length:
            langcode[random.randint(0, 6)] = 0
        return langcode


    def gen_password(self, langcode):
        if type(langcode) == list:
            password = ""
            if langcode[0] == 1:
                index = random.randint(0, 847)
                password += self.word_list[index]
            else:
                index_d = random.randint(0, 881)
                password += self.word_list_d[index_d]

            for c in range(1, len(langcode)):
                if langcode[c] == 1:
                    index = random.randint(0, 847)
                    password += f"_{self.word_list[index]}"
                else:
                    index_d = random.randint(0, 881)
                    password += f"_{self.word_list_d[index_d]}"
            return password

        elif type(langcode) == int:
            password = ""
            password += self.word_list[random.randint(0, 847)]
            for x in range(langcode - 1):
                index = random.randint(0, 847)
                password += f'_{self.word_list[index]}'
            return password


    def hasher(self, password):
        chari = ["!","@","#","$","%","^","&","*"]
        repeat = random.randint(2,5)
        for x in range(repeat):
            index = random.randint(0, len(password)-1)
            char_index = random.randint(0, 7)
            password = password.replace(password[index], chari[char_index])
        return password



#defining of the main window
root = Tk()
window_content = Btn_Lbl(root)

#   building the window

window_content.lbltitle.grid(row = 0, column = 0, columnspan = 4)
window_content.btnpathetick.grid(row = 1, column = 0)
window_content.btnweak.grid(row = 1, column = 1)
window_content.btnstrong.grid(row = 1, column = 2)
window_content.btnverystrong.grid(row = 1, column = 3)
window_content.lblpassword.grid(row = 6, column = 0, columnspan = 4)

root.mainloop()
