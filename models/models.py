# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulo_Clientes(models.Model):
    _name = 'modulo1.clientes'
    _description = 'Modelo Clientes'

    name = fields.Char(
        string='Nombre', help='Nombre del cliente', required=True)
    dni = fields.Integer(string='DNI', help='DNI del cliente', required=True)
    enrollment_date = fields.Datetime(
        string='Fecha de alta',
        default=lambda self: fields.Datetime.now(),
    )
    last_login= fields.Date(
        string='Ultimo_acceso',
        default=lambda self: fields.Datetime.now(),
    )
    


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
