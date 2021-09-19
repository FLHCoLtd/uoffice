""""""
import logging
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from uoffice.apis import NotifyDutyOwnerCronHandler
from uoffice.apis import EchoHandler


logger = logging.getLogger(__name__)

urlpatterns = [
    # path('admin/', admin.site.urls),

    # request handlers
    url(r'^notify_duty_owner$', csrf_exempt(NotifyDutyOwnerCronHandler.as_view()),
        name=NotifyDutyOwnerCronHandler.ID),
    url(r'^echo$', csrf_exempt(EchoHandler.as_view()), name=EchoHandler.ID),
    url(r'^$', csrf_exempt(EchoHandler.as_view()))
]
