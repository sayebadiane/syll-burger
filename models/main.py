import json
import logging
from datetime import datetime

from psycopg2.errors import LockNotAvailable
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.urls import url_decode, url_encode, url_parse

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.exceptions import AccessError, MissingError, UserError, ValidationError
from odoo.fields import Command
from odoo.http import request, route
from odoo.tools import SQL, lazy, str2bool

from odoo.addons.base.models.ir_qweb_fields import nl2br_enclose
from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers import portal as payment_portal
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.addons.website.controllers import main
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.addons.sale.controllers import portal as sale_portal
from odoo.osv import expression
from odoo.tools.json import scriptsafe as json_scriptsafe


class WebsiteSale(payment_portal.PaymentPortal):
    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(
        self, product_id, add_qty=1, set_qty=0,
        product_custom_attribute_values=None, no_variant_attribute_values=None,
        express=False, **kwargs
    ):
        """This route is called when adding a product to cart (no options)."""
        sale_order = request.website.sale_get_order(force_create=True)
        if sale_order.state != 'draft':
            request.session['sale_order_id'] = None
            sale_order = request.website.sale_get_order(force_create=True)

        if product_custom_attribute_values:
            product_custom_attribute_values = json_scriptsafe.loads(product_custom_attribute_values)

        if no_variant_attribute_values:
            no_variant_attribute_values = json_scriptsafe.loads(no_variant_attribute_values)

        sale_order._cart_update(
            product_id=int(product_id),
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values,
            **kwargs
        )

        request.session['website_sale_cart_quantity'] = sale_order.cart_quantity

        delivery_option = kwargs.get('delivery_option')
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",delivery_option)
        print(delivery_option)
        delivery_option ='onsite'

        # if delivery_option == 'delivery':
        #     return request.redirect("/shop/checkout?express=1")
        # elif delivery_option == 'onsite':
        #     return request.redirect("/shop/payment")

        # Existing logic or default redirection if delivery_option is not handled
        # if express:
        #     return request.redirect("/shop/checkout?express=1")
        if express:
            return request.redirect("/shop/payment")

        return request.redirect("/shop/cart")
