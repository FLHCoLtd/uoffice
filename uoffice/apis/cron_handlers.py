""""""
import os
import json
import uuid
import logging
import googleapiclient.discovery
import dotenv
import requests
from datetime import date
from django.views.generic import View
from django.http import JsonResponse
from google.oauth2 import service_account

logger = logging.getLogger()
dotenv.load_dotenv()
gcp_account_info = os.getenv('GCP_SERVICE_ACCOUNT_INFO')
sheet_url = os.getenv('SPREADSHEET_URL')
sheet_id = os.getenv('SPREADSHEET_ID')
sheet_range = os.getenv('SPREADSHEET_RANGE_NAME')
line_token = os.getenv('LINE_NOTIFY_TOKEN')
line_api_url = os.getenv('LINE_NOTIFY_API_URL')


def get_today_on_duty_name_n_team():
    """Query goodle spreadsheet for on duty name/team of the day"""
    # print(f'gcp_account_info {json.loads(gcp_account_info)}')
    if not gcp_account_info:
        raise ValueError('No GCP_SERVICE_ACCOUNT_INFO')
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(gcp_account_info)
    )
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    request = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=sheet_range)
    response = request.execute()
    return response.get('values')[0][0]


class NotifyUofCleanDutyHandler(View):
    """Query duty owner name from google sheet and push notification to line group"""
    ID = f'{uuid.uuid4()}'

    def get(self, _):
        duty = get_today_on_duty_name_n_team()
        logger.debug(f'on duty: {duty}')
        if not duty:
            logger.warning(f'No duty for today {date.today()} office clean job.')
            return JsonResponse({'response': 'OK'})

        msg = f'[測試]本日[{date.today()}]二樓辦公室值日生：\n{duty}\n\n查詢輪值表：{sheet_url}\n'
        if not self.send_line_push_msg(msg):
            logger.error('send_line_push_msg api fail')
        return JsonResponse({'notification': f'{msg}'})

    def send_line_push_msg(self, msg):
        payload = {'message': msg}
        headers = {'Authorization': f'Bearer {line_token}'}
        logger.debug(f'send_line_push_msg payload {payload}')
        # r = requests.post(self.line_api_url, headers=headers, data=payload)
        # if r.status_code == requests.codes.ok:
        #     return payload
        # else:
        #     logger.warning(f'Line notify api post error code {r.status_code}\n{r.content}')
        #     return None
        return payload


class QueryOnDutyHandler(View):
    ID = str(uuid.uuid1())

    def get(self, _):
        result = get_today_on_duty_name_n_team()
        logger.debug(f'query result {result}')
        return JsonResponse({'onDuty': f'{result}'})


class ListEnvVarsHandler(View):
    ID = f'{uuid.uuid4()}'

    def get(self, _):
        payload = {}
        keys = [
            'SPREADSHEET_URL',
            'SPREADSHEET_ID',
            'SPREADSHEET_RANGE_NAME',
            'LINE_NOTIFY_TOKEN',
            'LINE_NOTIFY_API_URL',
            'GCP_SERVICE_ACCOUNT_INFO',
        ]
        for key in keys:
            payload[key] = os.environ.get(key)[:10]
        return JsonResponse(payload)
