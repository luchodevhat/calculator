from tkinter import *

class Aplicacion_menu:
    def __init__(self):
        pass
    
    def menu_inicio(self):
        # Raiz
        root = Tk()
        root.title("Calculadora polinomios")
        root.resizable(0,0)

        # FramePrincipal
        frame = Frame(root, width=420, height=580)
        frame.pack()
        frame.config(cursor="plus", bg="peachpuff", bd=25, relief="groove")

        #Entry
        pantalla = Entry(frame, width=40)
        pantalla.place(x=75, y=50)
        pantalla.config(bg="peachpuff", justify="center", state="disabled")
 

        #Etiquetas
        label_1 = Label(frame, text="Bienvenido a la calculadora PYTHON")
        label_1.place(x=90, y=505)
        label_1.config(bg="peachpuff", relief="groove")

        #Botones
        






        root.mainloop()
        



if __name__ == '__main__':
    calculadora = Aplicacion_menu()
    calculadora.menu_inicio()
    

    
