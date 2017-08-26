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

from datetime import datetime

from openerp import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    date_sent_to_supplier = fields.Datetime('Date sent to supplier')

    @api.multi
    def action_rfq_send(self):
        self.write({'date_sent_to_supplier': datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')})
        return super(PurchaseOrder, self).action_rfq_send()
