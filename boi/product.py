# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class product_product(osv.osv):

    _inherit = 'product.product'

    _columns = {
        'boi_lines': fields.one2many('boi.certificate.line', 'product_id', 'BOI Certificate'),
        'thick': fields.selection([
            ('thick25', 25),
            ('thick42', 42),
            ('thick50', 50),
            ('thick75', 75),
            ('thick100', 100),
            ('thick125', 125),
            ('thick150', 150),
            ('thick200',200),
            ], 'Thick', select=True,
        ),
    }

product_product()
