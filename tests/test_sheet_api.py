from __future__ import print_function
# import os.path
import os
import json
import dotenv

from google.oauth2 import service_account
import googleapiclient.discovery

# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
dotenv.load_dotenv()
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.getenv('SAMPLE_SPREADSHEET_ID')
SAMPLE_RANGE_NAME = os.getenv('SAMPLE_RANGE_NAME')
GCP_SERVICE_ACCOUNT_INFO = os.getenv('GCP_SERVICE_ACCOUNT_INFO')


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    credentials = service_account.Credentials.from_service_account_info(
        json.loads(GCP_SERVICE_ACCOUNT_INFO)
    )

    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

    request = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
    response = request.execute()
    print(f'get sheet value: {response}, type {type(response)}')
    if response.get('values'):
        return response.get('values')[0][0]
    else:
        return None


if __name__ == '__main__':
    main()
