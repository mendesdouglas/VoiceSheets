import os
from logging import exception

from VoiceSheets.services.windows_service import WindowsService
from VoiceSheets.services.google_sheets import GoogleSheetsService
from VoiceSheets.services.autogui_utils import AutoguiService
from VoiceSheets.core.config import Config
from VoiceSheets.services.pdf_utils import PDFUtils



class TaskManager:
    def __init__(self):
        self.windows_service = WindowsService()
        self.autogui_service = AutoguiService()
        self.google_sheets_service = GoogleSheetsService(Config.GOOGLE_CREDENTIALS_FILE)
        self.pdf_utils = PDFUtils()

    def get_folders(self):
        path = Config.PROJECT_PATH
        quantidade_de_pastas = self.windows_service.count_folders(path)
        return f"a quantidade de pastas é {quantidade_de_pastas}"

    def get_proprietario(self):
        nome_aba = Config.SHEET_NAME
        planilha = self.google_sheets_service.connect_google_sheet(Config.GOOGLE_CREDENTIALS_FILE, Config.GOOGLE_SHEET_ID)
        proprietario = self.google_sheets_service.obter_ultimo_locatario_ou_proprietario_linha(planilha, nome_aba, flag_proprietario=True)
        print(proprietario.nome)
        return proprietario

    def contar_pagina_locatario(self):
        locatario = self.get_locatario()
        nome_pdf = locatario.nome_arquivo+".pdf"
        nome_pasta = locatario.nome_pasta
        try:
            if nome_pdf:
                caminho_pdf = os.path.join(Config.PROJECT_PATH, nome_pasta, nome_pdf)
                if os.path.exists(caminho_pdf):
                    print("pdf encontrado")
                    num_paginas = self.pdf_utils.contar_paginas_pdf(caminho_pdf)
                    return num_paginas
                else:
                    print("pdf não encontrado")
                    return False
        except Exception as e:
            print(f"Erro ao acessar a planilha: {e}")
            return None

    def atualizar_locatario(self):
        nome_aba = Config.SHEET_NAME
        planilha = self.google_sheets_service.connect_google_sheet(Config.GOOGLE_CREDENTIALS_FILE, Config.GOOGLE_SHEET_ID)
        locatario = self.get_locatario()
        atualiza_quantidade_locatario = self.google_sheets_service.inserir_valor_na_linha(planilha, nome_aba, locatario.index, 9, self.contar_pagina_locatario())

    def atualizar_proprietario(self):
        nome_aba = Config.SHEET_NAME
        planilha = self.google_sheets_service.connect_google_sheet(Config.GOOGLE_CREDENTIALS_FILE, Config.GOOGLE_SHEET_ID)
        locatario = self.get_locatario()
        atualiza_quantidade_proprietario = self.google_sheets_service.inserir_valor_na_linha(planilha, nome_aba, locatario.index, 9, self.contar_pagina_proprietario())


    def contar_pagina_proprietario(self):
        proprietario = self.get_proprietario()
        nome_pdf = proprietario.nome_arquivo+".pdf"
        nome_pasta = proprietario.nome_pasta
        try:
            if nome_pdf:
                caminho_pdf = os.path.join(Config.PROJECT_PATH, nome_pasta, nome_pdf)
                print(caminho_pdf)
                if os.path.exists(caminho_pdf):
                    print("pdf encontrado")
                    num_paginas = self.pdf_utils.contar_paginas_pdf(caminho_pdf)
                    return num_paginas
                else:
                   return False
            return "O campo na planilha nome_pdf está vazio"
        except Exception as e:
            print(f"Erro ao acessar a planilha: {e}")
        return None

    def get_locatario(self):
        nome_aba = Config.SHEET_NAME
        planilha = self.google_sheets_service.connect_google_sheet(Config.GOOGLE_CREDENTIALS_FILE, Config.GOOGLE_SHEET_ID)
        locatario = self.google_sheets_service.obter_ultimo_locatario_ou_proprietario_linha(planilha, nome_aba, flag_proprietario=False)
        return locatario

    def create_new_folder(self):
        path = Config.PROJECT_PATH
        locatario = self.get_locatario()
        nome_nova_pasta = self.windows_service.create_folder(path, locatario.nome_pasta)
        quantidade = locatario.quantidade
        print(quantidade)
        return nome_nova_pasta

    def press_f3(self):
        self.autogui_service.press_key('F3')
        return f"foi pressionado o botão F3"

    def press_f1(self):
        self.autogui_service.press_key('F1')
        return f"foi pressionado o botão F1"

    def get_hour(self):
        time = self.windows_service.get_current_time()
        return f"A hora atual é {time.hour} horas e {time.minute} minutos."