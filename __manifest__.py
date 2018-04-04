# -*- coding: utf-8 -*-
{
    'name': "Havana Backend Theme",

    'summary': """
        Feel Better""",

    'description': """
        Havana nanana for Odoo Feel Better
    """,

    'author': "Ali Alghozali",
    'website': "http://www.gueprogramer.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Themes/Backend',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
