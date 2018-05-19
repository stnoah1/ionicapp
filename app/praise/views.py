from random import randint

from django.db.models import Count
from django.views.generic import TemplateView

from praise.models import Praise


class PraiseSelectView(TemplateView):
    template_name = "praise/give_praise.html"

    def get_context_data(self, **kwargs):
        # 1. Get random praise
        count = Praise.objects.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        praise = Praise.objects.all()[random_index]

        # 2. Get 4 random friends


        context = super().get_context_data(**kwargs)
        context.update({'praise': '', 'friends': []})
        return context

    def get_success_url(self):
        messages.success(self.request, "회원정보가 수정되었습니다.")
        return reverse('settings:member_update')
