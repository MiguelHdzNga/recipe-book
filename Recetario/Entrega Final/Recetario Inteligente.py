from tkinter import*
from tkinter.font import Font
import os
import tkinter as tk
import random
import FuncionesGuiRecetario as funcionesGui

#Instalacion de folders
if 'Recetario Inteligente DB' not in os.getcwd():
    funcionesGui.instalacion()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('cwd:', os.getcwd())

raiz=Tk()
raiz.title("Recetario Inteligente")
raiz.resizable(0,0)
raiz.geometry('338x334')
raiz.iconbitmap('estufa.ico')

Frame= Frame(raiz)
Frame.pack(fill='both', expand=1)
Frame.config(bg="white smoke")

tipoFuente3= Font (family="Arial",size=11)

tipoFuente2= Font (family="Arial",size=12)

tipoFuente1= Font (family="Arial",size=15)
#__________________________________________________BOTONES______________________________________________________________

def tipoBoton1(funcion,texto,ejey):
    boton=Button(Frame, text=texto,command=funcion,font=tipoFuente2)
    boton.place(x=110,y=ejey)
    boton.config(width=11,height=1)

def tipoBoton2(funcion,texto,ejey):
    boton=Button(Frame, text=texto,command=funcion,font=tipoFuente2)
    boton.place(x=110,y=ejey)
    boton.config(width=12,height=2)

def tipoBoton3(funcion,texto):
    boton=Button(Frame, text=texto,command=funcion,font=tipoFuente2)
    boton.place(x=190,y=280)
    boton.config(width=13,height=1)

def tipoBoton4(funcion,texto,ejex):
    boton=Button(Frame, text=texto,command=funcion,font=tipoFuente2)
    boton.place(x=ejex,y=100)
    boton.config(width=15,height=1)

def tipoBoton5(funcion,texto,ejey, anchura):
    boton=Button(Frame, text=texto,command=funcion,font=tipoFuente2)
    boton.place(x=90,y=ejey)
    boton.config(width=anchura,height=1)

def botonAtras(funcion):
    atras=Button(Frame, command=funcion, text='Atrás',font=tipoFuente2)
    atras.place(x=20, y=280)
    atras.config(width=11, height=1)

def botonSiguiente(funcion):
    siguiente=Button(Frame, command=funcion, text='Siguiente', font=tipoFuente2)
    siguiente.place(x=210, y=280)
    siguiente.config(width=11, height=1)

def botonVolverCocinar(funcion):
    botonVolver=tipoBoton3(funcion, 'Volver a cocinar')

def botonOk(funcion):
    boton=Button(Frame, command=funcion, text='Ok', font=tipoFuente2, fg="white", bg="red")
    boton.place(x=110, y=280)
    boton.config(width=11, height=1)
#_______________________________________________ETIQUETAS_______________________________________________________________

def tipoEtiqueta1(texto):
    lbl=Label(Frame,text=texto,bg='white smoke',fg='black',font=tipoFuente1)
    lbl.pack(padx=50,pady=50)

def tipoEtiqueta2(texto):
    lbl=Label(Frame,text=texto,bg='white smoke',fg='black',font=tipoFuente1)
    lbl.pack(padx=20,pady=20)

def tipoEtiqueta3(texto,formato,ejex,ejey):
    lbl=Label(Frame,text=texto,bg='white smoke',fg='black',font=formato)
    lbl.pack(padx=ejex,pady=ejey)
#__________________________________________FUNCION LIMPIAR VENTANA______________________________________________________

def limpiarVentana(event=None):

    for child in Frame.winfo_children():
        child.destroy()
#_________________________________________VENTANA PRINCIPAL_____________________________________________________________

