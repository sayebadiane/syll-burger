from odoo import models, fields

class CustomProduct(models.Model):
    _inherit = 'product.template'

    product_type = fields.Selection([
        ('burger', 'BURGERS'),
        ('smashs', 'SMASHS'),
        ('chicken_burger', 'CHICKEN BURGERS'),
        ('menu_enfant', 'MENU ENFANTS'),
        ('snacks', 'SNACKS'),
        ('sauce', 'SAUCE'),
        ('menu_enfant', 'MENU ENFANTS'),
        ('milk_shakes', 'MILK-SHAKES'),
        ('dessert', 'DESSERTS'),
        ('boissons_eau', 'BOISSONS ET EAU'),
    ], string='Type du produit')














