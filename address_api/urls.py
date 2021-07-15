from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import (
    path, include, re_path
)

urlpatterns = [
    path('admin_page/', admin.site.urls),
    path('', include('front.urls')),
    path('api/v1/', include('api_v1.urls')),
    # path('front/', RedirectView.as_view(url='', permanent=False)),
    # path('front/', include('v2_front_base.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
