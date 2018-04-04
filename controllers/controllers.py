# -*- coding: utf-8 -*-
from odoo import http

# class Havana(http.Controller):
#     @http.route('/havana/havana/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/havana/havana/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('havana.listing', {
#             'root': '/havana/havana',
#             'objects': http.request.env['havana.havana'].search([]),
#         })

#     @http.route('/havana/havana/objects/<model("havana.havana"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('havana.object', {
#             'object': obj
#         })