from odoo import api, fields, models
from datetime import datetime, date , timedelta

class Cliente(models.Model):
    _name = 'lib.cliente'
    _description = 'Cliente de Libreria'

    name = fields.Char(string='Name')
    telefono = fields.Char(string='Telefono')
    direccion = fields.Char(string='Direccion')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    genero = fields.Selection(string='Genero', selection=[('hombre', 'Hombre'), ('mujer', 'Mujer'),])
    edad = fields.Integer(string='Edad', compute='_calcular_edad')
    

    @api.depends('fecha_nacimiento')
    def _calcular_edad(self):
        for record in self:

            if not record.fecha_nacimiento:
                record.edad = 0
            else:
                hoy = date.today()
                nacimiento = record.fecha_nacimiento
                print(type(hoy))
                print(hoy)                
                print(type(nacimiento))
                print(nacimiento)

                anios = hoy.year - nacimiento.year

                if anios > 0:

                    if hoy.month > nacimiento.month:
                        record.edad = hoy.year - nacimiento.year
                    elif hoy.month < nacimiento.month:
                        edadnocumplida = (hoy.year - nacimiento.year) - 1
                        record.edad = edadnocumplida
                    elif hoy.month == nacimiento.month and anios > 0:
                        if hoy.day >= nacimiento.day:
                            record.edad = hoy.year - nacimiento.year
                        else:
                            edadnocumplida = (hoy.year - nacimiento.year) - 1
                            record.edad = edadnocumplida

                elif anios <= 0:
                    record.edad = 0


    
    
    
    

    

