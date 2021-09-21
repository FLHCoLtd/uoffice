""""""
import logging
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from uoffice.apis import NotifyUofCleanDutyHandler
from uoffice.apis import ListEnvVarsHandler
from uoffice.apis import EchoHandler


logger = logging.getLogger(__name__)

urlpatterns = [
    # path('admin/', admin.site.urls),

    # request handlers
    url(r'^notify_uof_clean_duty$', csrf_exempt(NotifyUofCleanDutyHandler.as_view()),
        name=NotifyUofCleanDutyHandler.ID),
    url(r'list_env_vars', csrf_exempt(ListEnvVarsHandler.as_view()),
        name=ListEnvVarsHandler.ID),
    url(r'^echo$', csrf_exempt(EchoHandler.as_view()), name=EchoHandler.ID),
    url(r'^$', csrf_exempt(EchoHandler.as_view()))
]
