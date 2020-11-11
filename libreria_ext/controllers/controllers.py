# -*- coding: utf-8 -*-
# from odoo import http


# class LibreriaExt(http.Controller):
#     @http.route('/libreria_ext/libreria_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria_ext/libreria_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria_ext.listing', {
#             'root': '/libreria_ext/libreria_ext',
#             'objects': http.request.env['libreria_ext.libreria_ext'].search([]),
#         })

#     @http.route('/libreria_ext/libreria_ext/objects/<model("libreria_ext.libreria_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria_ext.object', {
#             'object': obj
#         })
