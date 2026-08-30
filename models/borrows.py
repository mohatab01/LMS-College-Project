# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging
from datetime import timedelta
_logger = logging.getLogger(__name__)


class Borrows(models.Model):
    _description = 'Borrows'
    _rec_name = 'book_id'
    _order = 'id DESC'
    _name = 'borrows'

    student_id = fields.Many2one('student', string='Student')
    user_id = fields.Many2one('res.users', string='User')
    book_id = fields.Many2one('book', string='Book')
    borrow_date = fields.Date(string="Borrow Date", required=True)
    return_date = fields.Date(string="Return Date", compute='calc_return_date')
    is_returned = fields.Boolean(string='Is Returned', default=False, tracking=True)

    def calc_return_date(self):
        for rec in self:
            if rec.borrow_date:
                rec.return_date = rec.borrow_date + timedelta(days=5)
            else:
                rec.return_date = False

    def return_book(self):
        for rec in self:
            rec.is_returned = True
