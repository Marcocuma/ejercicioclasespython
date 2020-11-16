class Empleado:
    def __init__(self,nombre,apellidos,dni,direccion,antiguedad,telf,salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.salario = salario
        self.telefono = telf
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Apellidos: ",self.apellidos)
        print("DNI: ",self.dni)
        print("Direccion: ",self.direccion)
        print("Antiguedad: ",self.antiguedad)
        print("Salario: ",self.salario)
        print("Telefono: ",self.telefono)

    def cambiarSupervisor(self,supervisor):
        self.supervisor = supervisor

    def imprimirSupervisor(self):
        if self.supervisor:
            print(self.supervisor)

    def incrementarSalario(self,incremento):
        self.salario += incremento


class Secretario(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, antiguedad, telf, salario,despacho,fax):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, antiguedad, telf, salario)
        self.despacho = despacho
        self.fax = fax

    def imprimir(self):
        Empleado.imprimir(self)
        print("Despacho: ",self.despacho)
        print("Fax: " , self.fax)

    def incrementarSalario(self):
        Empleado.incrementarSalario(self,self.salario*0.05)

class Coche:
    def __init__(self, matricula,marca,modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

    def imprimir(self):
        print("Matricula: ",self.matricula)
        print("Marca: " , self.marca)
        print("Modelo: " , self.modelo)

class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, antiguedad, telf, salario,coche,movil,areaVenta,percVentas):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, antiguedad, telf, salario)
        self.coche = coche
        self.movil = movil
        self.areaVenta = areaVenta
        self.lClientes = []
        self.percVentas = percVentas

    def imprimir(self):
        Empleado.imprimir(self)
        print("Coche: ",self.coche.imprimir())
        print("Movil: " , self.movil)
        print("Area Venta: " , self.areaVenta)
        print("Lista Clientes: ",self.lClientes)
        print("Porcentaje comision ventas: " , self.percVentas)

    def altaCliente(self,cliente):
        self.lClientes.append(cliente)

    def bajaCliente(self,cliente):
        self.lClientes.remove(cliente)

    def cambiarCoche(self,coche):
        self.coche = coche

    def incrementarSalario(self):
        Empleado.incrementarSalario(self,self.salario*0.10)

class JefeDeZona(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, antiguedad, telf, salario,despacho,secretario,coche):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, antiguedad, telf, salario)
        self.coche = coche
        self.despacho = despacho
        self.lVendedores = []
        self.secretario = secretario

    def imprimir(self):
        Empleado.imprimir(self)
        print("Coche: ",self.coche.imprimir())
        print("Despacho: " , self.despacho)
        print("Secretario: " )
        self.secretario.imprimir()
        print("Lista Vendedores: ")
        for vendedor in self.lVendedores:
            vendedor.imprimir()

    def cambiarSecretario(self,secretario):
        self.secretario = secretario

    def altaVendedor(self,vendedor):
        self.lVendedores.append(vendedor)

    def bajaVendedor(self,vendedor):
        self.lVendedores.remove(vendedor)

    def cambiarCoche(self,coche):
        self.coche = coche

    def incrementarSalario(self):
        Empleado.incrementarSalario(self,self.salario*0.20)

'''Programa prueba'''
'''Creo un secretario y le incremento el sueldo'''
secretario1 = Secretario("Juan","Sanchez","00000000h","Calle sol",14,666666666,800,"Num1",665666656)
'''Datos actuales del secretario 1'''
print("Datos secretario")
secretario1.imprimir()

'''incremento sueldo'''
print("Incremento sueldo")
secretario1.incrementarSalario()
'''Datos actuales del secretario 1'''
print("Datos secretario")
secretario1.imprimir()


'''Creo un vendedor'''
vendedor1 = Vendedor("Joaquin","Marin","77777777G","Estacion",70,665555555,1200,
                     Coche("222www","Seat","Ibiza"),666777889,"Loja",5)
'''Añado un cliente'''
vendedor1.altaCliente("pedro")
'''Muestro sus datos'''
print("Datos del vendedor")
vendedor1.imprimir()
'''Incremento salario'''
vendedor1.incrementarSalario()
'''Vuelvo a mostrar los datos'''
print("Vuelvo a mostrar los datos")
vendedor1.imprimir()


'''Creo un jefe de zona'''
jefe1 = JefeDeZona("Manolo","Garcia","666554433h","Calle gracia",20,635477443,1400,
                   "Num3",secretario1,Coche("252wfw","Suzuki","Vitara"))
'''Añado un vendedor'''
jefe1.altaVendedor(vendedor1)
'''Muestro sus datos'''
print("Datos del jefe")
jefe1.imprimir()
'''Incremento salario'''
jefe1.incrementarSalario()
'''Vuelvo a mostrar los datos'''
print("Datos del jefe")
jefe1.imprimir()