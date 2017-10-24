# -*- coding: utf-8 -*-
{
    'name': "Wizard from warehouse to pos",

    'summary': """
        Wizard para cambiar estado de un producto en el punto de venta
        """,

    'description': """
        Cambiar estado de disponible o no disponible solo ciertos productos seleccionados
        en el punto de venta. Esto desde la vista de lista de almacen
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale','product'],

    # always loaded
    'data': [
        'views/wizard_pos_view.xml',
        'views/wizard_desactivar_pos_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
