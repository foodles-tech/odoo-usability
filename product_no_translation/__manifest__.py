# -*- encoding: utf-8 -*-
##############################################################################
#
#    Product No Translation module for Odoo
#    Copyright (C) 2014 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
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
    'name': 'Product no Translation',
    'version': '14.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'summary': 'For companies that work with only one language',
    'description': """
This module sets the translatable fields of the product object (name,
descriptions) to non-translatable fields.

This change is usefull for companies that work with only one language.
And it reduces the start time of the Point of Sale !
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['product'],
    'installable': False,
}
