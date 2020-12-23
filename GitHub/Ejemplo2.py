from tkinter import *
import Pmw
    


class Boot(Frame): 

    def __init__(self, master=NONE):
        Frame.__init__(self,master)
        self.pack()
        self.iniciarComponentes()

    def iniciarComponentes(self):
        bar = Menu(self)
        self.master.config(menu=bar)

        archivo = Menu(bar, tearoff=0)
        editar = Menu(bar, tearoff=0)

        bar.add_cascade(label='Archivo',menu=archivo)
        archivo.add_command(label="Nuevo")
        bar.add_cascade(label='Editar',menu=editar)

        frame = LabelFrame(self.master,text='Editor de texto', padx=5,pady=5)
        frame.pack()

        Text(frame).pack()
        Button(frame,text='Evento').pack(padx=5, pady=5)
        

root = Tk()
boot = Boot(master = root)
boot.mainloop()


