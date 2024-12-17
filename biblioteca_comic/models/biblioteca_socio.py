from odoo import models, fields

class BibliotecaSocio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio de biblioteca'
    
    name = fields.Char(string='Nombre',)
    lastname = fields.Char(string='Apellido',)
    socio_id = fields.Char(string='Identificador',)
    ejemplar_ids = fields.One2many(
        string='Comics Prestados',
        comodel_name='biblioteca.ejemplar',
        inverse_name='socio_id',
    )