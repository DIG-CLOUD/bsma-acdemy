{
    'name': 'BSMA Website Customizations',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': 'Custom styling and templates for BSMA Academy website',
    'description': """
        Custom website modifications for BSMA Academy including:
        - RTL Arabic support
        - Custom course join popover styling
        - Enhanced CSS for website_slides module
        - Improved responsive design
    """,
    'author': 'BSMA Academy',
    'depends': [
        'base',
        'website',
        'website_slides',
        'portal',
    ],
    'data': [
        'views/courses_views.xml',
        'views/course_card.xml',
        'views/signup_form.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'bsma_website/static/src/css/course_join_popover.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
