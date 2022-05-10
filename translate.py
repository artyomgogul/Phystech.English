import requests

def translate(texts, language = 'ru'):
    IAM_TOKEN = 't1.9euelZrKz5uNm56LyZjNj8yenMeJye3rnpWaj4rMk4nJy8bMmZSSlJKLkMnl8_c1LBZs-e8KWR1P_t3z93VaE2z57wpZHU_-.1VUlj204ehw3PdA6aESDPwX4h-5i1q1zj0r4xn-EbfTP8naOJXclgkn4L6n-oNpyMrwqO4BBmj6J1s5oCxytBw'
    folder_id = 'b1gu7o5od00898noj0su'

    body = {
        "targetLanguageCode": language,
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