#Calcular isotonicidad de problema simple
Porc_sal= 0.009
class Problema_isotonicidad:
	
	def ProblemaSimple(self):
		cantidad_farmaco = float(input("Ingresa cantidad del fármaco en g: "))
		e_value_farmaco = float(input("Ingresa E-value del fármaco: "))
		volumen = float(input("Ingresa volumen en ml: "))
		farmaco_total = cantidad_farmaco
		eq_nacl = e_value_farmaco * farmaco_total
		nacl_total = Porc_sal * volumen
		resolucion = nacl_total - eq_nacl
		print(str(resolucion) + "g Nacl deben ser agregados")

	def Problema_dos_farmacos(self):
		cantidad_farmaco1 = float(input("Ingresa cantidad del fármaco 1 en g: "))
		e_value_farmaco1 = float(input("Ingresa E-value del fármaco/sustancia 1: "))
		cantidad_farmaco2 = float(input("Ingresa cantidad del fármaco/sustancia 2 en g: "))
		e_value_farmaco2 = float(input("Ingresa E-value del fármaco 2: "))
		volumen = float(input("Ingresa volumen en ml: "))
		farmaco_total1 = cantidad_farmaco1
		eq_nacl1 = e_value_farmaco1 * farmaco_total1
		farmaco_total2 = cantidad_farmaco2
		eq_nacl2 = e_value_farmaco2 * farmaco_total2
		nacl_total = Porc_sal * volumen
		total_eq_nacl = eq_nacl1 + eq_nacl2
		resolucion = nacl_total - total_eq_nacl
		print(str(resolucion) + "g Nacl deben ser agregados")



tipo_problema = input("¿Cuántos fármacos o sustancias incluye tu problema? (Elegir 1 o 2) ")
try:
    tipo_problema = int(tipo_problema) 
except:
    print("sólo números 1 y 2")
if tipo_problema == 1:
	resolver = Problema_isotonicidad()
	resolver.ProblemaSimple()

if tipo_problema == 2:
	resolver = Problema_isotonicidad()
	resolver.Problema_dos_farmacos()