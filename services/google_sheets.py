import gspread
from oauth2client.service_account import ServiceAccountCredentials
from VoiceSheets.core.config import Config
from VoiceSheets.entity.Locatario import LocatarioEntity
from VoiceSheets.entity.Proprietario import ProprietarioEntity


class GoogleSheetsService:
    def __init__(self, credenciais_path):
        self.credenciais_path = credenciais_path

    def connect_google_sheet(self, caminho_arquivo_credenciais, id_planilha):
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

    def obter_ultimo_locatario_ou_proprietario_linha(self, planilha, nome_aba, flag_proprietario=False):
        """Obtem a ultima linha que contém itens em uma aba específica."""
        try:
            aba = planilha.worksheet(nome_aba)

            valores = aba.get_all_values()
            dados = []
            linha_index = len(valores) - 1

            if flag_proprietario:
                if len(valores) > 1:
                    dados = valores[-2] #porque as listas começam do índice 0
            else:
                for i in range(len(valores) - 1, -1, -1):
                    if any(celula.strip() for celula in valores[i]):
                        linha_index = i
                        dados = valores[i]
                        break
            if flag_proprietario:
                proprietario = ProprietarioEntity(
                    index=linha_index,
                    malote=dados[1],
                    digitalizador=dados[2],
                    pasta=dados[3],
                    data_digitalizacao=dados[4],
                    endereco=dados[5],
                    tipo=dados[6],
                    nome=dados[7],
                    quantidade=dados[8],
                    nome_arquivo=dados[10],
                    nome_pasta=dados[11])
                return proprietario
            else:
                locatario = LocatarioEntity(
                    index=linha_index+1,
                    malote=dados[1],
                    digitalizador=dados[2],
                    pasta=dados[3],
                    data_digitalizacao=dados[4],
                    endereco=dados[5],
                    tipo=dados[6],
                    nome=dados[7],
                    quantidade=dados[8],
                    nome_arquivo=dados[10],
                    nome_pasta=dados[11])
                return locatario
        except Exception as e:
            print(f"Erro ao acessar a planilha: {e}")
            return None


    def inserir_valor_na_linha(self, planilha, nome_aba, linha, coluna, valor):
        """
        Insere um valor em uma célula específica da planilha.

        :param nome_aba:
        :param planilha:
        :param linha: Número da linha (índice baseado em 1).
        :param coluna: Número da coluna (índice baseado em 1).
        :param valor: Valor a ser inserido na célula.
        :return: True se o valor foi inserido com sucesso, False caso contrário.
        """
        try:
            aba = planilha.worksheet(nome_aba)
            aba.update_cell(linha, coluna, valor)  # Atualiza a célula
            print(f"Valor '{valor}' inserido na linha {linha}, coluna {coluna}.")
            return True
        except Exception as e:
            print(f"Erro ao inserir valor na planilha: {e}")
            return False