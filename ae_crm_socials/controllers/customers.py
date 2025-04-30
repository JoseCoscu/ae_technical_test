from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import pager


class Customers(http.Controller):
    _items_per_page = 10

    def _get_searchbar_inputs(self):
        return {
            'name': {'input': 'name', 'label': _('Name'), 'sequence': 50},
            'email': {'input': 'email', 'label': _('Email'), 'sequence': 30},
        }

    def _get_customers_searchbar_filters(self):
        return {
            'all': {'label': _('All'), 'domain': []},
            'facebook': {'label': _('Facebook'), 'domain': ('facebook_url', '!=', False)},
            'twitter': {'label': _('Twitter'), 'domain': ('twitter_url', '!=', False)},
            'linkedin': {'label': _('Linkedin'), 'domain': ('linkedin_url', '!=', False)},
        }

    @http.route(['/customers', '/customers/page/<int:page>'], type='http', auth='user', website=True)
    def list_customers(self, page=1, filterby=None, search=None, search_in=None, **kwargs):
        customer_obj = request.env['res.partner']
        total_customers = customer_obj.search_count([])
        searchbar_filters = self._get_customers_searchbar_filters()
        searchbar_inputs = self._get_searchbar_inputs()
        domain = []

        if not search_in:
            search_in="name"

        if search and search_in:
            domain.append((search_in, 'ilike', search))

        if filterby and filterby != 'all':
            domain.append(searchbar_filters.get(filterby, searchbar_filters.get('all'))['domain'])
        url_args = {'search': search, 'filterby': filterby}

        pager_values = pager(
            url="/customers",
            total=total_customers,
            page=page,
            step=self._items_per_page,
            url_args=url_args,
        )
        customers = customer_obj.search(domain, limit=self._items_per_page,
                                        offset=pager_values['offset'])

        return request.render('ae_crm_socials.customers_page', {
            'customers': customers,
            'pager': pager_values,
            'searchbar_filters': searchbar_filters,
            'searchbar_inputs': searchbar_inputs,
            'filterby': filterby,
            'search_in': search_in,
            'search': search,
            'default_url': '/customers',
        })
