# -*- coding: utf-8 -*-
# from odoo import http


# class BaseAgata(http.Controller):
#     @http.route('/base_agata/base_agata', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_agata/base_agata/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_agata.listing', {
#             'root': '/base_agata/base_agata',
#             'objects': http.request.env['base_agata.base_agata'].search([]),
#         })

#     @http.route('/base_agata/base_agata/objects/<model("base_agata.base_agata"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_agata.object', {
#             'object': obj
#         })
