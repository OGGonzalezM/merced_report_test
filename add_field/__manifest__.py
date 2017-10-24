# -*- coding: utf-8 -*-
{
    'name': "Adding Fields",

    'summary': """
        Agrega campos al res.partner
        """,

    'description': """
        Los campos que agrega son:
        - Fecha de cumpleaños
        - Telefono de casa
    """,

    'author': "Soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'view/add_field_view.xml',
     
    ],

    'installable':True,
    'auto_install':False,
}