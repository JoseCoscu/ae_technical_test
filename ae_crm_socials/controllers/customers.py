from odoo import http, _
from odoo.http import request, content_disposition


class Customers(http.Controller):

    @http.route('/customers', type='http', auth='public', website=True)
    def list_customers(self):
        customers = request.env['res.partner'].sudo().search([])
        return request.render('ae_crm_socials.customers_page', {
            'customers': customers,
        })