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

    @api.depends('except_group_ids', 'except_group_ids.users')
    def _compute_user_ids(self):
        super()._compute_user_ids()

        for rec in self:
            rec.user_ids -= rec.except_group_ids.users

    @api.model
    def get_filters(self, model, action_id=None):
        # WARNING: this function overrides the standard one.
        # The only change done is in the domain used to search the filters.

        action_domain = self._get_action_domain(action_id)
        action_domain += [
            (
                'model_id',
                '=',
                model,
            ),
            '|',
            (
                'user_id',
                '=?',
                self._uid,
            ),
            (
                'user_ids',
                'in',
                self._uid,
            ),
        ]

        filters = self.search(action_domain)
        user_context = self.env['res.users'].context_get()

        return filters.with_context(**user_context).read(
            [
                'name',
                'is_default',
                'domain',
                'context',
                'user_id',
                'sort',
            ]
        )
