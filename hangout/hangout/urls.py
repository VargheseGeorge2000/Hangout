
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('social.urls'), name="social"),
    path('account/', include('accounts.urls'), name="accounts"),
]

# Tells where the static files are
urlpatterns += staticfiles_urlpatterns()
# Tells where media url is by accessing settings of url list and the folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
