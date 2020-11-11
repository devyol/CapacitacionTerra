#-*- coding: utf-8 -*-

from odoo import models, fields, api


class libreria_ext(models.Model):
    _inherit = 'lib.factura'
    _description ='Factura'


    tipo_venta = fields.Selection(string='Tipo', selection=[('internaciona', 'Internacional'), ('nacional', 'Nacional'),])
    iva = fields.Float(string='Iva')
    


    # @api.model
    # def calcularTotal(self):
    #     record = super(libreria_ext,self).calcularTotal()
    #     print(record)
    #     ivaCalculado = record['total'] * 0.12
    #     record['iva'] = ivaCalculado
    #     return record

    
