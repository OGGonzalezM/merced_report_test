# -*- coding: utf-8 -*-
{
    'name': "Wizard asign barcode to products",

    'summary': """
        Wizard para asignar el código de barras a los productos
        """,

    'description': """
        De acuerdo a los campos requeridos como identificadores de clasificación
        asi tambien como identificador del proveedor    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'views/wizard_barcode_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}