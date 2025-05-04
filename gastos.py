'''
Fundamentos de Programación Imperativa
Nombre y código del autor:

Juan Manuel Moreno Murillo - 2360225
Wilmer Yulian Ulcue Velasco - 2360286
Nicoll Tatiana Vergara Echeverri - 2360385
Juan Carlos Villa Gallego - 2360311

Fecha de realización: 25/Junio/2023

'''
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================


# Proposito: Calcula y almacena y retorna una matriz c llena con los datos de los gastos de cada familia en pan, agua y leche
#                                                                               para cada años de 2017-2020                                   
# Contrato: gastos(entero[],entero[],entero[])--> entero[]
# Ejemplo: gastos([[450, 800, 650],[500, 810, 620], [200, 500, 600]],
#               [[200, 300, 500, 550], [300, 250, 400, 500], [1000, 1500, 1800, 2000]]
#                 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] ) --> 
# Encabezado: gastos(a,b,c)-->

def gastos(a,b,c):
    i = 0
    while i < 3:
        j = 0
        while j < 4:
            c[i][j] = a[i][0]*b[0][j] + a[i][1]*b[1][j] + a[i][2]*b[2][j]
            j += 1
        i += 1


# Proposito: recibe la matriz c y retorna un informe con los gastos de cada familia en 
#                                                       pan, agua y leche bien organizados        
# Contrato: informe(entero[])-->str
# Ejemplo: informe([[980000, 1310000, 1715000, 1947500], [963000, 1282500, 1690000, 1920000], [790000, 1085000, 1380000, 1560000]])-->	    2017    2018      2019    2020
#
#                                                                                                                               Familia1   980000   1310000  1715000  1947500	
#
#                                                                                                                               Familia2   963000   1282500  1690000  1920000	
#                                                                                                                                            
#                                                                                                                               Familia3   790000   1085000  1380000  1560000	
# Encabezado: informe(c)--> orden C



def informe(c):
    ordenC = "\t    2017\t2018\t2019\t2020\n"
    i = 0
    while i < 3:
        ordenC += '\nFamilia'+str(i+1)+'   '
        j = 0
        while j < 4:
            ordenC = ordenC + str(c[i][j])+"\t"
            j += 1
        ordenC = ordenC + "\n"
        i += 1
        
    return ordenC


# Proposito: Recibe la matriz c y un numero ente 1 y 3(la familia) y con ello genera un informe con los gastos de esa familia entre 2017-2020
# Contrato: gastosFamilia(entero[],entero)--> str
# Ejemplo: gastosFamilia([[980000, 1310000, 1715000, 1947500], [963000, 1282500, 1690000, 1920000], [790000, 1085000, 1380000, 1560000]], 2)-->Gastos de la Familia 2 fueron: 
#                                                                                                                                               2017 : 
#                                                                                                                                               963000
#                                                                                                                                               2018 : 
#                                                                                                                                               1282500
#                                                                                                                                               2019 : 
#                                                                                                                                               1690000
#                                                                                                                                               2020 : 
#                                                                                                                                               1920000
# Encabezado: gastosFamilia(c, familia)--> gastos



def gastosFamilia(c, familia):
    inFamilia = familia - 1
    gastos = ("2017 : "+"\n"+str(c[inFamilia][0])+"\n"+"2018 : "+"\n"+str(c[inFamilia][1])+"\n"+"2019 : "+"\n"+str(c[inFamilia][2])+"\n"+"2020 : "+"\n"+str(c[inFamilia][3]))
    return gastos



# Proposito: Genera un informe con los gastos de las 3 familias en el año escogido entre 2017-2020
# Contrato: gastosAño(entero[],entero)-->str
# Ejemplo: gastosAño([[980000, 1310000, 1715000, 1947500], [963000, 1282500, 1690000, 1920000], [790000, 1085000, 1380000, 1560000]], 2018)-->Gastos de todas las Familias en el año 2018 : 
#                                                                                                                                            Familia 1: 
#                                                                                                                                            1310000
#                                                                                                                                            Familia 2: 
#                                                                                                                                            1282500
#                                                                                                                                            Familia 3: 
#                                                                                                                                            1085000
# Encabezado: gastosAño(c,año)--> gaFamilias


def gastosAño(c, año):
    inAño = año - 2017
    gaFamilias = ("Familia 1: "+"\n"+str(c[0][inAño])+"\n"+"Familia 2: "+"\n"+str(c[1][inAño])+"\n"+"Familia 3: "+"\n"+str(c[2][inAño]))
    return gaFamilias



#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: Recibe los datos de entrada y subprocesos, crea las matrices y muestra los datos de salida.
# Contrato: principal()
# Ejemplo: opcion = 1, familia = 2 -->Gastos de la Familia 2 fueron: 
#                                     2017 : 
#                                     963000
#                                     2018 : 
#                                     1282500
#                                     2019 : 
#                                     1690000
#                                     2020 : 
#                                     1920000
#
#           opcion = 0 --> saliendo del aplicativo
# Encabezado: principal()
            

