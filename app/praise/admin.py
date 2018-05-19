from django.contrib import admin

from praise.models import Praise, PraiseHistory


@admin.register(Praise)
class PraiseAdmin(admin.ModelAdmin):
    pass


@admin.register(PraiseHistory)
class PraiseHistoryAdmin(admin.ModelAdmin):
    pass
