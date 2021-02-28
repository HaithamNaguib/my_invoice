# -*- coding: utf-8 -*-
{
    'name': "my_invoice",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/my_invoice.xml',
        'views/persons.xml',
        'views/classes.xml',
        'views/skills.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
