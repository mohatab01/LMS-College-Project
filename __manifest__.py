# -*- coding: utf-8 -*-
{
    'name': 'LMS',
    'version': '1.0.0',
    'website': '',
    'category': 'web',
    'summary': 'JS v1.0',
    'description': """

	""",
    'depends': ['base','website'],
    'data': [
       'views/ir.ui.view.xml',
       'views/ir.ui.menu.xml',
       'views/website/home.xml',
       'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}


