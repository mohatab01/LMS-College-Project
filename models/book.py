# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
import logging
_logger = logging.getLogger(__name__)


class Book (models.Model):
    _description = 'Book'
    _rec_name = 'isbn'
    _order = 'id DESC'
    _name = 'book'

    isbn = fields.Char(string="ISBN", required=True, index=True, tracking=True)
    title = fields.Char(string="Title", required=True, index=True, tracking=True)
    description = fields.Text(string="Description")
    edition = fields.Char(string="Edition")
    location = fields.Char(string="Location")
    auther_name = fields.Char(string="Auther Name")
    thumbnail = fields.Binary(string="Attachment")
    category_id = fields.Many2one('category', string='Category')
    is_borrowed = fields.Char(compute='check_if_book_borrowed', default=False)

    def check_if_book_borrowed(self):
        for rec in self:
            borrow_rec = self.env['borrows'].search([('book_id', '=', rec.id), ('is_returned', '=', False)], limit=1)
            if borrow_rec:
                rec.is_borrowed = False
            else:
                rec.is_borrowed = True
