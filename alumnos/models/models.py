-*- coding: utf-8 -*-

from odoo import models, fields, api


class alumnos(models.Model):
    _name = 'alumnos.alumnos'
    _description = 'alumnos.alumnos'

    name = fields.Char('Nombre')
    value = fields.Integer(default=100, copy=True)
    value2 = fields.Float(compute="_value_pc", store=True, readonly=True)
    description = fields.Text()
    tipo_alumno = fields.Selection(string='Tipo', selection=[('exce', 'Excelente'), ('bueon', 'Bueno'),], default="exce")
    seleccion = fields.Boolean(string='Boolean', default=True)
    new_field = fields.Selection(string='', selection=[('', ''), ('', ''),])
    tipo_cambio = fields.Float(string='Tipo',digits=(10,5))
    
    
    
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
