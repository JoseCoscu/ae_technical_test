{
    'name': 'CRM Socials',
    'summary': 'CRM Socials',
    'description': """
                   """,
    'category': 'Sales/CRM',
    'author': 'Juan Jose',
    'version': '18.0.0.0.1',

    'depends': ['base','crm',"web", 'website', 'portal'],
    'data': ["views/res_partner_views.xml",
             "views/website_customers.xml"],
    'installable': True,
    'auto_install': False,
    'application': True,
}
