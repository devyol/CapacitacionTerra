URL = 'http://localhost:8069'
DB = 'c_odoo13'
USER = 'admin'
PASS = 'admin'

import xmlrpc.client

common =xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
version = common.version()
print('details....',version)


uid = common.authenticate(DB, USER, PASS, {})

#Devuelve listado de id's del modelo res.partner
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
customers = models.execute_kw(DB, uid, PASS,'res.partner','search',[[]])
print("Partnes...", customers)

print('----------------------------------------------------------')

#conexion con nuestro modelo
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
customers2 = models.execute_kw(DB, uid, PASS,'lib.cliente','search',[[]])
print("Partnes2...", customers2)

print('----------------------------------------------------------')

mayores = models.execute_kw(DB, uid, PASS,
    'lib.cliente', 'search_read',
    [[['mayor_edad', '=', False]]],
    {'fields': ['name', 'telefono', 'direccion'], 'limit': 5})

print(mayores)

print('----------------------------------------------------------')

mayores = models.execute_kw(DB, uid, PASS,
    'lib.cliente', 'search_read',
    [[['mayor_edad', '=', False]]],
    {'fields': ['name', 'telefono', 'direccion'], 'limit': 5})