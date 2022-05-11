import requests

def translate(texts, language = 'ru'):
    IAM_TOKEN = 't1.9euelZqJm5aVjJzPj5qTl5bGmY2Pk-3rnpWaj4rMk4nJy8bMmZSSlJKLkMnl9PdRbBJs-e8BTwnp3fT3ERsQbPnvAU8J6Q.pFu_BF37I3TcBtp5wLJBWR9v9YCH-2hUmLqxl_mwJdE2nHrQ1plt3LM38gZwwj9zZnAgG2mbMpqEYnMGz2tTCg'
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
