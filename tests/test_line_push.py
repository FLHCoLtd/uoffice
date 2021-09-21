""""""
import os
import requests
import dotenv

dotenv.load_dotenv()
LINE_NOTIFY_TOKEN = os.getenv('LINE_NOTIFY_TOKEN')
LINE_NOTIFY_API_URL = os.getenv('LINE_NOTIFY_API_URL')


def main():
    """$ curl -X POST -H 'Authorization: Bearer <access_token>' \
        -F 'message=foobar' https://notify-api.line.me/api/notify
                {"status":200,"message":"ok"}
    """
    message = 'this is api test, ignore it.'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer {}'.format(LINE_NOTIFY_TOKEN)}
    print(f'payload: {payload}')
    r = requests.post(LINE_NOTIFY_API_URL, headers=headers, data=payload)
    if r.status_code == requests.codes.ok:
        return payload
    else:
        print(f'line notify api post error code {r.status_code}\n{r.content}')
        return None


if __name__ == '__main__':
    main()
