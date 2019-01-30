from re import compile
from datetime import datetime

class PicoPlaca(object):

    def __init__(self, placa = "ABC-0123", fecha = datetime.now().strftime("%Y-%m-%d"), hora = datetime.now().strftime("%H:%M")):
        self.placa = placa.upper()
        self.fecha = fecha
        self.hora = hora

        matricula_ciudad = ["A","B","U","C","H","X","O","E","W","G","I","L" \
        ,"R","M","V","N","Q","S","P","Y","J","K","T","Z"]
        formato_placa = compile('^[A-Z]{3}[-]{1}[0-9]{4}$')
        formato_fecha = compile('^[0-9]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$')
        formato_hora = compile('^[0-9]{2}[:]{1}[0-9]{2}')

        if self.placa[0] not in matricula_ciudad:
            print("Verifique que la placa sea correcta")
            exit(1)

        if formato_placa.match(self.placa) and formato_fecha.match(self.fecha) \
        and formato_hora.match(self.hora) is not None:
            pass
        else:
            print("Ingrese el formato correcto, Ejemplos:")
            print("Formato de placa: 'ABC-0123' o 'abC-9482'")
            print("Formato de fecha: '2019-01-28'")
            print("Formato de hora: '17:30' o '09:02'")
            exit(1)

    def valida_hora(self):
        hora = datetime.strptime(self.hora, '%H:%M').time()
        manana_inicio = datetime.strptime("07:00", "%H:%M").time()
        manana_fin = datetime.strptime("09:30", "%H:%M").time()
        tarde_inicio = datetime.strptime("16:00", "%H:%M").time()
        tarde_fin = datetime.strptime("19:30", "%H:%M").time()

        if (hora >= manana_inicio and hora <= manana_fin) or \
        (hora >= tarde_inicio and hora <= tarde_fin):
            return True
        else:
            return False

    def valida_fecha(self):
        fecha = datetime.strptime(self.fecha, "%Y-%m-%d").weekday()
        if fecha < 5:
            return True
        else:
            return False

    def valida_placa(self):
        digito_placa = int(self.placa[-1])
        fecha = datetime.strptime(self.fecha, "%Y-%m-%d").weekday()
        if fecha == 0 and (digito_placa == 1 or digito_placa ==2):
            return True
        elif fecha == 1 and (digito_placa == 3 or digito_placa == 4):
            return True
        elif fecha == 2 and (digito_placa == 5 or digito_placa == 6):
            return True
        elif fecha == 3 and (digito_placa == 7 or digito_placa == 8):
            return True
        elif fecha == 4 and (digito_placa == 9 or digito_placa == 0):
            return True
        else:
            return False

    def prediccion(self):
        if self.valida_hora() and self.valida_fecha() and self.valida_placa():
            print("No puede circular")
            return True
        else:
            print("Si puede circular")
            return False

placa= "abc-1234"
fecha = "2019-02-26"
hora = "19:30"
Placa = PicoPlaca(placa, fecha, hora)
#Placa = PicoPlaca()
Placa.prediccion()
