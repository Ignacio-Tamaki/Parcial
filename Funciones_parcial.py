from Clases import * 
import matplotlib.pyplot as mlp

#login recibe un usuario y una contraseña para chequear si está en el sistema. 
def login_parcial(username, password, new_password=None):
    with open("Usuarios.txt", 'r', encoding='utf-8') as archivo:
        listaUsuarios=[]
        passwordList=[]
        for linea in archivo:
            usu, contra = linea.strip().split(".")
            listaUsuarios.append(usu)
            passwordList.append(contra)
        while username not in listaUsuarios:
            username = input("El usuario ingresado no existe. Intente de nuevo: ")
        index = listaUsuarios.index(username)
        while passwordList[index] != password:
            password = input("Error, contraseña incorrecta. Ingresela nuevamente: ")
        if new_password is not None:
            passwordList[index] = new_password
            with open("Usuarios.txt", 'w', encoding='utf-8') as archivo:
                for i in range(len(listaUsuarios)):
                    archivo.write(f"{listaUsuarios[i]}.{passwordList[i]}\n")
        return True

def DNI_repetido_login(DNI,matrizInvitados):
    for objeto in matrizInvitados:
        if objeto[0]==DNI:
            DNI=input('Ingreso un DNI ya existente. Ingrese uno nuevo:  ')
            DNI=persona.check_DNI(DNI)
            DNI=DNI_repetido_login(DNI,matrizInvitados)
            return DNI
    return DNI

def mail_repetido_login(mail,matrizInvitados):
    for objeto in matrizInvitados:
        if objeto[3]==mail:
            mail=input('Ingreso un mail ya existente. Ingrese uno nuevo:  ')
            mail=persona.check_DNI(mail)
            mail=mail_repetido_login(mail,matrizInvitados)
            return mail
    return mail

def actualizar_login():
    while True:
        listaComodin_1=[]
        matrizInvitados = leer_parcial()
        listaMenu = ['DNI', 'mail']
        #inputs
        for i in range(2):
                user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                listaComodin_1.append(user_input)
        listaComodin_1[0]=persona.check_DNI(listaComodin_1[0])
        listaComodin_1[1]=persona.check_sintaxis_mail(listaComodin_1[1])
        for i in range(len(matrizInvitados)):
            if matrizInvitados[i][0] == listaComodin_1[0] and matrizInvitados[i][3] == listaComodin_1[1]:
                fila = i
                booleana = True
        #Permitido
        if booleana == True:
            print('Permitido actualizar')
            listaMenu = ['DNI', 'Nombre', 'apellido', 'mail']
            listaComodin_2=[]
            for i in range(4):
                    user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                    listaComodin_2.append(user_input)
            
            listaComodin_2[0]=persona.check_DNI(listaComodin_2[0])
            listaComodin_2[0]=DNI_repetido_login(listaComodin_2[0],matrizInvitados)
            listaComodin_2[1]=persona.check_nombre(listaComodin_2[1],'nombre')
            listaComodin_2[2]=persona.check_nombre(listaComodin_2[2],'apellido')
            listaComodin_2[3]=persona.check_sintaxis_mail(listaComodin_2[3])
            listaComodin_2[3]=mail_repetido_login(listaComodin_2[3],matrizInvitados)
            listaComodin_2.append(matrizInvitados[fila][-1])
            matrizInvitados[fila]=listaComodin_2
            print(matrizInvitados[fila])
            print('actualizado')
            return matrizInvitados
        #No permitido
        else: 
            print('No fue permitido actualizar. Ingrese nuevamente los datos')
            
def listanormal_a_txt(matrizInvitados):
    matrizNueva = []
    for fila in matrizInvitados:
                cadena = ""
                for elemento in fila:
                    cadena += str(elemento) + " "
                matrizNueva.append(cadena)

    with open('visitass.txt', 'w') as archivo:
        for elemento in matrizNueva:
            archivo.write(str(elemento) + '\n')

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
    for fila in range(5):
           matrizUsuarios.append(matrizInvitados[fila][0])
           matrizAccesos.append(int(matrizInvitados[fila][4]))
    mlp.bar(matrizUsuarios,matrizAccesos)
    mlp.title("5 usuarios con menor acceso")
    mlp.xlabel("DNI")
    mlp.ylabel("Cantidad de veces")
    mlp.show()



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