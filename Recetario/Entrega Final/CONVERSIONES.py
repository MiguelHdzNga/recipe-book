#CONVERSIONES

from tkinter import*
from tkinter import ttk
from tkinter.font import Font

#Funciones
def ConUnidades():
    if valor0.get()=="g a Kg":
        convert1=float(Conversion.get()/1000)
        convert2="Kg=",str('%.2f'%(convert1))#dos decimales en el resultado
        Unidades.set(convert2)

    elif valor0.get()=="L a mL":
        convert1=float(Conversion.get()*1000)
        convert2="mL=",str('%.2f'%(convert1))
        Unidades.set(convert2)

    elif valor0.get()=="Kg a tz":
        convert1=float(Conversion.get()*1000/200)
        convert2="tz=",str('%.2f'%(convert1))
        Unidades.set(convert2)

    elif valor0.get()=="tz a g":
        convert1=float(Conversion.get()*200)
        convert2="g=",str('%.2f'%(convert1))
        Unidades.set(convert2)

    elif valor0.get()=="cda a g":
        convert1=float(Conversion.get()*14)
        convert2="g=",str('%.2f'%(convert1))
        Unidades.set(convert2)


def Borrar():
    valor0.set("")
    Conversion.set("0.0")
    Unidades.set("0.0")

def btn(Frame,texto,funcion,renglon):
    Button(Frame, text=texto, padx=2, pady=2, bd=2, fg="black",
           font=myfont, width=12, height=1, command=funcion).grid(row=renglon, column=0)

#Raíz
raiz=Tk()
raiz.title("Recetario Inteligente")
raiz.geometry('1000x400')
raiz.config(bg='white smoke')
raiz.resizable(0,0)
raiz.iconbitmap('estufa.ico')

#Fuente
myfont2= Font (family="Arial",size=30)
myfont= Font(family='Arial',size=20)

etiqueta1=Label(raiz,text="Conversiones",bg='white smoke',fg='black',font=myfont2)
etiqueta1.pack(padx=50,pady=50)


#Variables
valor0=StringVar()
Conversion=DoubleVar()
Unidades=DoubleVar()

#Frames
FrameIzquierdo=Frame(raiz, width=660, height=400, bd=8, relief="raise")
FrameIzquierdo.pack(side=LEFT)
FrameDerecho=Frame(raiz, width=200, height=400, bd=8, relief="raise")
FrameDerecho.pack(side=RIGHT)


#Entrada de datos
EntUnidades=Entry(FrameIzquierdo, font=myfont,textvariable=Conversion,bd=2,width=28, justify='center')
EntUnidades.grid(row=0,column=1)


#Menú desplegable
CajaOpciones=ttk.Combobox(FrameIzquierdo, textvariable=valor0,state='readonly',font=myfont,width=20)
CajaOpciones['values']=(' ','g a Kg','L a mL','Kg a tz','tz a g','cda a g')
CajaOpciones.current(0)
CajaOpciones.grid(row=4,column=2)


#Etiquetas
etiquetaUnidadesResultado=Label(FrameIzquierdo,font=myfont,textvariable=Unidades,bd=2,width=25,bg="white",pady=2,padx=2,relief='sunken')
etiquetaUnidadesResultado.grid(row=4,column=1)

etiquetaBarraUnidades=Label(FrameIzquierdo,font=myfont,text='Unidades',padx=2, pady=2,bd=2,fg="black",width=18)
etiquetaBarraUnidades.grid(row=0,column=2,sticky=W)

#Botones
botonConversiones=btn(FrameDerecho,'Convertir',ConUnidades,2)
botonBorrar=btn(FrameDerecho,'Borrar',Borrar,3)

raiz.mainloop()
