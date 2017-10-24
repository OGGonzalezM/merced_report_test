# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Wizard_pos(models.TransientModel):
	_name = 'almacen.actpos'

	def _default_products(self):
		return self.env['product.product'].browse(self._context.get('active_ids'))

	product_wiz_ids = fields.Many2many('product.product',
		string="Productos a activar",
		required=True,
		default=_default_products)

	@api.multi
	def activar_enpos(self):
		for product_wiz_ids in self.product_wiz_ids:
			product_wiz_ids.available_in_pos = True
