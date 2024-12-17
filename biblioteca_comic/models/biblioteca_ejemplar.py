from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BibliotecaEjemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar de comic'

    name = fields.Char(related='comic_id.nombre')
    comic_id = fields.Many2one(
        string='Comic',
        comodel_name='biblioteca.comic',
        ondelete='cascade',
        required=True,
        
    )
    prestado = fields.Boolean(string='Está Prestado', compute='_value_prestado', store=True)
    socio_id = fields.Many2one(
        string='Prestatario',
        comodel_name='biblioteca.socio',
        ondelete='restrict',
    )
    fecha_inicio = fields.Date(string='Fecha Prestado', compute='_value_prestado', store=True)
    fecha_fin = fields.Date(string='Fecha Devolución',)
    
    
    @api.depends('socio_id')
    def _value_prestado(self):
        for record in self:
            if record.socio_id:
                record.prestado = True
                record.fecha_inicio = fields.Date.today()
            else:
                record.prestado = False
                record.fecha_inicio = False
                record.fecha_fin = False

    @api.constrains('fecha_fin', 'socio_id')
    def _check_fecha(self):
        for record in self:
            if record.socio_id and (not record.fecha_fin or record.fecha_fin < fields.Date.today()):
                raise models.ValidationError('La fecha de devolución debe ser posterior a la actual')