""""""
import logging
from django.views.generic import View
from django.http import JsonResponse


logger = logging.getLogger()
ID_HEADER = '_'.join(f'{__name__}'.split('.'))


class NotifyDutyOwnerCronHandler(View):
    ID = f'{ID_HEADER}_notify_duty_owner_cron_handler'

    def get(self, _):

        return JsonResponse({'response': 'OK'})
