from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'visualize.views.home', name='home'),
    url(r'^PlotDistribution/', include('PlotDistribution.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
