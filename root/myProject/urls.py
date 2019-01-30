from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # 서버요청 -> 일치하는 urlPattern을 가장 먼저 찾게 됨.
    #path('/', include()),
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
