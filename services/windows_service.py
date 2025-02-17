from datetime import datetime
import os



class WindowsService:
    def __init__(self):
        pass

    def get_current_time(self):
        now = datetime.now()
        return now

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

    def create_folder(self, path, name):
        """
                Cria uma pasta no caminho especificado.

                :param caminho: Caminho completo da pasta a ser criada.
                :return: True se a pasta foi criada com sucesso, False caso contrário.
                """
        try:
            folder_path = os.path.join(path, name)
            if not os.path.exists(folder_path):
                os.makedirs(os.path.join(folder_path))
                return f"A pasta '{name}' foi criada no caminho indicado."
            return f"A pasta '{name}' já existe no caminho indicado."

        except OSError:
            print(f"Erro ao criar a pasta '{name}' no caminho '{path}'.")
            return False


