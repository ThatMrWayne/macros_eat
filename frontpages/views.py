from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"
    redirect_to = "record"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return redirect(self.redirect_to)

        return super().dispatch(request, *args, **kwargs)


class RecordPageView(TemplateView):
    template_name = "record.html"
    redirect_to = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        remind_cookie = self.request.COOKIES.get('remind', 'no')
        context['remind'] = remind_cookie
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user is None or not request.user.is_authenticated:
            return redirect(self.redirect_to)

        response = super().dispatch(request, *args, **kwargs)
        response.delete_cookie('remind')
        return response
