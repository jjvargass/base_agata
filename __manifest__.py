# -*- coding: utf-8 -*-
{
    'name': "base_agata",
    'icon': '/base_agata/static/description/icon.png',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'hr_contract',
        'crm',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/hr_view.xml',
        'views/crm_lead_agata_view.xml',
        'views/crm_lead_agata_menu_view.xml',
        'views/crm_lead_view.xml',
        'data/hr.department.csv',
        'data/hr.job.csv',
        'data/crm.lead.ally.csv',
        'data/crm.lead.budget.csv',
        'data/crm.lead.business.line.csv',
        'data/crm.lead.strategy.csv',
        'data/crm.lead.type.solution.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
