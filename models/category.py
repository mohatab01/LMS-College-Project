# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import _, api, fields, models
_logger = logging.getLogger(__name__)


class Category(models.Model):
    _name = "category"
    _description = "Book Category"
    _rec_name = "name"
    _order = "id DESC"

    name = fields.Char(string="Category", index=True, tracking=True)
    active = fields.Boolean(string='Active', index=True, default=True)
