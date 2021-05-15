from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from users.models import UserProfile

admin.site.unregister(User)


class UserPProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [UserPProfileInline, ]


admin.site.register(User, UserProfileAdmin, )

admin.site.site_header = _('PTP 点达系统')
admin.site.site_title = _('PTP 数据管理')

