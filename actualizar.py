from Clases import *
from Funciones_parcial import *
def chequeo_existencia_DNI_mail():
    while True:
        listaComodin=[]
        matrizInvitados = leer_parcial()
        listaMenu = ['DNI', 'mail']
        #inputs
        for i in range(2):
                user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                listaComodin.append(user_input)
        listaComodin[0]=persona.check_DNI(listaComodin[0])
        listaComodin[1]=persona.check_sintaxis_mail(listaComodin[1])
        for i in range(len(matrizInvitados)):
            if matrizInvitados[i][0] == listaComodin[0] and matrizInvitados[i][3] == listaComodin[1]:
                fila = i
                booleana = True
        #Permitido
        if booleana == True:
            print('Permitido actualizar')
            listaMenu = ['DNI', 'Nombre', 'apellido', 'mail']
            for i in range(4):
                    user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                    listaComodin.append(user_input)
            listaComodin[0]=persona.check_DNI(listaComodin[0],matrizInvitados)
            listaComodin[0]=DNI_repetido_login(listaComodin)
            listaComodin[1]=persona.check_nombre(listaComodin[1])
            listaComodin[2]=persona.check_nombre(listaComodin[2])
            listaComodin[3]=persona.check_sintaxis_mail(listaComodin[3])
            listaComodin[3]=mail_repetido_login(listaComodin[3],matrizInvitados)
            matrizInvitados[fila]=[listaComodin[0],listaComodin[1],listaComodin[2],listaComodin[3]]
            #Falta lo de pasarlo al txt
            print('actualizado')
        #No permitido
        else: 
            print('No fue permitido actualizar. Ingrese nuevamente los datos')

