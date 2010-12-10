from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class ClassView(TemplateView):
    template_name = "index.html"


class_based_views = ClassView.as_view()


def function_based_view(request):
    return render_to_response('index.html', {})
