# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Domsense s.r.l. (<http://www.domsense.com>).
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

{
    'name': 'Input/Output Tax Report for SQP (Oct 14)',
    'version': '1.0',
    'category': 'Thai Localisation',
    'description': """
    
    """,
    'author': 'Ecosoft',
    'website': 'http://www.ecosoft.co.th',
    'depends': ['account','jasper_reports','web_m2o_enhanced','advance_and_additional_discount'],
    'init_xml': [],
    'update_xml': [
        "reports.xml",
        "wizard/sqp_report_thai_tax_wizard.xml",
    ],
    'demo_xml': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
