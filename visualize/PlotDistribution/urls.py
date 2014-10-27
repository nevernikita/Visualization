from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^home$', 'PlotDistribution.views.home'),
    url(r'^Plot', 'PlotDistribution.views.Plot'),
    url(r'^Update', 'PlotDistribution.views.Update'),
)
