from odoo import models, fields, api
from werkzeug import urls


class Partner(models.Model):
    _inherit = 'res.partner'

    linkedin_url = fields.Char(string='Linkedin URL')
    facebook_url = fields.Char(string='Facebook URL')
    twitter_url = fields.Char(string='Twitter URL')

    def write(self, vals):
        if vals.get('linkedin_url'):
            vals['linkedin_url'] = self._clean_social_url(vals['linkedin_url'])
        if vals.get('facebook_url'):
            vals['facebook_url'] = self._clean_social_url(vals['facebook_url'])
        if vals.get('twitter_url'):
            vals['twitter_url'] = self._clean_social_url(vals['twitter_url'])
        return super().write(vals)

    @api.model
    def _clean_social_url(self, social_url):
        url = urls.url_parse(social_url)
        if not url.scheme:
            if not url.netloc:
                url = url.replace(netloc=url.path, path='')
            social_url = url.replace(scheme='http').to_url()
        return social_url
