# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
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
###############################################################################

{
    'name': "Record the date of sent of quotation request to supplier",
    'description': """
        Adds field "Date sent to supplier" to model of purchase
        orders for allow record the date in which the quotation request is sent
        to supplier. This date is initially registered by the module
        automatically but the user can modify it.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'Purchases',
    'version': '1.0.0',
    'depends': ['purchase', ],
    'data': [
        'views/purchase_view.xml',
    ],
    'demo': [
    ],
}
