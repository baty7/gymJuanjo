# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class modulo_Profesores(models.Model):
    _name = 'modulo3.profesores'
    _description = 'Modelo Profesores'

    name = fields.Char(
        string='Nombre', help='Nombre del profesor/a', required=True)


class modulo_Cursos(models.Model):
    _name = 'modulo2.cursos'
    _description = 'Modelo Cursos'

    name = fields.Char(
        string='Nombre', help='Nombre del curso', required=True)
    schedule = fields.Datetime(
        string='Fecha de alta',
        default=lambda self: fields.Datetime.now(),
    )

    clientes_id = fields.Many2one(
        string='Clientes',
        comodel_name='modulo1.clientes',
        ondelete='restrict',
    )


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
    last_login = fields.Date(
        string='Ultimo_acceso',
        default=lambda self: fields.Datetime.now(),
    )
    photo = fields.Image(max_width=200, max_height=200)

    fee = fields.Selection(string='Formato', help='Formato de disco',
                           selection=[('1', '4-10$'),
                                      ('2', '8-15$'), ('3', '12-20$')]
                           )
    curso_id = fields.Many2one(
        string='Cursos',
        comodel_name='modulo2.cursos',
        ondelete='restrict',
    )
    
    #trainings = fields.Integer(string = 'Clases',compute =_clases_ )

    @api.constrains('dni')
    def _check_(self):
        for record in self:
            if self.search([('dni', '=', record.dni)], limit=1) != record:
                raise ValidationError("Error, DNI repetido")


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
