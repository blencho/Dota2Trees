from django.conf.urls import patterns, include, url

from pubWeb import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pubstompr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
)
