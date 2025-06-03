from tkinter import Tk, Frame, Button, Entry, Label, Scrollbar, StringVar, Text, END
from tkinter.font import Font
import FuncionesGuiRecetario as funcionesGui

#Funciones
def codigo_boton():
    tipo_data=tipo.get().strip()
    nombre_data=nombre.get()
    ingredientes_data=str(ingredientes.get())
    procedimiento_data=str(procedimiento_texto.get(1.0, END+"-1c"))
    print(tipo_data)
    print(nombre_data)
    print(ingredientes_data)
    print(procedimiento_data)

    funcionesGui.crear_receta(tipo_data, nombre_data, ingredientes_data, procedimiento_data)


    tipo_texto.delete(0,END)
    nombre_texto.delete(0,END)
    ingredientes_texto.delete(0,END)
    procedimiento_texto.delete(0.0,END)

def label(texto,renglon):
    lbl=Label(frame,text=texto,bg='white smoke',font=myfont)
    lbl.grid(row=renglon,column=0,sticky="n",padx=2,pady=10)


def btn(texto,funcion):
    btn=Button(frame, text=texto,command=funcion,font=myfont)
    btn.grid(row=7,column=1)


#Raiz
root = Tk()
root.title("Recetario Inteligente")
root.geometry('338x334')
root.config(bg='white smoke')
root.resizable(0,0)
root.iconbitmap('estufa.ico')

#Fuente
myfont= Font(family="Arial",size=10)

#Variables

tipo= StringVar()
nombre= StringVar()
ingredientes= StringVar()
procedimiento= StringVar()


#Frame
frame=Frame(root)
frame.pack(fill='both', expand=1)
frame.config(bg="white smoke")


#Etiquetas
tipo_label=  label("Tipo:",0)
nombre_label=  label("Nombre",1)
ingredientes_label = label("Ingredientes",2)
procedimiento_label= label("Procedimiento",6)



#Entradas de texto
tipo_texto = Entry(frame, textvariable=tipo,width="33")
tipo_texto.grid(row=0, column=1, padx=2, pady=2)
nombre_texto = Entry(frame,textvariable=nombre,width="33")
nombre_texto.grid(row=1, column=1, padx=2, pady=2)
ingredientes_texto = Entry(frame,textvariable=ingredientes,width="33")
ingredientes_texto.grid(row=2, column=1, padx=2, pady=2)
procedimiento_texto = Text(frame, width=25, height=8)
procedimiento_texto.grid(row=6, column=1, padx=2, pady=2)


#scroll
scroll_vert = Scrollbar(frame, command=procedimiento_texto.yview)
scroll_vert.grid(row=6, column=2, sticky="nsew")
procedimiento_texto.config(yscrollcommand=scroll_vert.set)


#boton guardar
boton_guardar=btn("Guardar",codigo_boton)


root.mainloop()