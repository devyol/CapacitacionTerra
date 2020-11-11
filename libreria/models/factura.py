from odoo import api, fields, models
from odoo.exceptions import Warning


class Factura(models.Model):
    _name = 'lib.factura'
    _description = 'Factura Libreria'

    name = fields.Char(string='Name')
    cliente_id = fields.Many2one(comodel_name='lib.cliente', string='Cliente')
    factura_lines = fields.One2many(comodel_name='lib.factura.detalle', inverse_name='factura_id', string='Lineas')
    xml = fields.Text(string='XML')
    total = fields.Float(string='Total')
    test = fields.Boolean(string='Test',default='False')
    state = fields.Selection(string='Estado', selection=[('iniciado', 'Iniciado'), ('finalizado', 'Finalizado'),], default="iniciado")
    direccion_cliente = fields.Char(string='Direccion', related="cliente_id.direccion")
    
    
    
    
    
    @api.model
    def create(self,vals):
        record = super(Factura,self).create(vals)
        record['name'] = self.env['ir.sequence'].next_by_code('factura')
        return record


    def calcularTotal(self):

        for record in self:

            totalT = 0
            for li in record.factura_lines:
                totalT += li.total

            record.total = totalT

    def validarTest(self):
        for record in self:
            if not record.test:
                raise Warning('El valor de test es Falso')


    


class FacturaDetalle(models.Model):
    _name= 'lib.factura.detalle'
    _description = 'Detalle de Factura'

    factura_id = fields.Many2one(comodel_name='lib.factura', string='Factura')
    cantidad = fields.Integer(string='Cantidad')
    precio = fields.Float(string='Precio')
    total = fields.Float(string='Total')

    
    @api.onchange('precio')
    def _calculo_total(self):
        for record in self:
            if record.cantidad and record.precio:
                record.total = record.cantidad * record.precio
    
    