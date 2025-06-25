{
    'name': 'Syll burger',
    'description': 'My module description',
    'depends': ['base','sale', 'website', 'website_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/website_menu.xml',
        'views/syll_burger_page.xml',
        # 'views/assets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'web.public.widget',  # ⚠️ Ceci est un module JS, pas un fichier
            '/syll_burger/static/src/js/syll_burger_checkout.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
