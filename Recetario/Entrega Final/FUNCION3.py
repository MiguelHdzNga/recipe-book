#CUESTIONARIO CONVERSIONES JUNIOR

import random
from tkinter import*
from tkinter.font import Font

ventana = Tk()
ventana.title("Recetario Inteligente")
ventana.geometry("998x334")
ventana.config(bg='white smoke')
ventana.iconbitmap('estufa.ico')
ventana.resizable(0,0)

fuente= Font (family="Arial",size=12)
#_____________________________________________LISTA DE PREGUNTAS________________________________________________________

preguntas= [["1 pizza se prepara con 1 g de sal, ¿Cuántos g necesito para 2 pizzas?", "10 g", "1 g", "2 g"]]
preguntas.append(["1 pastel  se prepara con 2 cucharadas de aceite, ¿Cuántas cucharadas necesito para 2 pasteles?", "2", "3", "4"])
preguntas.append(["¿1 Kg + 5 Kg?", "3", "2", "6"])
preguntas.append(["¿20 g + 5 g?", "19", "30", "25"])
preguntas.append(["Una malteada se prepara con 10 mL de nieve, ¿Cuántos mL necesito para 2 malteadas? ", "12", "34", "20"])
preguntas.append(["Para 1 volcan de queso se agregan 2 g de sal, ¿Cuántos g necesito para 3 volcanes? ", "1", "2", "4"])

#___________________________________________________TEXTO_______________________________________________________________

def preguntaVentana(textopregunta):
    preguntaEnVentana= Text(ventana, font=("Arial", 12), width=80, height=1)
    preguntaEnVentana.insert(END, textopregunta)
    preguntaEnVentana.grid(column=0, row=0, padx=135, pady=(75, 0))

#__________________________________________________BOTONES______________________________________________________________

def volverJugar():
    volver= Button(ventana, text="Volver a Jugar", font=fuente, command=menuCreator)
    volver.grid(column=0, row=1)

def tipoBoton():
    Button(ventana, text="", font=fuente)
#__________________________________________FUNCION LIMPIAR VENTANA______________________________________________________

def limpiar():

    for child in ventana.grid_slaves():
        child.destroy()
#__________________________________________________CLASE________________________________________________________________

class JuegoPreguntas:
    def __init__(self,buscar):
        limpiar()
        self.pregunta=[]
        for n in buscar:
            self.pregunta.append(n)
        self.respuesta1=""
        self.respuesta2=""
        self.respuesta3=""
        self.respuesta=""
        self.respuestaBoton= tipoBoton()
        self.respuesta1= tipoBoton()
        self.respuesta2= tipoBoton()
        self.respuesta3= tipoBoton()
        self.lock=False
        self.right=0
        self.siguiente= Button(ventana,text="Siguiente",font=fuente,command=self.preguntar)
        self.numero=0
        self.MaxPreguntas=3
        self.preguntar()

#__________________________________________________________FUNCION PREGUNTAS____________________________________________

    def preguntar(self):
        self.siguiente.grid(column=0, row=5, pady=5)
        if len(self.pregunta) > 0 and self.numero < self.MaxPreguntas:
            self.numero += 1
            self.lock= False
            numeroAleatorio= random.randint(0, len(self.pregunta)-1)
            textoPregunta= self.pregunta[numeroAleatorio][0]
            self.respuesta= self.pregunta[numeroAleatorio][-1]
            respuestas= []
            for i in range(1,4):
                respuestas.append(self.pregunta[numeroAleatorio][i])
            random.shuffle(respuestas)

            self.respuesta1= respuestas[0]
            self.respuesta2= respuestas[1]
            self.respuesta3= respuestas[2]

            pregunta= preguntaVentana(textoPregunta)

            self.botonRespuesta1 = Button(ventana, text=self.respuesta1, font=fuente, width=19, command=self.resultado1)
            self.botonRespuesta1.grid(column=0, row=1, pady=(8, 5))

            self.botonRespuesta2 = Button(ventana, text=self.respuesta2, font=fuente, width=19, command=self.resultado2)
            self.botonRespuesta2.grid(column=0, row=2, pady=5)

            self.botonRespuesta3 = Button(ventana, text=self.respuesta3, font=fuente, width=19, command=self.resultado3)
            self.botonRespuesta3.grid(column=0, row=3, pady=5)


            if self.respuesta1 == self.respuesta:
                self.respuestaCorrecta = self.botonRespuesta1
            elif self.respuesta2 == self.respuesta:
                self.respuestaCorrecta = self.botonRespuesta2
            elif self.respuesta3 == self.respuesta:
                self.respuestaCorrecta = self.botonRespuesta3

            self.pregunta.pop(numeroAleatorio)
        else:
            limpiar()
            etiquetaResultados= Label(ventana, text=" Acertaste " + str(self.right) + " de " + str(self.MaxPreguntas) + " ¡Puedes hacerlo MEJOR!",font=("Arial",12))
            etiquetaResultados.grid(column=0, row=0, padx=355, pady=(100, 15))
            volverJugar()

#____________________________________________________FUNCION RESULTADOS_________________________________________________

    def resultado1(self):
        if self.lock == False:
            if self.respuesta != self.respuesta1:
                self.botonRespuesta1.configure(bg="red")
            else:
                self.botonRespuesta1.configure(bg="green")
                self.right += 1
            self.respuestaCorrecta.configure(bg="green")
            self.lock = True

    def resultado2(self):
        if self.lock == False:
            if self.respuesta != self.respuesta2:
                self.botonRespuesta2.configure(bg="red")
            else:
                self.botonRespuesta2.configure(bg="green")
                self.right += 1
            self.respuestaCorrecta.configure(bg="green")
            self.lock = True

    def resultado3(self):
        if self.lock == False:
            if self.respuesta != self.respuesta3:
                self.botonRespuesta3.configure(bg="red")
            else:
                self.botonRespuesta3.configure(bg="green")
                self.right += 1
            self.respuestaCorrecta.configure(bg="green")
            self.lock = True

#___________________________________________________CLASE_______________________________________________________________

class Menu:
    def __init__(self):
        limpiar()
        self.QuizJ=Button(ventana, text="Empezar", font=fuente,command=CreadorQuiz,width=20, height=2)
        self.QuizJ.grid(column=0,row=0,padx=400, pady=200)

#________________________________________FUNCIONES QUE CREAN EL JUEGO___________________________________________________

def menuCreator():
    m=Menu()

def CreadorQuiz():
    q=JuegoPreguntas(preguntas)

menuCreator()
ventana.mainloop()
