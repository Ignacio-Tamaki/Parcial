from Clases import *
import matplotlib.pyplot as mlp
import numpy as np
def ordenamiento(columna, matriz, orden=0):
  if orden == 0:
    for i in range(len(matriz)-1):
      for j in range(i+1, len(matriz)):
          if matriz[i][(columna)] < matriz[j][(columna)]:
            aux = matriz[i]
            matriz[i] = matriz[j]
            matriz[j] = aux
  else:
    for i in range(len(matriz)-1):
      for j in range(i+1, len(matriz)):
          if matriz[i][(columna)] > matriz[j][(columna)]:
            aux = matriz[i]
            matriz[i] = matriz[j]
            matriz[j] = aux
  return matriz
 #Visualizar en una gráfica tipo barras los dni de los 5 usuarios invitados que menos acceso hayan 
        #tenido acceso a la plataforma. 

def visualizacion():
    matrizInvitados = leer_parcial()
    matrizInvitados= ordenamiento(4,matrizInvitados,1)   
    matrizUsuarios=[]   
    matrizAccesos=[]
    for fila in range(len(matrizInvitados)):
           matrizUsuarios.append(matrizInvitados[fila][0])
           matrizAccesos.append(matrizInvitados[fila][4])
    
    return matrizAccesos[0:5],matrizUsuarios[0:5]



#Eliminar un usuario invitado por dni o email, 
#el usuario debe decidir por cual de estas dos opciones hacerlo

def EliminarInvitado():
    matrizInvitados=leer_parcial()
    opcion=input("Ingrese 1 si quiere eliminar por dni, Ingrese 2 si quiere eliminar por mail: ")
    while True: 
      if opcion=='1':
        dni=input("Ingrese el dni que quiere eliminar: ")
        dni=persona.check_DNI(dni)
        for fila in range(len(matrizInvitados)):
           if matrizInvitados[fila][0]==dni:
              matrizInvitados.pop(fila)
              return matrizInvitados
      elif opcion=='2':
        mail=input("Ingrese el mail que quiere eliminar: ")
        mail=persona.check_sintaxis_mail(mail)
        for fila in range(len(matrizInvitados)):
           if matrizInvitados[fila][3]==mail:
              print(matrizInvitados[fila][3])
              matrizInvitados.pop(fila)     
              return matrizInvitados   
      else: 
        opcion=input("Ingrese 1 si quiere eliminar por dni, Ingrese 2 si quiere eliminar por mail: ") 



matriz=EliminarInvitado()
print(matriz)



