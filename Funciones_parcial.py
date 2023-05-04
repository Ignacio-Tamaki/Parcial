from Clases import * 

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

