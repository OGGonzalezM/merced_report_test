# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models, _

class Generador(models.Model):
    _inherit = 'product.template'

    class_id = fields.Many2one('classification.product', string="Clasificacion")
    msj_error = fields.Char(readonly=True)
    #barcode = fields.Char(string="Código de barras ", store=True)
    #tested_field = fields.Char(string="Test", compute='', readonly=True)


    @api.multi
    def imprimir(self):
        try:
	    prov_id = self.seller_ids[0].name
	    ident_prov = prov_id.x_identificador
	    ident_class = self.class_id.identificador
	    print "*******************Entrada al try***********************"
	    if ident_prov == False:
	        #self.write({'barcode': ''})
	       	self.write({'msj_error': 'Por favor agregue un identificador al proveedor'})
	    elif ident_class == False:
	    	#self.write({'barcode':''})
	    	print "*****************Entrada elif***********************************"
	    	self.write({'msj_error': 'Por favor agregue una clasificacion'})
	    else:
	       numero = 1000000000 + self.id
	       num_str = str(numero)
	       cod_barras = str(ident_prov) + str(ident_class) + str(num_str[1:10])
               self.write({'barcode': cod_barras})
               #self.write({'tested_field': cod_barras})
	       print "*******************Finalizado*********************"
	       self.write({'msj_error': ' '})
	except IndexError as e:
	    #self.write({'barcode': ' '})
	    self.write({'msj_error': 'Por favor agregue un proveedor '})
