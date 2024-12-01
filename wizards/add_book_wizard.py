from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AddBookWizard(models.TransientModel):
    _name = 'add.book.wizard'
    _description = 'Wizard for Adding Books'

    title = fields.Char(string="Title", required=True)
    isbn = fields.Char(string="ISBN", required=True, help="13-character ISBN")
    publication_date = fields.Date(string="Publication Date", default=fields.Date.context_today, required=True)
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
    author_id = fields.Many2one('res.partner', string="Author", required=True)
    number_of_copies = fields.Integer(string="Number of Copies", required=True, default=1)

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

    def create_books(self):
        self.ensure_one()
        self.env['product.template'].create({
            'name': self.title,
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author_id.id,
            'publication_date': self.publication_date,
            'category_id': self.category_id.id,
            'number_of_copies': self.number_of_copies,
            'status': 'available',
        })
