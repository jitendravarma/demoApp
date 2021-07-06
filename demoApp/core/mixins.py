from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class BaseMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if user:
                return HttpResponseRedirect('/home/')
            else:
                return super(BaseMixin, self).dispatch(
                    request, *args, **kwargs)
        else:
            return super(BaseMixin, self).dispatch(
                request, *args, **kwargs)


class CustomTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        user = self.request.user
        if not user.is_anonymous:
            kwargs["fullname"] = user.full_name
            kwargs["logged_in"] = True
        else:
            kwargs["fullname"] = ""
            kwargs["logged_in"] = False
        return kwargs
