from django.contrib import admin
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # projects
    url(r'^project/$',
        'libreqda.views.browse_projects',
        name='browse_projects'),
    # accounts
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/accounts/login'}),
)
