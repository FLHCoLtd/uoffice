""""""
import os
import json
from django.http import JsonResponse
from django.views.generic import View
import django.conf


ID_HEADER = '_'.join(f'{__name__}'.split('.'))


class EchoHandler(View):
    """"""
    ID = f'{ID_HEADER}_echo_handler'

    def get(self, _):
        response = {
            'echo': 'OK',
            'ID': f'{self.ID}',
        }
        if django.conf.settings.DEBUG:
            response.update({
                'DEBUG MODE': django.conf.settings.DEBUG,
                'GOOGLE_CLOUD_PROJECT': os.getenv('GOOGLE_CLOUD_PROJECT'),
                'GAE_APPLICATION': os.getenv('GAE_APPLICATION')
            })
        return JsonResponse(response)

    @staticmethod
    def post(request):
        try:
            payload = json.loads(request.body.decode('utf-8'))
            return JsonResponse(payload)
        except json.JSONDecodeError as err:
            return JsonResponse({'error': f'{err}'})
