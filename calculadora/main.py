from tkinter import *

class Aplicacion:
    def __init__(self):
        pass
    
    def menu_inicio(self):
        # Raiz
        root = Tk()
        root.title("Calculadora polinomios")
        root.resizable(0,0)

        # FramePrincipal
        frame = Frame(root, width=580, height=420)
        frame.pack()
        frame.config(cursor="plus", bg="peachpuff", bd=25, relief="groove")

        #Etiquetas
        label_1 = Label(frame, text="Bienvenido a la calculadora de polinomios")
        label_1.place(x=150, y=130)
        label_1.config(bg="peachpuff", relief="groove")

        label_2 = Label(frame, text="Hecho por Luis Alejandro Alfaro")
        label_2.place(x=355, y=348) 
        







        root.mainloop()
        



if __name__ == '__main__':
    calculadora = Aplicacion()
    calculadora.menu_inicio()
    

    
