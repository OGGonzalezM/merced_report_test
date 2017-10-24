# -*- coding: utf-8 -*-

from odoo import models, fields

class Add_field(models.Model):
	_inherit = 'res.partner'

	nac = fields.Date(string="Fecha de Nacimiento")
	tel_ofi = fields.Char(string="Teléfono(oficina)")
	tel_cas = fields.Char(string="Telefono(casa)")
	ext = fields.Char()
	