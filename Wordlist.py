from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import string
import itertools
import threading

class liste(Tk):
    def __init__(self):
        super(liste, self).__init__()
        self.title("Create wordlist")
        self.geometry("300x500")
        self.layout()


    def layout(self):
        """
        All  my wighets is here
        labelframe
        button
        checkbutton
        radiobutton

        """
        self.right = ttk.LabelFrame(self, text='Wordlist')
        self.default = ttk.LabelFrame(self.right, text="Defaut Mode")
        self.repeat = ttk.LabelFrame(self.right, text="Repeat")
        #My Control variables******************
        self.var_enter = StringVar()
        self.var_enter_repeat = StringVar()
        self.var_choix = DoubleVar()
        self.var_choix1 = DoubleVar()
        self.choice_mode = StringVar()
        self.word_letters = DoubleVar()
        self.MODES = StringVar()

        # self.modes_names = {'Number Only':Number Only,'Letters Only': string.ascii_lowercase, "Digist with Number":string.digits+string.ascii_lowercase}

        self.Modes1 = ttk.Radiobutton(self.default, text='Number Only', value=string.digits, variable=self.MODES)
        self.Modes2 = ttk.Radiobutton(self.default, text='Letters Only', value=string.ascii_lowercase, variable=self.MODES)
        self.Modes3 = ttk.Radiobutton(self.default, text='Digist with Number', value=string.digits+string.ascii_lowercase, variable=self.MODES)

        self.Modes1.pack(side="top",fill="both", expand=1, padx=30)
        self.Modes2.pack(side="top",fill="both", expand=1, padx=30)
        self.Modes3.pack(side="top",fill="both", expand=1, padx=30)


        self.var_choix1.trace('w', self.see_choice1)
        self.select_words = ttk.Checkbutton(self.right, name="person" ,text="Entrer your words", variable=self.var_choix1)

        self.entrer = Entry(self.right, width=30, textvariable=self.var_enter,  state="disable")
        self.entrer_repeat = Entry(self.repeat, width=10, textvariable=self.var_enter_repeat)
        self.var_enter_repeat.trace("w", self.observation)
        self.word_letters.trace("w", self.trace_word)
        self.word_or_letters = ttk.Checkbutton(self.right, name="letter or word", text="Your text in letters", variable=self.word_letters, state="disable")
        self.choix = Checkbutton(self.right, name="choix" ,text="with uppercase", variable=self.var_choix)

        self.select_mode = ttk.LabelFrame(self.right, text="Choix Mode")

        self.choice_mode1 = ttk.Radiobutton(self.select_mode, value="C", text="Combination", variable=self.choice_mode)
        self.choice_mode2 = ttk.Radiobutton(self.select_mode, value="R", text="Repetition",variable=self.choice_mode)

        self.valider = Button(self.right, bitmap="gray50", command=self.thread, border=0, cursor="hand2")
        self.label_see = Label(self.right)
        #pack my wighets **********************
        self.default.pack(fill="both", expand=1)
        self.select_words.pack(fill="both", expand=1)
        self.entrer.pack(fill="both", expand=1)
        self.word_or_letters.pack(fill="both", expand=1)
        self.entrer_repeat.pack()
        self.repeat.pack(fill="both", pady=20)
        self.choix.pack(fill="both", expand=1)
        self.select_mode.pack(fill="both", expand=1, pady=20)
        self.choice_mode1.pack(fill="both", expand=1, padx=20)
        self.choice_mode2.pack(fill="both", expand=1, padx=20)
        self.valider.pack(fill="both", expand=1)
        self.label_see.pack(expand=1)
        
        self.right.pack(fill="both", expand=1, pady=20)

    def see_choice1(self, *args):
        if self.var_choix1.get()==1:
            self.choix.config(state="disable")
            self.entrer.config(state='normal')
            self.word_or_letters.config(state="normal")
            self.Modes1.config(state="disable")
            self.Modes2.config(state="disable")
            self.Modes3.config(state="disable")
        else:
            self.entrer.config(state="disable")
            self.word_or_letters.config(state="disable")
            self.Modes1.config(state="normal")
            self.Modes2.config(state="normal")
            self.Modes3.config(state="normal")

    def thread(self):
        threading.Thread(target=self.work).start()
    
    def work(self):
        try:
            if self.var_choix1.get():
                Letters = self.var_enter.get()
                if self.word_letters.get():
                

                    if self.var_choix.get():
                        alls = Letters+Letters.upper()
                        if self.choice_mode.get()=="R":
                            self.product(self.var_enter_repeat.get(), alls)
                        elif self.choice_mode.get()=="C":
                            self.comibination(self.var_enter_repeat.get(), alls)
                        else:
                            messagebox.showerror("Error", "Please choice The mode")
                    else:
                        if self.choice_mode.get()=="R":
                            self.product(self.var_enter_repeat.get(), Letters)
                        elif self.choice_mode.get()=="C":
                            self.comibination(self.var_enter_repeat.get(), Letters)
                        else:
                            messagebox.showerror("Error", "Please choice The mode")
                else:
                    listeofword = self.var_enter.get().split(' ')
                    well = ''.join(listeofword)
                    if self.choice_mode.get()=="R":
                        self.product(self.var_enter_repeat.get(),well)
                    elif self.choice_mode.get()=="C":
                        self.comibination(self.var_enter_repeat.get(), well)
                    else:
                        messagebox.showerror("Error", "Please choice The mode")
        except AttributeError:
            pass


        else:
            Letters = self.MODES.get()
            if self.var_choix.get():
                alls = Letters+Letters.upper()
                if self.choice_mode.get()=="R":
                    self.product(self.var_enter_repeat.get(), alls)
                elif self.choice_mode.get()=="C":
                    self.comibination(self.var_enter_repeat.get(), alls)
                else:
                    messagebox.showerror("Error", "Please choice The mode")
            else:
                if self.choice_mode.get()=="R":
                    self.product(self.var_enter_repeat.get(), Letters)
                elif self.choice_mode.get()=="C":
                    self.comibination(self.var_enter_repeat.get(), Letters)
                else:
                    messagebox.showerror("Error", "Please choice The mode")


    def funct(self):
        op = f'{self.conter}/{self.len}'
        
        self.label_see.config(text=f'luncher {op}')
        if self.conter ==self.len+1:self.label_see.config(text=f"finiched {self.len} words generate",bg="green", fg="white")
        
    def product(self, repeat, chars):
        self.conter  = 1
        try:
            name = filedialog.asksaveasfile(initialdir="/", title='Save As', filetype=(("text","txt"),('*.*',"all file")), defaultextension='txt')
            self.label_see.config(text='luncher')
            for i in(itertools.product(chars, repeat=int(repeat))):
                self.len = len(chars)**int(repeat)
                self.charactes = "".join(i)
                with open(name.name, "a") as file:
                        file.write(f'{self.charactes} \n')
                        self.label_see.after(2, self.funct)
                        self.conter += 1

    
        except TypeError:
            messagebox.showerror("Please ","Please Enter Numbers Here")
        except ValueError:

            messagebox.showerror("Error", "Repeat is void")
        except AttributeError:
            self.label_see.config(text="")


    def comibination(self, repeat, chars):
        name = filedialog.asksaveasfile(initialdir="/", title='Save as', filetype=(("text","txt"),('*.*',"all file")), defaultextension='txt')
        self.conter = 1
        try:
            self.label_see.config(text='lunch')
            for i in (itertools.combinations(chars, int(repeat))):
                self.len = len(list((itertools.combinations(chars, int(repeat)))))
                
                self.charactes = "".join(i)
                with open(name.name, "a") as file:
                    file.write(f'{self.charactes} \n')
                    self.label_see.after(2, self.funct)
                    self.conter +=1

        except TypeError:
            messagebox.showerror("Please ","Please Enter Numbers Here")

        except ValueError:
            messagebox.showerror("Error", "Repeat is void")
        except AttributeError:
            self.label_see.config(text="")

    def observation(self, *args):

        if self.var_enter_repeat.get().isdigit():
            self.valider.config(state="normal")
            self.entrer_repeat.config(background="white")
        else:
            self.valider.config(state="disable")
            self.entrer_repeat.config(background="red")

    def progress_bar(self, max):
        self.var_bar = IntVar()
        self.bar = ttk.Progressbar(self.right ,maximum=max ,value=1, variable=self.var_bar, length=20, phase=10 )

        self.bar.pack(fill='both', side="bottom", expand=1)

    def you(self, *args):
        print(self.var_bar.get())

    def trace_word(self,*args):
        if self.word_letters.get():self.choix.config(state="normal")
            
        else:self.choix.config(state="disable")
            


if __name__ =="__main__":
    liste().mainloop()

