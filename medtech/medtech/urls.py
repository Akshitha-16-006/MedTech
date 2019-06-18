"""medtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path
from medtechapp import views
from django.conf import settings
# from .
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('homeremedies/',views.homeremedies,name='homeremedies'),
    path('admin/', admin.site.urls),
    # path('signup/',views.signup,name="signup"),
    path('',include('medtechapp.urls')),
    re_path(r' ^homeremedies/(?P<solutions_id>[0-9]+)/$',views.display,name="display"),

    #  path('add_hosp_form_submission/',views.add_hosp_form_submission,name='add_hosp_form_submission' ),
    
    # path('logout/',views.logout_request,name="logout"),


]
# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
