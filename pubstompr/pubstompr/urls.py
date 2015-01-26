from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pubstompr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^pubWeb/', include('pubWeb.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
