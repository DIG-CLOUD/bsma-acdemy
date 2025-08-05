# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sis_learning(models.Model):
    _inherit = 'op.batch'

    student_id = fields.Many2one(
        comodel_name='op.student',
        string='Students',
        required=False)

    istructor_id = fields.Many2one(
        comodel_name='op.faculty',
        string='Istructor',
        required=False)