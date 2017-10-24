# -*- coding: utf-8 -*-
{
    'name': "Grupo editar identificador proveedores",

    'summary': """Editar el identificador de los proveedores solo por grupo de usuarios""",

    'description': """
        Creación de un grupo para que solo ese pueda editar el campo del identificador de proveedor
    """,

    'author': "Soluciones 4G",
    'website': "soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_dat$
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/user_groups.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}