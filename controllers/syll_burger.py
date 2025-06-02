from odoo import http
from odoo.http import request
from collections import defaultdict

class SyllBurgerController(http.Controller):
    @http.route('/syll_burger', auth='public', website=True)
    def syll_burger(self, **kw):
        products = request.env['product.template'].search([('sale_ok','=',True), ('product_type', '!=', False)])
        
        # Grouper les produits par type
        grouped_products = defaultdict(list)
        for product in products:
            grouped_products[product.product_type].append(product)
        
        return request.render('syll_burger.syll_burger_page', {
            'grouped_products': grouped_products,
        })

    @http.route('/syll_burger/product_type/<string:product_type>', auth='public', website=True)
    def syll_burger_by_type(self, product_type, **kw):
        products = request.env['product.template'].search([
            ('sale_ok', '=', True),
            ('product_type', '=', product_type)
        ])
        return request.render('syll_burger.syll_burger_page', {
            'grouped_products': {product_type: products},
        })
