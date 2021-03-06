from django.contrib import admin

# Register your models here.
from organizers import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ('application', 'author', 'text')
    list_per_page = 200
    actions = ['delete_selected', ]
    date_hierarchy = 'created_at'


class VoteAdmin(admin.ModelAdmin):
    list_display = ('application', 'user', 'tech', 'personal', 'calculated_vote')
    list_per_page = 200
    list_filter = ('user', 'application')
    search_fields = ('application__user__name', 'application__user__email', 'user__name', 'user__email')
    actions = ['delete_selected', ]


admin.site.register(models.ApplicationComment, admin_class=CommentAdmin)
admin.site.register(models.Vote, admin_class=VoteAdmin)
