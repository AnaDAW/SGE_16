# -*- coding: utf-8 -*-
{
    'name': "Batoi",

    'summary': "CIPFP Batoi",

    'description': """
Gestiona los estudios impartidos en el instituto CIPDP Batoi
    """,

    'author': "Ana Carbonell",
    'website': "https://github.com/AnaDaw",

    'application': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ciclo.xml',
        'views/modulo.xml',
        'views/alumno.xml',
        'views/profesor.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

