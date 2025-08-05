# -*- coding: utf-8 -*-
# from odoo import http


# class SisLearning(http.Controller):
#     @http.route('/sis_learning/sis_learning', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sis_learning/sis_learning/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sis_learning.listing', {
#             'root': '/sis_learning/sis_learning',
#             'objects': http.request.env['sis_learning.sis_learning'].search([]),
#         })

#     @http.route('/sis_learning/sis_learning/objects/<model("sis_learning.sis_learning"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sis_learning.object', {
#             'object': obj
#         })

