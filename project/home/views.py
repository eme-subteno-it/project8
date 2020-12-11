""" All views for the home application """
from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name)


class LegalNoticeView(View):
    template_name = 'home/legal_notice.html'

    def get(self, request):
        return render(request, self.template_name)
