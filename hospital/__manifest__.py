# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Gestor de un Hospital",

    'description': """
Gestionar los Medicos, Pacientes y Diagnosticos de un Hospital
    """,

    'author': "Ana Carbonell",
    'website': "https://github.com/AnaDaw",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application': True,
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/medico.xml',
        'views/paciente.xml',
        'views/diagnostico.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

