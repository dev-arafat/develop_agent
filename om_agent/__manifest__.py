# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'agent',
    'version' : '1.2',
    'summary': 'account agent managemente software',
    'sequence': 10,
    'description': """ account agent software """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/agent.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}
