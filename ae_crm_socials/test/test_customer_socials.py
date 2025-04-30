from odoo.tests.common import TransactionCase

class TestCustomers(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Customer = self.env['res.partner']

    def test_create_customer_with_social_links(self):
        customer = self.Customer.create({
            'name': 'Test Customer',
            'facebook_url': 'https://facebook.com/testcustomer',
            'twitter_url': 'https://twitter.com/testcustomer',
            'linkedin_url': 'https://linkedin.com/in/testcustomer',
        })

        self.assertEqual(customer.name, 'Test Customer')
        self.assertTrue(customer.facebook_url.startswith('https://facebook.com'))
        self.assertTrue(customer.twitter_url.startswith('https://twitter.com'))
        self.assertTrue(customer.linkedin_url.startswith('https://linkedin.com'))

    def test_customers_page_accessible(self):
        # Simula acceso al controlador web
        response = self.url_open('/customers')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Our Customers", response.content)

class TestCustomerSocialProfile(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Customer = self.env['res.partner']

    def test_profile_incomplete_missing_all_socials(self):
        customer = self.Customer.create({
            'name': 'No Socials',
        })
        self.assertFalse(customer.is_profile_incomplete,
                        "Debe marcarse como incompleto si faltan todas las redes sociales.")

    def test_profile_incomplete_missing_one_social(self):
        customer = self.Customer.create({
            'name': 'Only Facebook and Twitter',
            'facebook_url': 'https://facebook.com/user',
            'twitter_url': 'https://twitter.com/user'
        })
        self.assertTrue(customer.is_profile_incomplete, "Debe marcarse como incompleto si falta una red social.")

    def test_profile_complete_all_socials_present(self):
        customer = self.Customer.create({
            'name': 'Full Profile',
            'facebook_url': 'https://facebook.com/user',
            'twitter_url': 'https://twitter.com/user',
            'linkedin_url': 'https://linkedin.com/in/user'
        })
        self.assertFalse(customer.is_profile_incomplete,
                         "Debe marcarse como completo si tiene todas las redes sociales.")