def ventanaPrincipal(event=None):

    limpiarVentana()

    etiquetaRecetarioInteligente= tipoEtiqueta1("Recetario Inteligente")

    botonRecetario= tipoBoton1(VentanaOpRecetario, 'Recetario',100)

    botonCocinar= tipoBoton1(ventanaCocinar, 'Cocinar',140)

    botonAprender= tipoBoton1(ventanaAprender,'Aprender',180)

#________________________________________VENTANA NUEVA RECETA___________________________________________________________

def VentanaOpRecetario(event=None):

    limpiarVentana()

    etiquetaRecetario= tipoEtiqueta1("Recetario")

    botonNuevaReceta= tipoBoton2(ventanaReestriccionesNuevaReceta,'Nueva receta',100)

    botonAtras(ventanaPrincipal)
#________________________________________VENTANA COCINAR______________________________________________________________________

def ventanaCocinar(event=None):

    limpiarVentana()

    etiquetaCocinar= tipoEtiqueta1("Cocinar")

    botonConversiones= tipoBoton1(ventanaconversiones2,'Conversiones',100)

    botonMenu= tipoBoton1(ventanaReestriccionesMenu,'Menu',140)

    botonAtras(ventanaPrincipal)
#________________________________________VENTANA CONVERSIONES (os.systemConversiones)___________________________________

def ventanaConversiones(event=None):

    limpiarVentana()

    etiquetaConversiones= tipoEtiqueta1("Conversiones")

    botonAtras(ventanaCocinar)

    os.system("CONVERSIONES.py")

