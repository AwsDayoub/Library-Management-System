from odoo import models, fields, api



class BooksCategory(models.Model):
    _name = 'books.category'

    name = fields.Selection(
        [
            ('fiction', 'Fiction'),
            ('non_fiction', 'Non-Fiction'),
            ('science', 'Science'),
            ('history', 'History'),
            ('biography', 'Biography'),
            ('fantasy', 'Fantasy'),
            ('romance', 'Romance'),
        ],
        string="Category",
        required=True,
    )

