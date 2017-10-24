# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Barcodes_wizard(models.TransientModel):
	_name = 'merced.codigosbarras'

	def _default_products(self):
		return self.env['product.template'].browse(self._context.get('active_ids'))

	product_barcode_ids = fields.Many2many('product.template',
         string="Productos para general el código de barras", required=True, default=_default_products)

	@api.multi
	def asignar_codigos(self):
		for productos_asignar in self.product_barcode_ids:
			try:
			    prov_id = productos_asignar.seller_ids[0].name
			    ident_prov = prov_id.x_identificador
			    ident_class = productos_asignar.class_id.identificador
			    if ident_prov == False:
			    	print "*************************************** if"
			        #self.write({'barcode': ''})
			       	productos_asignar.write({'msj_error': 'Por favor agregue un identificador al proveedor'})
			    elif ident_class == False:
			    	print "************************************ elif"
			    	#self.write({'barcode':''})
			    	productos_asignar.write({'msj_error': 'Por favor agregue una clasificacion'})

			    else:
			       print "************************************ Finalizado"
			       numero = 1000000000 + productos_asignar.id
			       num_str = str(numero)
			       cod_barras = str(ident_prov) + str(ident_class) + str(num_str[1:10])
		               productos_asignar.write({'barcode': cod_barras})
		               #self.write({'tested_field': cod_barras})
			       productos_asignar.write({'msj_error': ' '})
			except IndexError as e:
			    #self.write({'barcode': ' '})
			    productos_asignar.write({'msj_error': 'Por favor agregue un proveedor '})
