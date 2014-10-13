from django.conf.urls import patterns, include
from api import EntryResource
from django.contrib import admin

admin.autodiscover()
entry_resource = EntryResource()

urlpatterns = patterns('',
    (r'^api/', include(entry_resource.urls)),
    (r'^admin/', include(admin.site.urls)),

)
