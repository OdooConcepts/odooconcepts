# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def on_change_partnerid(self):
        if self.partner_id:
            self.order_line = [(0,0,{'product_id':1})]
            return {'value': {'order_line': [(0,0,{'product_id':1})]}}