def principal():
    a = [[450,800,650],[500,810,620],[200,500,600]]
    mostrarA = '\t Pan   Agua  Leche\n'
    i = 0
    while i < 3:
        mostrarA = mostrarA + '\nFamilia'+str(i+1)+'  '
        j = 0
        while j < 3:
            mostrarA = mostrarA + str(a[i][j]) + "  \t"
            j += 1
        mostrarA = mostrarA + "\n"
        i += 1



    b = [[200,300,500,550],[300,250,400,500],[1000,1500,1800,2000]]
    mostrarB = "       2017  2018  2019  2020\n"
    i = 0
    while i < 3:
        j = 0
        if i == 0:
            mostrarB += '\nPan    '
        elif i == 1:
            mostrarB += '\nAgua   '
        else:
            mostrarB += '\nLeche '
        while j < 4:
            mostrarB = mostrarB + str(b[i][j])+" \t"
            j += 1
        mostrarB = mostrarB + "\n"
        i += 1
        
    reporte.config(state="normal")
    reporte.insert(INSERT,"Matriz A:"+"\n"+str(mostrarA)+"\n"+"Matriz B:"+"\n"+str(mostrarB)+"\n")
    reporte.config(state="disable")

    c = [[0 for i in range (4)]for i in range (3)]
    gastos(a,b,c)

    mostrarC = informe(c)


    reporte.config(state="normal")
    reporte.insert(INSERT,"Matriz C:"+"\n"+str(mostrarC))
    reporte.config(state="disable")

    
    while True:
        opcion = simpledialog.askinteger("seleccione","MENU\n1. Obtener gastos de una familia en un año específico\n2. Obtener gastos de todas las familias en un año específico\n0. Salir\nSeleccione una opción : ")

        if opcion == 1:
            familia = simpledialog.askinteger("Familia","Ingrese el número de la familia (1-3): ")
            if familia <= 3 and familia >= 1:
                gaFamilias = gastosFamilia(c, familia)
                mostrar = messagebox.showinfo(message = "Gastos de la Familia "+str(familia)+" fueron: "+"\n"+str(gaFamilias),title = "")
            else:
                messagebox.showerror(message = "Opción inválida Por favor, seleccione una opción válida.", title = "Error")  
        elif opcion == 2:
            año = simpledialog.askinteger("Año","Ingrese el año (2017-2020): ")
            if año <= 2020 and año >= 2017:
                gastos_año = gastosAño(c, año)
                mostrar = messagebox.showinfo(message = "Gastos de todas las Familias en el año "+str(año)+" : "+"\n"+str(gastos_año), title = "")
            else:
                messagebox.showerror(message = "Opción inválida Por favor, seleccione una opción válida.", title = "Error")
        elif opcion == 0:
            mostrar = messagebox.showinfo(message = "Saliendo del aplicativo", title = "")
            break
        else:
            messagebox.showerror(message = "Opción inválida Por favor, seleccione una opción válida.", title = "Error")

def salir():
    ventana.destroy()


def delete():
    reporte.config(state="normal")
    reporte.delete("1.0", "end")
    reporte.config(state="disable")


ventana = Tk()
ventana.title("Matriz")
ventana.geometry("660x700")
ventana.config(bg='#25B788')
ventana.resizable(0,0)


marcoSalidas = LabelFrame(ventana, text= "Salidas")
marcoSalidas.config(width=40, height= 35, bd=  3, relief = "groove")
marcoSalidas.grid(column = 1, row = 1, rowspan = 4, pady = 10, padx = 10)
marcoSalidas.config(bg='#D8F3DC')


reporte = Text(marcoSalidas,width = 70, height = 28, state = "disable")
reporte.grid(column = 0, row = 0, pady = 10, padx = 10)


marcoEntry = LabelFrame(ventana, text= "Entradas")
marcoEntry.config(width=60, height= 45, bd= 3, relief = "groove")
marcoEntry.grid(column = 1, row =0, pady = 10, padx = 10)
marcoEntry.config(bg='#D8F3DC')


botonIniciar = Button(marcoEntry, text="Inicio", width = 20, command = principal)
botonIniciar.grid(row = 1 ,column = 0, pady = 10, padx = 10)

botonBorrar = Button(marcoEntry, text="Borrar", width = 20, command = delete)
botonBorrar.grid(row = 2 ,column = 0, pady = 10, padx = 10)

botonSalir = Button(marcoEntry, text="salir", width = 20, command = salir)
botonSalir.grid(row = 3 ,column = 0, pady = 10, padx = 10)


ventana.mainloop()