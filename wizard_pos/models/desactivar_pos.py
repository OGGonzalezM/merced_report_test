# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Wizard_pos(models.TransientModel):
	_name = 'available.despos'

	def _default_products(self):
		return self.env['product.template'].browse(self._context.get('active_ids'))

	product_wiz_ids = fields.Many2many('product.template',
		string="Productos a desactivar",
		required=True, 
		default=_default_products)

	@api.multi
	def desactivar_enpos(self):
		for product_wiz_ids in self.product_wiz_ids:
			product_wiz_ids.available_in_pos = False
		return {}