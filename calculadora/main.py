from tkinter import *
from math import *

class Aplicacion_menu:
    def __init__(self, comas=0, input_text="", width=2, height=1):
        self.comas = comas
        self.input_text = input_text
        self.width = width
        self.height = height

    
    def clear(): 
        pass

    def digit():
        pass

    def coma():
        pass


    
    def menu_start(self):
        # Raiz
        root = Tk()
        root.title("Calculadora polinomios")
        root.resizable(0,0)

        # FramePrincipal
        frame = Frame(root, width=420, height=580)
        frame.pack()
        frame.config(cursor="plus", bg="gray20", bd=25)

        #Entry
        pantalla = Entry(frame, width=40)
        pantalla.place(x=65, y=50)
        pantalla.config(bg="peachpuff", justify="center", state="disabled", relief="sunken")
 

        #Etiquetas
        label_1 = Label(frame, text="Bienvenido a la calculadora PYTHON")
        label_1.place(x=90, y=505)
        label_1.config(bg="peachpuff", relief="groove")

        #Botones
        button_0 = Button(frame, text= 0, width=2, height=1)
        button_0.place(x=60, y=100)
        button_0.config(bg="gray50")

        button_1 = Button(frame, text= 1, width=2, height=1)
        button_1.place(x=90, y=100)
        button_1.config(bg="gray50")

        button_2 = Button(frame, text= 2, width=2, height=1)
        button_2.place(x=120, y=100)
        button_2.config(bg="gray50")

        button_3 = Button(frame, text= 3, width=2, height=1)
        button_3.place(x=150, y=100)
        button_3.config(bg="gray50")

        button_ce = Button(frame, text= "CE", width=3, height=1)
        button_ce.place(x=180, y=100)
        button_ce.config(bg="red")


        button_c = Button(frame, text= "C", width=3, height=1)
        button_c.place(x=220, y=100)
        button_c.config(bg="red")


        button_4 = Button(frame, text= 4, width=2, height=1)
        button_4.place(x=60, y=130)
        button_4.config(bg="gray50")

        button_5 = Button(frame, text= 5, width=2, height=1)
        button_5.place(x=90, y=130)
        button_5.config(bg="gray50")

        button_6 = Button(frame, text= 6, width=2, height=1)
        button_6.place(x=120, y=130)
        button_6.config(bg="gray50")

        button_7 = Button(frame, text= 7, width=2, height=1)
        button_7.place(x=150, y=130)
        button_7.config(bg="gray50")

        button_8 = Button(frame, text= 8, width=2, height=1)
        button_8.place(x=180, y=130)
        button_8.config(bg="gray50")

        button_9 = Button(frame, text= 9, width=2, height=1)
        button_9.place(x=210, y=130)
        button_9.config(bg="gray50")

        button_sum = Button(frame, text= "+", width=2, height=1)
        button_sum.place(x=60, y=160)
        button_sum.config(bg="gray50")

        button_subtraction = Button(frame, text= "-", width=2, height=1)
        button_subtraction.place(x=90, y=160)
        button_subtraction.config(bg="gray50")

        button_division = Button(frame, text= "/", width=2, height=1)
        button_division.place(x=120, y=160)
        button_division.config(bg="gray50")

        button_multiplication = Button(frame, text= "*", width=2, height=1)
        button_multiplication.place(x=150, y=160)
        button_multiplication.config(bg="gray50")

        button_square_root = Button(frame, text= "√", width=2, height=1)
        button_square_root.place(x=180, y=160)
        button_square_root.config(bg="gray50")

        button_rest = Button(frame, text= "%", width=2, height=1)
        button_rest.place(x=210, y=160)
        button_rest.config(bg="gray50")

        button_equal = Button(frame, text= "=", width=3, height=1)
        button_equal.place(x=240, y=160)
        button_equal.config(bg="red")

        root.mainloop()
        



if __name__ == '__main__':
    calculadora = Aplicacion_menu()
    calculadora.menu_start()
    

    
