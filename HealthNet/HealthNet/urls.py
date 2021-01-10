from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = (
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('health.urls', namespace='health'))
)
