from clase_email import Email
import csv
import re

def verificar(fila:list[Email])->bool:
    patron=r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
    if re.match(patron,fila):
        print("\nDireccion valida.")
        return True
    else: 
        print("\nDireccion invalida.")

def test(lista):
    archivo=open('email.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        if verificar(fila[0]):
            email = Email("", "", "", "")
            email.crear_cuenta(fila[0])
            lista.append(email)

if __name__ == '__main__':
    lista_email = []
    persona = Email()
    nombre = input('Ingrese su Nombre:')
    persona.crear_email()
    print('Estimado ' + nombre +' te enviaremos tus mensajes a la dirección ',persona.retorna_email())
    persona.modificar_contraseña()
    test(lista_email)
    dom = input('Ingrese el dominio')
    Email.cantDominios(dom,lista_email)
    
    
    