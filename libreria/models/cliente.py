from odoo import api, fields, models


class Cliente(models.Model):
    _name = 'lib.cliente'
    _description = 'Cliente de Libreria'

    name = fields.Char(string='Name')
    telefono = fields.Char(string='Telefono')
    direccion = fields.Char(string='Direccion')
    

    

