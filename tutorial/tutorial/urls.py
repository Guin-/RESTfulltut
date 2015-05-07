from django.conf.urls import include, url
from django.contrib import admin
import snippets
from snippets import urls

urlpatterns = [
    url(r'^', include(snippets.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
