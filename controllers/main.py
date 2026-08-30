# -*- coding: utf-8 -*-

import collections
import babel.dates
import requests
import shutil
import werkzeug
import logging
from werkzeug.datastructures import OrderedMultiDict
from werkzeug.exceptions import NotFound

from ast import literal_eval
from collections import defaultdict
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import fields, http, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.event.controllers.main import EventController

from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home

from odoo.http import request
from odoo.osv import expression
from odoo.tools.misc import get_lang, format_date

import mimetypes
from odoo.tools.mimetypes import guess_mimetype

import base64
import json
import sys
import ast
import re
_logger = logging.getLogger(__name__)


class WebsiteLMSController(Home):

    @http.route(['/', '/category/<string:category_id>'], type='http', auth="public", website=True, sitemap=True)
    def home(self, category_id=False, search=False):
        domain_search = []
        if category_id:
            domain_search.append(('category_id', '=', int(category_id)))
        if search:
            domain_search.append(('title', 'ilike', search))
        book_recs = request.env['book'].search(domain_search)
        category_recs = request.env['category'].search([])
        books = []
        for book in book_recs:
            books.append({
                'isbn': book.isbn,
                'title': book.title,
                'description': book.description,
                'edition': book.edition,
                'auther_name': book.auther_name,
                'thumbnail': book.thumbnail,
                'category': book.category_id.name,
                'is_borrowed': book.is_borrowed,
            })
        values = {
            'books': books,
            'books_count': len(books),
            'categories': category_recs,
            'category_id': int(category_id) if category_id else False,
            'search': search if search else False,
        }
        return request.render("lms.home", values)
