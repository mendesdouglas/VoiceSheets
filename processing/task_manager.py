import os
from VoiceSheets.services.windows_service import WindowsService
import pyautogui


class TaskManager:
    def __init__(self):
        self.windows_service = WindowsService()

    def count_folders(self, path):
        try:
            itens = os.listdir(path)
            folders = [item for item in itens if os.path.isdir(os.path.join(path, item))]
            return len(folders)
        except FileNotFoundError:
            print(f"Permissão negada para acessar o diretorio '{path}'.")
            return 0
        except PermissionError:
            print(f"Permissão negada para acessar o diretorio '{path}'.")
            return 0

    def obter_ultimo_locatario_ou_proprietario_linha(self, planilha, nome_aba, flag_proprietario=False):
        """Obtem a ultima linha que contém itens em uma aba específica."""
        try:
            aba = planilha.worksheet(nome_aba)

            valores = aba.get_all_values()
            if flag_proprietario:
                return valores[-2]

            for linha in reversed(valores):
                if any(celula.strip() for celula in linha):
                    return linha

            return None
        except Exception as e:
            print(f"Erro ao acessar a planilha: {e}")
            return None

    def press_f3(self):
        pyautogui.press('f3')
        return f"foi pressionado o botão F3"

    def press_f1(self):
        pyautogui.press('f1')
        return f"foi pressionado o botão F1"

    def get_hour(self):
        time = self.windows_service.get_current_time()
        return f"A hora atual é {time.hour} horas e {time.minute} minutos."