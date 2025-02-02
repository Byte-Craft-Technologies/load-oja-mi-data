import io
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def download_excel():
    # Chemin vers ton fichier credentials.json
    SERVICE_ACCOUNT_FILE = 'credentials.json'

    # Portée de l'API
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    # Créer les informations d'identification
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Construire le service Drive
    drive_service = build('drive', 'v3', credentials=creds)

    # ID de la feuille Google Sheets (extrait de l'URL)
    FILE_ID = '1rv-xu_lc7DqE4fzpygTWSz2zGfu7E0JIv-siaRFxdew'

    # Exporter le fichier Google Sheet au format Excel
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
