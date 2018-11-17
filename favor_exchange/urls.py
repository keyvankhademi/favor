from django.conf.urls import url

from favor_exchange.views import homepage, signup, favor_request, add_credit

urlpatterns = [
    url(r'^$', homepage, name='index'),
    url(r'^signup/$', signup, name='auth_signup'),
    url(r'^favor-request/$', favor_request, name='favor_request'),
    url(r'^add-credit/$', add_credit, name='add_credit'),
]
