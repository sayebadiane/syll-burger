{
    'name': 'Syll burger',
    'description': 'My module description',
    'depends': ['base','sale', 'website', 'website_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/website_menu.xml',
        'views/syll_burger_page.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
