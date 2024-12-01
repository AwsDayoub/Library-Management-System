from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    book_id = fields.Many2one('product.product', string='Book') 
    is_book = fields.Boolean('Is Book')
    is_paid_or_in_payment = fields.Boolean(string="Paid or In Payment", compute="_compute_is_paid_or_in_payment")

    @api.depends('invoice_ids', 'invoice_ids.payment_state')
    def _compute_is_paid_or_in_payment(self):
        for order in self:
            paid_or_in_payment = all(
                invoice.payment_state in ['paid', 'in_payment'] for invoice in order.invoice_ids
                if invoice.state not in ('draft', 'cancel')
            )
            order.is_paid_or_in_payment = paid_or_in_payment


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    book_id = fields.Many2one(
        'product.product', 
        string="Book", 
        domain="[('sale_ok', '=', True), ('type', '=', 'product')]" 
    )

    @api.onchange('book_id')
    def _onchange_book_id(self):
        if self.book_id:
            self.product_id = self.book_id
            self.name = self.book_id.name
            self.price_unit = self.book_id.list_price
