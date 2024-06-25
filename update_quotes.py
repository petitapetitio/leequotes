from pathlib import Path

import requests


def download_google_sheet_to(spreadsheet_id: str, filepath: Path):
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=tsv'
    print(f"Downloading https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print('File saved to: {}'.format(filepath))


if __name__ == '__main__':
    download_google_sheet_to('1PbIU9R8N4NF8xAjC81YHqXPQumMo0bNEnzSHMo7K3v4', Path("leequotes/data/quotes.tsv"))
