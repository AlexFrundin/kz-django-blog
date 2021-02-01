
urls = [
    {'stable/user/':
        {'v1': ('users.urls'),
         'latest': ('users.v2.urls')}},
    {'stable/user/':
        {'v1': ('user_profile.urls'),
         'latest': None}},
    {'stable/user/content/':
        {'v1': ('content.urls'),
         'latest': None}},

    {'stable/user/causes/':
        {'v1': ('causes_subcauses.urls'),
         'latest': ('causes_subcauses.v2.urls')}},
    {'stable/user/interest/':
        {'v1': ('user_interest.urls'),
         'latest': ('user_interest.v2.urls')}},
    {'stable/other/user/':
        {'v1': ('other_user_profile.urls'),
         'latest': None}},
    {'stable/user/notification/':
        {'v1': ('notifications.urls'),
         'latest': None}},
    {'stable/user/chat/':
        {'v1': ('chat.urls'),
         'latest': None}},

    # Admin URLs
    {'stable/admin/user/':
        {'v1': ('admin_users.urls'),
         'latest': None}},
    {'stable/user/post/':
        {'v1': ('post.urls'),
         'latest': None}},
    {'stable/user/explore/':
        {'v1': ('post_explore.urls'),
         'latest': None}},
    {'stable/admin/post/':
        {'v1': ('admin_post.urls'),
         'latest': None}},
    {'stable/admin/causes/':
        {'v1': ('admin_causes.urls'),
         'latest': None}},
    {'stable/admin/report/management/':
        {'v1': ('admin_report_management.urls'),
         'latest': None}},
    {'stable/admin/reports/':
        {'v1': ('admin_post_reports.urls'),
         'latest': None}},
    {'stable/admin/content/moderation/':
        {'v1': ('admin_content_moderation.urls'),
         'latest': None}}

]


def get_include(url):
    try:
        return url, {'latest': (urls[url]['latest'])}
    except KeyError:
        return url, {'latest': (urls[url]['stable'])}
