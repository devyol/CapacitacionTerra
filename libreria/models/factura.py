from odoo import api, fields, models


class Factura(models.Model):
    _name = 'lib.factura'
    _description = 'Factura Libreria'

    name = fields.Char(string='Name')
    cliente_id = fields.Many2one(comodel_name='lib.cliente', string='Cliente')
    factura_lines = fields.One2many(comodel_name='lib.factura.detalle', inverse_name='factura_id', string='Lineas')


class FacturaDetalle(models.Model):
    _name= 'lib.factura.detalle'
    _description = 'Detalle de Factura'

    factura_id = fields.Many2one(comodel_name='lib.factura', string='Factura')
    cantidad = fields.Integer(string='Cantidad')
    precio = fields.Float(string='Precio')
    total = fields.Float(string='Total')
    
    
    
    

    
    
