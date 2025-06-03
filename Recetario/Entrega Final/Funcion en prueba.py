import random
import os
import json
import datetime as date



def recetaCocinarAleatoria():
    menu = ''
    listaIngTotal = []
    for numRecetas in range(1,4):
        menu = menu +'Receta ' + str(numRecetas) + '\n\n'
        rutaHistorial = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial','Normal', 'Recetas usadas')
        rutaRecetario = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Recetario', 'Normal')

        recetasHistorial = os.listdir(rutaHistorial)
        recetasDB = os.listdir(rutaRecetario)
        if sorted(os.listdir(rutaHistorial)) == sorted(os.listdir(rutaRecetario)):
            for i in os.listdir(rutaRecetario):
                os.remove(os.path.join(rutaHistorial, i))
        for i in recetasHistorial:
            recetasDB.remove(i)


        aleatorio = random.randint(0, (len(recetasDB) - 1))
        NombreReceta = recetasDB[aleatorio]

        receta = os.path.join(rutaRecetario, NombreReceta)

        with open(receta) as f:
            json_string = f.read()
            data = json.loads(json_string)
        j = json.dumps(data, indent=4)
        with open((rutaHistorial + '\\' + data['Nombre'] + ".txt"), "w") as f:
            f.write(j)
        # eliminar Conteo de recetas
        if sorted(os.listdir(rutaHistorial)) == sorted(os.listdir(rutaRecetario)):
            for i in os.listdir(rutaRecetario):
                os.remove(os.path.join(rutaHistorial, i))


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

    menu = menu + 'Lista de Ingredientes:\n\n'
    for i in sorted(listaIngTotal):
        menu = menu + '- ' + i +'\n\n'
    rutaHistorial = os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial', 'Normal')
    fecha = str(date.date.today())
    with open(os.path.join(os.getcwd(), 'Recetario Inteligente DB', 'Historial','Normal', fecha + ".txt"), "w") as f:
        f.write(menu)

    print("Menu Creado")
    return menu



# receta = recetaCocinarAleatoria()
# print(receta)