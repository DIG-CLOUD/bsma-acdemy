{
    'name': 'BASMA Website',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': 'Custom website module for BSMA education platform.',
    'description': """
        This module customizes the website slides module for BSMA education platform.
        It replaces the courses_all template with a responsive Arabic design.
    """,
    'author': 'BSMA',
    'website': '',
    'depends': ['website_slides', 'website'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'bsma_website/static/src/css/bsma_website.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
