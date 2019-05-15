# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _inherit = 'hr.employee'

    custom_name = fields.Char(string='Record Name: ')

    @api.multi
    def name_get(self):
        result = []
        name = ''
        for record in self:
            if record.name:
                name = str(record.custom_name)
            result.append((record.id, name))
        return result
