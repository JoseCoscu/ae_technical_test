from odoo import http, _
from odoo.http import request, content_disposition


class Customers(http.Controller):

    @http.route('/customers', type='http', auth='public', website=True)
    def list_customers(self):
        search = request.params.get('search')
        customers = request.env['res.partner'].sudo().search([])

        if search:
            domain = ['|', '|',
                       ('name', 'ilike', search),
                       ('email', 'ilike', search),
                       ('comment', 'ilike', search)]

            customers = request.env['res.partner'].sudo().search(domain)


        return request.render('ae_crm_socials.customers_page', {
            'customers': customers,
        })