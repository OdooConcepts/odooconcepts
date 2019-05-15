# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields

class AddModels(models.Model):
    _name = 'add.addmodels'
    _rec_name = 'contrat'
    contrat = fields.Char('Type de contrat ')





