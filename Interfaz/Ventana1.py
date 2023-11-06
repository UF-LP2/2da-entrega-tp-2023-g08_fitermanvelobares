from tkinter import *
from tkinter import messagebox

#Creo la clase
class App():
    def __init__(self):
        ventana = Tk()
        ventana.geometry("500x500")
        ventana.config(bg='lightblue')
        ventana.title("Hospital")
        ventana.resizable(width=False,height=False)
        

        #widgets
        self.label1 = Label(ventana, text="Simulacion Hospital",bg='lightgreen')
        self.label1.place(x=160, y=20)
        self.text1=Entry(ventana,bg='grey')
        self.text1.place(x=130, y=200)

        #boton
        self.bt1= Button(ventana, text="Simular", command=self.simulacion)
        self.bt1.place(x=130, y=50)
        
        
        
        ventana.mainloop()
        
    def simulacion(self):
        messagebox.showinfo(message="Atendiendo a"+self.text1.get(), title="Simulacion Hospital")

#Programa principal
Objeto_ventaja = App()