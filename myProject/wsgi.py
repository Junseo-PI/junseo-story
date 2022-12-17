# 실제 웹 서버에 배포를 할 때, 설정 파일들을 연결해 주는 파일.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myProject.settings")

application = get_wsgi_application()
