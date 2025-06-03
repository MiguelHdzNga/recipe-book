import json
import os
import random
import datetime as date

def crear_receta(tipo,nombre,ingredientes,procedimiento):
    receta = {}
    receta['Nombre'] = nombre.title().strip()
    receta['Ingredientes'] = ingredientes.split(';')
    receta['Procedimiento'] = procedimiento.split(';')
    j = json.dumps(receta, indent=4)
    with open(
            os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Recetario', tipo,
                         receta['Nombre']) + ".txt",
            "w") as f:
        f.write(j)
    print('Receta Agregada')

def instalacion ():
    folderPrincipal = 'Recetario Inteligente DB'
    folderRecetario = 'Recetario'
    folderModo = ['Normal','Aprender']
    folderPrincipalPath = os.path.join(os.getcwd(),folderPrincipal)
    if not os.path.exists(folderPrincipalPath):
        for i in folderModo:
            folderModoTipoPath = os.path.join(folderPrincipalPath,folderRecetario,i)
            os.makedirs(folderModoTipoPath)
            folderHistorial = os.path.join(folderPrincipalPath,'Historial',i,'Recetas Usadas')
            os.makedirs(folderHistorial)
        print('Instalacion Terminada')
def recetaAprenderAleatoria():
    #asignacion de rutas
    rutaHistorial = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial','Aprender', 'Recetas usadas')
    rutaRecetario = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Recetario', 'Aprender')
    #validacion de recetas
    if os.listdir(rutaRecetario) == []:
        recetastr = '!!! RECETARIO VACIO !!! \n\n !!! FAVOR DE AGREGAR TUS \nRECETAS EN EL MODULO \nRECETARIO!!!'
    else:
        #receta aleatoria
        recetasHistorial = os.listdir(rutaHistorial)
        recetasDB = os.listdir(rutaRecetario)
        # reiniciar contador de recetas usadas
        if sorted(os.listdir(rutaHistorial)) == sorted(os.listdir(rutaRecetario)):
            for i in os.listdir(rutaRecetario):
                os.remove(os.path.join(rutaHistorial, i))
        #comparacion de Historial vs Recetario
        for i in recetasHistorial:
            recetasDB.remove(i)
        aleatorio = random.randint(0, (len(recetasDB) - 1))
        NombreReceta = recetasDB[aleatorio]
        #receta aleatoria seleccionada
        receta = os.path.join(rutaRecetario, NombreReceta)
        with open(receta) as f:
            json_string = f.read()
            data = json.loads(json_string)
        j = json.dumps(data, indent=4)
        #agregar receta al Historial
        with open((rutaHistorial + '\\' + data['Nombre'] + ".txt"), "w") as f:
            f.write(j)
        #reiniciar contador de recetas usadas
        if sorted(os.listdir(rutaHistorial)) == sorted(os.listdir(rutaRecetario)):
            for i in os.listdir(rutaRecetario):
                os.remove(os.path.join(rutaHistorial, i))
        #conversion del diccionario a string
        nombre = data['Nombre']
        listaIng = data['Ingredientes']
        listaPro = data['Procedimiento']
        recetastr = nombre + '\n\n' + 'Ingredientes:\n\n'
        for i in range(len(listaIng)):
            recetastr = recetastr + '- ' + listaIng[i] + '\n\n'
        recetastr = recetastr + 'Elaboracion:\n\n' + 'CON AYUDA DE UN ADULTO:\n\n'
        for i in range(len(listaPro)):
            recetastr = recetastr + str(i + 1) + '.- ' + listaPro[i] + '\n\n'
        recetastr = recetastr + 'A DISFRUTAR!'
    return recetastr

def recetaCocinarAleatoria():
    #creacion de contadores y rutas
    menu = ''
    listaIngTotal = []
    rutaHistorial = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial', 'Normal', 'Recetas usadas')
    rutaRecetario = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Recetario', 'Normal')
    #validacion de Recetas agregadas
    if len(os.listdir(rutaRecetario)) < 3:
        menu = '!!! RECETARIO VACIO O \nINSUFICIENTE !!! \n\n !!! FAVOR DE AGREGAR TUS \nRECETAS EN EL MODULO \nRECETARIO!!!'
    else:
        #seleccion de 3 recetas aleatorias
        for numRecetas in range(1,4):
            menu = menu +'Receta ' + str(numRecetas) + '\n\n'
            recetasHistorial = os.listdir(rutaHistorial)
            recetasDB = os.listdir(rutaRecetario)
            #comparacion de Historial vs Recetario
            for i in recetasHistorial:
                recetasDB.remove(i)
            aleatorio = random.randint(0, (len(recetasDB) - 1))
            NombreReceta = recetasDB[aleatorio]
            # receta aleatoria seleccionada
            receta = os.path.join(rutaRecetario, NombreReceta)
            with open(receta) as f:
                json_string = f.read()
                data = json.loads(json_string)
            j = json.dumps(data, indent=4)
            # agregar receta al Historial
            with open((rutaHistorial + '\\' + data['Nombre'] + ".txt"), "w") as f:
                f.write(j)
            #reiniciar contador de recetas usadas
            if sorted(os.listdir(rutaHistorial)) == sorted(os.listdir(rutaRecetario)):
                for i in os.listdir(rutaRecetario):
                    os.remove(os.path.join(rutaHistorial, i))
            #conversion del diccionario a string
            nombre = data['Nombre']
            listaIng = data['Ingredientes']
            listaPro = data['Procedimiento']
            listaIngTotal.extend(listaIng)
            recetastr = nombre + '\n\n' + 'Ingredientes:\n\n'
            for i in range(len(listaIng)):
                recetastr = recetastr + '- ' + listaIng[i] + '\n\n'
            recetastr = recetastr + 'Procedimiento:\n\n'
            for i in range(len(listaPro)):
                recetastr = recetastr + str(i + 1) + '.- ' + listaPro[i] + '\n\n'
            recetastr = recetastr + 'A DISFRUTAR!\n\n'
            menu = menu + recetastr
        #creacion de la lista de ingredientes
        menu = menu + 'Lista de Ingredientes:\n\n'
        for i in sorted(listaIngTotal):
            menu = menu + '- ' + i +'\n\n'
        rutaHistorial = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial', 'Normal')
        fecha = str(date.date.today())
        with open(os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial','Normal', fecha + ".txt"), "w") as f:
            f.write(menu)

        print("Menu Creado")
    return menu
