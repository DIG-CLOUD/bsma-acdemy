from odoo import models, fields
from odoo.http import request


class WebsiteSlides(models.Model):
    _inherit = 'slide.channel'
    _description = 'Website Slide Channel'

    target_age = fields.Char(string='Target Age')
    duration_hours = fields.Integer(string='Duration (Hours)')
    duration_weeks = fields.Integer(string='Duration (Weeks)')
    course_price = fields.Float(string='Course Price', digits='Product Price')
    start_date = fields.Date(string='Start Date')