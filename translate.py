import requests

def translate(texts):
    IAM_TOKEN = 't1.9euelZqMlo-SkcrIncubx8zNj5iRme3rnpWaj4rMk4nJy8bMmZSSlJKLkMnl8_d-SCFs-e8EegU-_t3z9z53Hmz57wR6BT7-.dnYNNW5gED11SZNTE3oe7N1ibqwIZJyf92UF5MRDHylR36cMwFXOGDvG8xstZ6mtuUS3zuBewumP5Zd800GxCg'
    folder_id = 'b1gu7o5od00898noj0su'
    target_language = 'ru'

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
        json = body,
        headers = headers
    )

    l = response.text

    l = l[37:]
    l = l[:l.index("\"")]
    return l

print(l)

