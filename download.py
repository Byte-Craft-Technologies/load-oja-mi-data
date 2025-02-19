import io
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def download_excel():
    SERVICE_ACCOUNT_FILE = os.environ["SERVICE_ACCOUNT_FILE"]

    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    drive_service = build('drive', 'v3', credentials=creds)

    FILE_ID = '1rv-xu_lc7DqE4fzpygTWSz2zGfu7E0JIv-siaRFxdew'

    request = drive_service.files().export_media(
        fileId=FILE_ID,
        mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    
    if os.path.exists('output_with_images.xlsx'):
        os.remove('output_with_images.xlsx')

    fh = io.FileIO('output_with_images.xlsx', 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False

    while not done:
        status, done = downloader.next_chunk()
        print("Téléchargement à {}%.".format(int(status.progress() * 100)))
