class Email:
    __id_cuenta: str
    __dominio: str
    __tipo_dominio: str
    __contrasena: str
    
    def __init__ (self, id_cuenta = '', dominio = '', tipo_dominio = '', contrasena = ''):
        self.__id_cuenta = id_cuenta
        self.__dominio = dominio
        self.__tipo_dominio = tipo_dominio
        self.__contrasena = contrasena
        return
    
    def __str__(self)->str:
        return f"{self.__id_cuenta, self.__dominio, self.__tipo_dominio, self.__contrasena}"
        
    def get_dominio(self):
        return self.__dominio

    def retorna_email(self)->str:
        return self.__id_cuenta + '@' + self.__dominio + '.' + self.__tipo_dominio
    
    def verifica_contrasena(self)->bool:
        verifica = False
        contraseña = input ('Ingrese su contraseña actual')
        if contraseña == self.__contrasena:
            verifica = True
        return verifica
    
    def modificar_contraseña (self):
        if self.verifica_contrasena() == True:
            contrasena = input('Ingrese la nueva contraseña: ')
            self.__contrasena = contrasena
        else:
            print('Contraseña incorrecta')
        return
    
    def crear_cuenta(self, direccion:str):
        id_cuenta = direccion.split('@')
        self.__id_cuenta = id_cuenta[0]
        dominio = id_cuenta[1].split('.')
        self.__dominio = dominio[0]
        self.__tipo_dominio = dominio[1]
        return Email(self.__id_cuenta, self.__dominio, self.__tipo_dominio)
    
    def crear_email(self):
        print('Ingrese los siguientes datos:')
        self.__id_cuenta = id_cuenta = input('ID Cuenta:')
        self.__dominio = dominio = input('Dominio:')
        self.__tipo_dominio = tipo_dominio = input('Tipo de Dominio:')
        self.__contrasena = contraseña = input('Contraseña:')
        return
    
    def cantDominios(dom:str, lista:list["Email"])->None:
        contador=0
        for correo in lista:
            if dom == correo.get_dominio():
                contador+=1
        if contador==0: print("\nDominio no encontrado.")
        else: print("El dominio {} se encuentra en {} correo/s".format(dom,contador))