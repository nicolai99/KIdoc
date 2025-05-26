"""
URL configuration for dmsAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db import IntegrityError
from django.urls import path
from dmsAPI.views.archive import archiveRouter
from dmsAPI.views.auth import authRouter
from dmsAPI.views.pdf import pdfRouter
from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth)
api.add_router("/upload", pdfRouter)
api.add_router("/auth", authRouter)
api.add_router("/archives", archiveRouter)


@api.exception_handler(IntegrityError)
def objectExists(request, exc):
    return api.create_response(request, status=409, data={"message": "Object must be unique", "exception": str(exc)})


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("api/", api.urls),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
