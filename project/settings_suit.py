# -*- coding: utf-8 -*-

from __future__ import unicode_literals

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Hello Blog',
    'HEADER_DATE_FORMAT': 'l, j E Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # menu
    'SEARCH_URL': '',
    'MENU': (
        '-',
        {'label': 'Blog', 'permissions': 'hello_blog.change_note', 'models': [
            {'label': 'Notes', 'permissions': 'hello_blog.change_note', 'url': '/admin/hello_blog/note/'},
            {'label': 'Categories', 'permissions': 'hello_blog.change_category', 'url': '/admin/hello_blog/category/'},
        ]},
        '-',
        {'label': 'Auth', 'permissions': 'auth.add_user', 'models': [
            {'label': 'Users', 'permissions': 'auth.add_user', 'url': '/admin/auth/user/'},
            {'label': 'Groups', 'permissions': 'auth.add_group', 'url': '/admin/auth/group/'},
        ]},
    ),

    # misc
    'LIST_PER_PAGE': 25,
    'CONFIRM_UNSAVED_CHANGES': False,
}
