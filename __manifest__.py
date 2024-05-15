# © 2024 Erre Elle Net s.r.l. (<https://erre-elle.net>)
# License LGPL-3 - See https://www.gnu.org/licenses/lgpl-3.0.html
{
    'name': 'Plugin that add the possibility to use groups to exclude users from filters.',
    'author': 'Erre Elle Net s.r.l.',
    'maintainer': 'Erre Elle Net s.r.l.',
    'version': '16.0.1.2.0',
    'category': 'Tools',
    'website': 'https://github.com/RLTravis/filter_multi_user_with_exception',
    'depends': [
        'filter_multi_user',
    ],
    "data": [
        "views/ir_filters_view.xml",
    ],
    'license': 'LGPL-3',
    'installable': True,
}
