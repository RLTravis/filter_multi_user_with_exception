# © 2024 Erre Elle Net s.r.l. (<https://erre-elle.net>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class IrFilters(models.Model):
    _inherit = 'ir.filters'
    except_group_ids = fields.Many2many(
        string='Except for Groups',
        comodel_name='res.groups',
        relation='filter_groups_rel',
        column1='filter_id',
        column2='group_id'
    )

    @api.constrains('except_group_ids', 'except_group_ids.users')
    def _compute_user_ids(self):
        super()._compute_user_ids()

        for rec in self:
            rec.user_ids -= rec.except_group_ids.users
