"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.http import HttpResponse
import json

from .views import ConvView

# from django.contrib import admin
usage = "Usage: main_url/float_number/lang_code/. Example http://example.com/num2words/-37345.66/PL/ or" \
        " http://127.0.0.1:8000/num2words/-37345.66/"

urlpatterns = [
    url(r'(?P<number>[-.\w]+)/(?P<lang>\w{5})/$',ConvView.as_view(), name='num2words'),
    url(r'(?P<number>[-.\w]+)/$',ConvView.as_view(), name='num2words'),
    url(r'', lambda r: HttpResponse(json.dumps({'error': usage}),  content_type="application/json")),
    # url(r'^admin/', admin.site.urls),
]