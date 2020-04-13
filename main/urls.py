from django.urls import path, include
from .views import *

urlpatterns = [
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^branch/', include('bankapi.urls')),
	re_path(r'^ifsc/', include('bankapi.urls')),
]