def ventanaconversiones2(event=None):

    limpiarVentana()

    etiquetaAtencion= tipoEtiqueta3("¡ATENCION!",tipoFuente1,13,13)

    etiquetaReestriccion= tipoEtiqueta3("Máximo 20 caracteres incluyendo el (.) decimal.",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3("Longitud mínima de 1 caracter. No dejar vacio.",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3("Sólo caracteres numericos y un punto para",tipoFuente3,15,15)

    etiquetaReestriccion= tipoEtiqueta3("la cantidad decimal. No ingresar espacios.", tipoFuente3, 15, 15)

    botonOk(ventanaConversiones)
#______________________________________VENTANA NUEVA RECETA (os.system)_________________________________________________

def ventanaNuevaReceta(event=None):

    limpiarVentana()

    etiquetaNuevaReceta= tipoEtiqueta1("Nueva Receta")

    botonAtras(VentanaOpRecetario)

    os.system("AgregarRecetaConFunciones.py")

def ventanaReestriccionesNuevaReceta(event=None):

    limpiarVentana()

    etiquetaAtencion= tipoEtiqueta3("Para un funcionamiento correcto:",tipoFuente1,13,13)

    etiquetaReestriccion= tipoEtiqueta3("Escribir 'Aprender' o 'Normal' en 'Tipo'",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3("Usar un 'Nombre' de menos de 100 caracteres",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3("Separar 'Ingredientes' y pasos del...",tipoFuente3,15,15)

    etiquetaReestriccion= tipoEtiqueta3("'Procedimiento' por medio de punto y coma (;)", tipoFuente3, 15, 15)

    botonOk(ventanaNuevaReceta)
#________________________________________VENTANA APRENDER A COCINAR_____________________________________________________

def ventanaAprender(event=None):

    limpiarVentana()

    etiquetaAprenderCocinar= tipoEtiqueta1("Aprender a cocinar")

    botonHacerReceta= tipoBoton1(ventanaHacerReceta,'Hacer receta',100)

    botonJugar= tipoBoton1(ventanaJugar,'Jugar',140)

    botonAtras(ventanaPrincipal)
#________________________________________VENTANA HACER RECETA___________________________________________________________

def ventanaHacerReceta(event=None):

    limpiarVentana()

    etiquetaHacerReceta= tipoEtiqueta1("Hacer receta")

    botonRecetario= tipoBoton1(ventanaTipo,'Recetario',100)

    botonRecetaAleatoria= tipoBoton5(ventanaReestriccionesAleatoria,'Receta Aleatoria',140,15)

    botonAtras(ventanaAprender)
#________________________________________VENTANA RECETA TIPO____________________________________________________________

def ventanaTipo(event=None):

    limpiarVentana()

    etiquetaTipo= tipoEtiqueta2("Tipo")

    botonBebida= tipoBoton1(ventanaBebida, 'Bebida',60)

    botonSnack= tipoBoton1(ventanaSnack, 'Snack',100)

    botonDesayuno= tipoBoton1(ventanaDesayuno,'Desayuno',139)

    botonComida= tipoBoton1(ventanaComida, 'Comida',179)

    botonCena= tipoBoton1(ventanaCena, 'Cena',220)

    botonAtras(ventanaHacerReceta)
#________________________________________VENTANA BUSCAR RECETA _________________________________________________________

def ventanaBebida(event=None):

    limpiarVentana()

    etiquetaBuscarReceta= tipoEtiqueta1("Buscar receta")

    botonPanteraRosa= tipoBoton1(ventanaPorpasos,'Pantera rosa',100)

    botonAtras(ventanaTipo)

def ventanaSnack(event=None):

    limpiarVentana()

    etiquetaBuscarReceta= tipoEtiqueta1("Buscar receta")

    botonPaletaAmarilla= tipoBoton5(ventanaPorpasos2,'Paleta amarilla',100,16)

    botonAtras(ventanaTipo)

def ventanaDesayuno(event=None):

    limpiarVentana()

    etiquetaBuscarReceta= tipoEtiqueta1("Buscar receta")

    botonPizzaPortobello= tipoBoton4(ventanaPorpasos3,'Pizza Portobello',93)

    botonAtras(ventanaTipo)

def ventanaComida(event=None):

    limpiarVentana()

    etiquetaBuscarReceta= tipoEtiqueta1("Buscar receta")

    botonSpaguetti= tipoBoton1(ventanaPorpasos4, 'Spaguetti',100)

    botonAtras(ventanaTipo)

def ventanaCena(event=None):

    limpiarVentana()

    etiquetaBuscarReceta= tipoEtiqueta1("Buscar receta")

    botonClubSandwich= tipoBoton4(ventanaPorpasos5, 'Club Sandwich', 93)

    botonAtras(ventanaTipo)

#________________________________________RECETA POR PASOS_______________________________________________________________

def ventanaPorpasos(event=None):

    limpiarVentana()

    etiquetaPanteraRosa= tipoEtiqueta3("Pantera rosa",tipoFuente1, 15,15)

    etiquetaIngredientes= tipoEtiqueta3("Para empezar, necesitamos:",tipoFuente2,18,18)

    etiquetaIngredientes= tipoEtiqueta3("2 fresas, 1 tz de leche, 1 cda de azúcar",tipoFuente2, 20,20)

    botonSiguiente(ventanaPaso1)

    botonAtras(ventanaBebida)

def ventanaPorpasos2(event=None):

    limpiarVentana()

    etiquetaPaletaAmarilla= tipoEtiqueta3("Paleta amarilla",tipoFuente1,15,15)

    etiquetaIngredientes= tipoEtiqueta3("Para empezar, necesitamos:",tipoFuente2,18,18)

    etiquetaIngredientes= tipoEtiqueta3("1 vaso, 1 tz de piña, 1 cda de azúcar",tipoFuente2,20,20)

    etiquetaIngredientes= tipoEtiqueta3("y un palo de madera",tipoFuente2,20,20)

    botonSiguiente(ventanaPaso1_2)

    botonAtras(ventanaSnack)

def ventanaPorpasos3(event=None):

    limpiarVentana()

    etiquetaPizzaPortobello= tipoEtiqueta3("Pizza Portobello",tipoFuente1,15,15)

    etiquetaIngredientes= tipoEtiqueta3("Para empezar, necesitamos:",tipoFuente2,18,18)

    etiquetaIngredientes= tipoEtiqueta3("1 pza portobelo, 20 g de queso, 5 g de sal",tipoFuente2,20,20)

    etiquetaIngredientes= tipoEtiqueta3("4 rebandas salchicha",tipoFuente2,20,20)

    botonSiguiente(ventanaPaso1_3)

    botonAtras(ventanaDesayuno)

def ventanaPorpasos4(event=None):

    limpiarVentana()

    etiquetaSpaguetti= tipoEtiqueta3("Spaguetti",tipoFuente1,14,14)

    etiquetaIngredientes= tipoEtiqueta3("Para empezar, necesitamos:",tipoFuente2,15,15)

    etiquetaIngredientes= tipoEtiqueta3("1 paquete de spaguetti, 5 g de sal",tipoFuente2,16,16)

    etiquetaIngredientes= tipoEtiqueta3("1 tza de salsa de tomate, 1 L de agua",tipoFuente2,16,16)

    etiquetaIngredientes= tipoEtiqueta3("y 20 g de queso",tipoFuente2,16,16)

    botonSiguiente(ventanaPaso1_4)

    botonAtras(ventanaComida)

def ventanaPorpasos5(event=None):

    limpiarVentana()

    etiquetaClubSandwich= tipoEtiqueta3("Club Sandwich",tipoFuente1,15,15)

    etiquetaIngredientes= tipoEtiqueta3("Para empezar, necesitamos:",tipoFuente2,18,18)

    etiquetaIngredientes= tipoEtiqueta3("2 pza pan, 1 rebanada de queso",tipoFuente2,20,20)

    etiquetaIngredientes= tipoEtiqueta3("1 cda de aderezo y 1 rebanda de jamón.",tipoFuente2,20,20)

    botonSiguiente(ventanaPaso1_5)

    botonAtras(ventanaCena)

#________________________________________PASO 1_________________________________________________________________________

def ventanaPaso1(event=None):

    limpiarVentana()

    etiquetaPaso1= tipoEtiqueta3("Paso 1",tipoFuente1,15,15)

    etiquetaPasos= tipoEtiqueta3("Con ayuda de un adulto:",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("Vierte los ingredientes en una licuadora.",tipoFuente3,16,16)

    etiquetaPasos= tipoEtiqueta3("Espera hasta que la bebida sea color ROSA.",tipoFuente3,18,18)

    botonSiguiente(ventanaDato)

    botonAtras(ventanaPorpasos)

def ventanaPaso1_2(event=None):

    limpiarVentana()

    etiquetaPaso1= tipoEtiqueta3("Paso 1",tipoFuente1,14,14)

    etiquetaPasos= tipoEtiqueta3("Con ayuda de un adulto:",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("Vierte los ingredientes en una licuadora.",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("Espera hasta que la bebida sea color",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("AMARILLO. Despues, sirve y congela.",tipoFuente3,15,15)

    botonSiguiente(ventanaDato_2)

    botonAtras(ventanaPorpasos2)

def ventanaPaso1_3(event=None):

    limpiarVentana()

    etiquetaPaso1= tipoEtiqueta3("Paso 1",tipoFuente1,13,13)

    etiquetaPasos= tipoEtiqueta3("Con ayuda de un adulto:",tipoFuente3,14,14)

    etiquetaPasos= tipoEtiqueta3("Agrega la salsa en el portobleo.",tipoFuente3,14,14)

    etiquetaPasos= tipoEtiqueta3("Despúes, añade el queso y la salchicha.",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("Calienta hasta que el queso se derrita.",tipoFuente3, 15, 15)

    botonSiguiente(ventanaDato_3)

    botonAtras(ventanaPorpasos3)

def ventanaPaso1_4(event=None):

    limpiarVentana()

    etiquetaPaso1= tipoEtiqueta3("Paso 1",tipoFuente1,13,13)

    etiquetaPasos= tipoEtiqueta3("Con ayuda de un adulto:",tipoFuente3,14,14)

    etiquetaPasos= tipoEtiqueta3("En una olla, hierve el agua.",tipoFuente3,14,14)

    etiquetaPasos= tipoEtiqueta3("Despúes, añade la pasta y la sal.",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("Añade la salsa y el queso y calienta.",tipoFuente3, 15, 15)

    botonSiguiente(ventanaDato_4)

    botonAtras(ventanaPorpasos4)

def ventanaPaso1_5(event=None):

    limpiarVentana()

    etiquetaPaso1= tipoEtiqueta3("Paso 1",tipoFuente1,15,15)

    etiquetaPasos= tipoEtiqueta3("Con ayuda de un adulto:",tipoFuente3,15,15)

    etiquetaPasos= tipoEtiqueta3("Unta el aderezo en ambas piezas de pan.",tipoFuente3,16,16)

    etiquetaPasos= tipoEtiqueta3("Sobre una de ellas, pon el jamón y el queso.",tipoFuente3,18,18)

    botonSiguiente(ventanaDato_5)

    botonAtras(ventanaPorpasos5)
#________________________________________DATO___________________________________________________________________________

def ventanaDato(event=None):

    limpiarVentana()

    etiquetaExcelente= tipoEtiqueta3("¡Excelente!",tipoFuente1,15,15)

    etiquetaSabiasQue= tipoEtiqueta3("¿Sabias qué?",tipoFuente3,15,15)

    etiquetaTexto= tipoEtiqueta3("Esta bebida es una mezcla homogenea.",tipoFuente3,16,16)

    etiquetaTexto= tipoEtiqueta3("Ya que se trituran muy bien sus ingredientes.",tipoFuente3,18,18)

    botonSiguiente(ventanaFin)

    botonAtras(ventanaPaso1)

def ventanaDato_2(event=None):

    limpiarVentana()

    etiquetaExcelente= tipoEtiqueta3("¡Excelente!",tipoFuente1,14,14)

    etiquetaSabiasQue= tipoEtiqueta3("¿Sabias qué?",tipoFuente3,15,15)

    etiquetaTexto= tipoEtiqueta3("Cuando se expone un líquido",tipoFuente3,15,15)

    etiquetaTexto= tipoEtiqueta3("a bajas temperaturas;",tipoFuente3,15,15)

    etiquetaTexto= tipoEtiqueta3("cambia de estado líquido a sólido.",tipoFuente3, 15, 15)

    botonSiguiente(ventanaFin_2)

    botonAtras(ventanaPaso1_2)

def ventanaDato_3(event=None):

    limpiarVentana()

    etiquetaExcelente= tipoEtiqueta3("¡Excelente!",tipoFuente1,15,15)

    etiquetaSabiasQue= tipoEtiqueta3("¿Sabias qué?",tipoFuente3,15,15)

    etiquetaDato= tipoEtiqueta3("Para preparar 2 pizzas necesitas",tipoFuente3,16,16)

    etiquetaDato= tipoEtiqueta3("10 g de NACl.",tipoFuente3,18,18)

    botonSiguiente(ventanaFin_3)

    botonAtras(ventanaPaso1_3)

def ventanaDato_4(event=None):

    limpiarVentana()

    etiquetaExcelente= tipoEtiqueta3("¡Excelente!",tipoFuente1,15,15)

    etiquetaSabiasQue= tipoEtiqueta3("¿Sabias qué?",tipoFuente3,15,15)

    etiquetaDato= tipoEtiqueta3("Cuando el agua hierve presenta burbujas.",tipoFuente3,16,16)

    etiquetaDato= tipoEtiqueta3("Estas, se llaman nucleos de ebullición.",tipoFuente3,18,18)

    botonSiguiente(ventanaFin_4)

    botonAtras(ventanaPaso1_4)

def ventanaDato_5(event=None):

    limpiarVentana()

    etiquetaExcelente= tipoEtiqueta3("¡Excelente!",tipoFuente1,15,15)

    etiquetaSabiasQue= tipoEtiqueta3("¿Sabias qué?",tipoFuente3,15,15)

    etiquetaDato= tipoEtiqueta3("Para que el pan este esponjoso.",tipoFuente3,16,16)

    etiquetaDato= tipoEtiqueta3("Se le añade polvo para hornear.",tipoFuente3,18,18)

    botonSiguiente(ventanaFin_5)

    botonAtras(ventanaPaso1_5)
#________________________________________FIN____________________________________________________________________________

def ventanaFin(event=None):

    limpiarVentana()

    etiquetaSirve= tipoEtiqueta3("¡Sirve y a disfrutar!",tipoFuente1,15,15)

    etiquetaComentarios= tipoEtiqueta3("Puedes decorar tu bebida,",tipoFuente3,15,15)

    etiquetaComentarios= tipoEtiqueta3("para disfrutarla a tu estilo.",tipoFuente3,16,16)

    botonVolverCocinar(ventanaHacerReceta)

    botonAtras(ventanaDato)

def ventanaFin_2(event=None):

    limpiarVentana()

    etiquetaADisfrutar= tipoEtiqueta3("¡A disfrutar!",tipoFuente1,15,15)

    etiquetaComentarios= tipoEtiqueta3("Decorar tu paleta antes de que se derrita,",tipoFuente3,15,15)

    etiquetaComentarios= tipoEtiqueta3("para disfrutarla a tu estilo.",tipoFuente3,16,16)

    botonVolverCocinar(ventanaHacerReceta)

    botonAtras(ventanaDato_2)

def ventanaFin_3(event=None):

    limpiarVentana()

    etiquetaADisfrutar= tipoEtiqueta3("¡Sirve y a disfrutar!",tipoFuente1,15,15)

    etiquetaComentarios= tipoEtiqueta3("Añade algun aderezo o salsa,",tipoFuente3,15,15)

    etiquetaComentarios= tipoEtiqueta3("para acompañar.",tipoFuente3,16,16)

    botonVolverCocinar(ventanaHacerReceta)

    botonAtras(ventanaDato_3)

def ventanaFin_4(event=None):

    limpiarVentana()

    etiquetaADisfrutar= tipoEtiqueta3("¡A disfrutar!",tipoFuente1,15,15)

    etiquetaComentarios= tipoEtiqueta3("Añade algun aderezo o salsa,",tipoFuente3,15,15)

    etiquetaComentarios= tipoEtiqueta3("para acompañar.",tipoFuente3,16,16)

    botonVolverCocinar(ventanaHacerReceta)

    botonAtras(ventanaDato_4)

def ventanaFin_5(event=None):

    limpiarVentana()

    etiquetaADisfrutar= tipoEtiqueta3("¡A disfrutar!",tipoFuente1,15,15)

    etiquetaComentarios= tipoEtiqueta3("Puedes partir el sandwich por mitad,",tipoFuente3,15,15)

    etiquetaComentarios= tipoEtiqueta3("y agregar alguna salsa ",tipoFuente3,16,16)

    etiquetaComentarios= tipoEtiqueta3("para disfrutarla a tu estilo.",tipoFuente3,16,16)

    botonVolverCocinar(ventanaHacerReceta)

    botonAtras(ventanaDato_5)
#________________________________________RECETA ALEATORIA_______________________________________________________________

def ventanaReestriccionesAleatoria(event=None):

    limpiarVentana()

    etiquetaAtencion= tipoEtiqueta3("¡ATENCION!",tipoFuente1,13,13)

    etiquetaReestriccion= tipoEtiqueta3("Si quieres mas recetas",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3("puedes agregarlas en",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3('el modulo de "Recetario".',tipoFuente3,15,15)

    etiquetaReestriccion= tipoEtiqueta3("",tipoFuente3,15,15)

    botonRecetaAleatoria= Button(Frame, command=ventanaAleatoria, text='Receta aleatoria', font=tipoFuente2,fg="white", bg="green")
    botonRecetaAleatoria.place(x=170, y=280)
    botonRecetaAleatoria.config(width=15, height=1)

    botonAtras(ventanaHacerReceta)

def ventanaAleatoria(event=None):
    #no se llamo a la funcion clearwin para que siguiera presente el menu
    #limpiarVentana()

    ventana = tk.Tk()
    ventana.title("Recetario Inteligente")
    ventana.resizable(0, 0)
    ventana.geometry('338x334')
    ventana.iconbitmap('estufa.ico')

    frame = tk.Frame(ventana, pady=10, padx=10)
    frame.grid(row=0, column=0, sticky="nsew")

    text = tk.Text(frame, width=31, height=15, font=("Arial", 12))
    text.grid(row=0, column=0, rowspan=6, columnspan=2, pady=5, padx=5)
    scrollbar = tk.Scrollbar(frame, command=text.yview)
    text['yscroll'] = scrollbar.set
    scrollbar.grid(row=0, column=2, rowspan=6, sticky="ns")

    quote = funcionesGui.recetaAprenderAleatoria()

    text.insert(tk.INSERT, quote)
#___________________________________________________Menu________________________________________________________________

def ventanaReestriccionesMenu(event=None):

    limpiarVentana()

    etiquetaAtencion= tipoEtiqueta3("¡ATENCION!",tipoFuente1,13,13)

    etiquetaReestriccion= tipoEtiqueta3("Si quieres mas recetas",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3("puedes agregarlas en",tipoFuente3,14,14)

    etiquetaReestriccion= tipoEtiqueta3('el modulo de "Recetario".',tipoFuente3,15,15)

    etiquetaReestriccion= tipoEtiqueta3("",tipoFuente3,15,15)

    botonRecetaAleatoria= Button(Frame, command=ventanaMenu, text='Menú aleatorio', font=tipoFuente2,fg="white", bg="green")
    botonRecetaAleatoria.place(x=170, y=280)
    botonRecetaAleatoria.config(width=15, height=1)

    botonAtras(ventanaCocinar)

def ventanaMenu(event=None):
    #no se llamo a la funcion clearwin para que siguiera presente el menu
    #limpiarVentana()

    ventana = tk.Tk()
    ventana.title("Recetario Inteligente")
    ventana.resizable(0, 0)
    ventana.geometry('338x334')
    ventana.iconbitmap('estufa.ico')

    frame = tk.Frame(ventana, pady=10, padx=10)
    frame.grid(row=0, column=0, sticky="nsew")

    text = tk.Text(frame, width=31, height=15, font=("Arial", 12))
    text.grid(row=0, column=0, rowspan=6, columnspan=2, pady=5, padx=5)
    scrollbar = tk.Scrollbar(frame, command=text.yview)
    text['yscroll'] = scrollbar.set
    scrollbar.grid(row=0, column=2, rowspan=6, sticky="ns")

    quote = funcionesGui.recetaCocinarAleatoria()

    text.insert(tk.INSERT, quote)
#________________________________________TIPO DE JUEGO__________________________________________________________________

def ventanaJugar(event=None):

    limpiarVentana()

    etiquetaJugar= tipoEtiqueta1("Jugar")

    botonConversiones= tipoBoton1(ventanaJugarConver,'Conversiones',100)

    botonReacciones= tipoBoton1(ventanaJugarReac,'Reacciones',140)

    botonAtras(ventanaAprender)
#________________________________________CATEGORIA CONVERSIONES_________________________________________________________

def ventanaJugarConver(event=None):

    limpiarVentana()

    etiquetaJugar= tipoEtiqueta1("Jugar")

    botonMaestro= tipoBoton1(ventanaJugarMtroConver,'Maestro',100)

    botonJunior= tipoBoton1(ventanaJugarJrConver,'Junior',140)

    botonAtras(ventanaJugar)
#_______________________________________Empezar a Jugar conversioes Junior______________________________________________

def ventanaJugarJrConver(event=None):

    limpiarVentana()

    etiquetaConversiones= tipoEtiqueta3("Conversiones Jr",tipoFuente1,15,15)

    etiquetaInstruccion= tipoEtiqueta3("Este juego consta de 3 preguntas. Elige",tipoFuente3,15,15)

    etiquetaInstruccion= tipoEtiqueta3("una respuesta y presiona siguiente para seguir.",tipoFuente3,16,16)

    etiquetaInstruccion= tipoEtiqueta3("Para volver a jugar, presiona volver a jugar.",tipoFuente3,18,18)

    botonAtras(ventanaJugarConver)

    os.system("FUNCION3.py")
#_______________________________________Empezar a Jugar conversiones Maestro______________________________________________

def ventanaJugarMtroConver(event=None):

    limpiarVentana()

    etiquetaConversiones= tipoEtiqueta3("Conversiones Maestro", tipoFuente1, 15, 15)

    etiquetaInstruccion= tipoEtiqueta3("Este juego consta de 3 preguntas. Elige", tipoFuente3, 15, 15)

    etiquetaInstruccion= tipoEtiqueta3("una respuesta y presiona siguiente para seguir.", tipoFuente3, 16, 16)

    etiquetaInstruccion= tipoEtiqueta3("Para volver a jugar, presiona volver a jugar.", tipoFuente3, 18, 18)

    botonAtras(ventanaJugarConver)

    os.system("FUNCION4.py")
#_____________________________________________CATEGORIA REACCIONES______________________________________________________

def ventanaJugarReac(event=None):

    limpiarVentana()

    etiquetaJugar= tipoEtiqueta1("Jugar")

    botonMaestro= tipoBoton1(ventanaJugarMtroReac, 'Maestro',100)

    botonJunior= tipoBoton1(ventanaJugarJrReac, 'Junior',140)

    botonAtras(ventanaJugar)
#_______________________________________Empezar a Jugar reacciones Junior_______________________________________________

def ventanaJugarJrReac(event=None):

    limpiarVentana()

    etiquetaReacciones= tipoEtiqueta3("Reacciones Jr", tipoFuente1, 15, 15)

    etiquetaInstruccion= tipoEtiqueta3("Este juego consta de 3 preguntas. Elige", tipoFuente3, 15, 15)

    etiquetaInstruccion= tipoEtiqueta3("una respuesta y presiona siguiente para seguir.", tipoFuente3, 16, 16)

    etiquetaInstruccion= tipoEtiqueta3("Para volver a jugar, presiona volver a jugar.", tipoFuente3, 18, 18)

    botonAtras(ventanaJugarReac)

    os.system("FUNCION1.py")
#_______________________________________Empezar a Jugar reacciones Maestro______________________________________________

def ventanaJugarMtroReac(event=None):

    limpiarVentana()

    etiquetaReacciones = tipoEtiqueta3("Reacciones Maestro", tipoFuente1, 15, 15)

    etiquetaInstruccion= tipoEtiqueta3("Este juego consta de 3 preguntas. Elige", tipoFuente3, 15, 15)

    etiquetaInstruccion= tipoEtiqueta3("una respuesta y presiona siguiente para seguir.", tipoFuente3, 16, 16)

    etiquetaInstruccion= tipoEtiqueta3("Para volver a jugar, presiona volver a jugar.", tipoFuente3, 18, 18)

    botonAtras(ventanaJugarReac)

    os.system("FUNCION2.py")
#_______________________________________________________________________________________________________________________

ventanaPrincipal()
raiz.mainloop()