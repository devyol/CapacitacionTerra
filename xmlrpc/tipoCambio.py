from zeep import Client
from datetime import datetime,date

url = 'https://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?wsdl'

response = Client(url)

tipo_cambio = response.service.TipoCambioDia()

msg = f'Tipo de cambio es {tipo_cambio}'

tasa = tipo_cambio.CambioDolar.VarDolar[0].referencia
fecha = tipo_cambio.CambioDolar.VarDolar[0].fecha

#print(msg)
print(f'Tasa {tasa}')
print(f'Fecha {fecha}')
print (type(fecha))