import requests

def translate(texts, language):
    IAM_TOKEN = 't1.9euelZqWmJOWx8bMjszKi5XOy5qTz-3rnpWaj4rMk4nJy8bMmZSSlJKLkMnl8_ceDRps-e9VPUEo_N3z9147F2z571U9QSj8.OCiGo0h7qv2Zk9inNAe1P7FEro19oSa4Hdl3mM1WaaV2ENktXT4jzlYCtuDpcm8NOa9AeWTPUyuXUH50CPGhDg'
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
