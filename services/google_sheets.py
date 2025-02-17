import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsService:
    def __init__(self, credenciais_path):
        self.credenciais_path = credenciais_path

    def connect_google_sheet(caminho_arquivo_credenciais, id_planilha):
        """Conecta ao Google Sheets."""

        try:
            escopo = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            credenciais = ServiceAccountCredentials.from_json_keyfile_name(caminho_arquivo_credenciais, escopo)
            client = gspread.authorize(credenciais)
            planilha = client.open_by_key(id_planilha)
            return planilha
        except Exception as e:
            print(f"Erro ao conectar ao Google Sheets: {e}")
            return None

    def get_column(self, sheet, nome_aba, coluna):
        aba = sheet.worksheet(nome_aba)
        return aba.col_values(coluna)