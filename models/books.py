from odoo import models, fields, api
from odoo.exceptions import ValidationError


# 9781861972712

class Books(models.Model):
    _inherit = 'product.template'

    isbn = fields.Char(string="ISBN", required=True, help="13-character ISBN")
    title = fields.Char(string='Title', required=True, tracking=True, store=True)
    author = fields.Many2one('res.partner', string="Categories", ondelete='set null')
    publication_date = fields.Date(string='Publication Date', required=True, default=fields.Datetime.now,store=True)
    category_id = fields.Many2one('books.category', string="Category", ondelete='set null')
    category_selection = fields.Selection(
        [
            ('fiction', 'Fiction'),
            ('non_fiction', 'Non-Fiction'),
            ('science', 'Science'),
            ('history', 'History'),
            ('biography', 'Biography'),
            ('fantasy', 'Fantasy'),
            ('romance', 'Romance'),
        ],
        string="Category Selection",
    )
    number_of_copies = fields.Integer(string='Number Of Copies', store=True, tracking=True)



    status = fields.Selection(
        [('available', 'Available'), ('borrowed', 'Borrowed')], default='available'
    )


    @api.onchange('category_selection')
    def _onchange_category_selection(self):
        if self.category_selection:
            category_mapping = {
                'fiction': 1,
                'non_fiction': 2,
            }
            self.category_id = category_mapping.get(self.category_selection)



    @api.constrains('isbn')
    def _check_isbn(self):
        for record in self:
            if len(record.isbn) != 13 or not record.isbn.isdigit():
                raise ValidationError("The ISBN must be a 13-digit number.")
            
            if not self._is_valid_isbn13(record.isbn):
                raise ValidationError("The ISBN is not valid.")


    def _is_valid_isbn13(self, isbn):
        total = 0
        for index, char in enumerate(isbn):
            digit = int(char)
            if index % 2 == 0:
                total += digit
            else:
                total += 3 * digit
        return total % 10 == 0






