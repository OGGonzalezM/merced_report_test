# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Customer_barcodes(models.Model):
	_inherit = 'res.partner'

	barcode = fields.Char(compute='set_barcode')
        #test_barcode = fields.Char(related='barcode', store='True', string="Relacionado con el codigo de barras")
        #ref = fields.Char(related='barcode')

	@api.multi
	def set_barcode(self):
            for record in self:
                nuevoid = record.id
                nummedio = 1000000 + nuevoid
                numstr = str(nummedio)
                nmedio = str(numstr[1:7])
                codigo_barras = "042"+ nmedio
                record.barcode = codigo_barras
