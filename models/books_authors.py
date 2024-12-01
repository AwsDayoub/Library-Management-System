from odoo import models, fields, api


class BooksAuthors(models.Model):
    _inherit = 'res.partner'


    nationality = fields.Char(string="Nationality")
    place_of_birth = fields.Char(string="Place Of Birth")
    date_of_birth = fields.Date(string="Date Of Birth")
    occupation = fields.Char(string="Occupation")
   