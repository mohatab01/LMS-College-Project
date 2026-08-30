# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging
from datetime import timedelta
_logger = logging.getLogger(__name__)


class Student(models.Model):
    _description = 'Students'
    _rec_name = 'name'
    _order = 'id DESC'
    _name = 'student'

    name = fields.Char(string="Student Name", required=True, index=True)
    id_number = fields.Char(string="ID Number", required=True, index=True)
    phone = fields.Char(string="Phone", required=True, index=True)
    email = fields.Char(string="Email Address", index=True)



