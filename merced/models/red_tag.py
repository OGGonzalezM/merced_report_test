# -*- coding: utf-8 -*-

from odoo import models, fields

class red_tag(models.Model):
	_name = 'redes.tag'

	name = fields.Char(String="Nombre de red")
