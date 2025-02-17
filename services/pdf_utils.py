from PyPDF2 import PdfReader
import os


class PDFUtils:
    def contar_paginas_pdf(self, caminho_pdf):
        """
        Conta o número de páginas de um arquivo PDF.

        :param caminho_pdf: Caminho completo do arquivo PDF.
        :return: Número de páginas do PDF ou -1 em caso de erro.
        """
        try:
            reader = PdfReader(caminho_pdf)
            num_paginas = len(reader.pages)
            print(f"O PDF '{caminho_pdf}' tem {num_paginas} páginas.")
            return num_paginas
        except Exception as e:
            print(f"Erro ao contar as páginas do PDF: {e}")
            return -1

    def exists_file(self, caminho_pdf):
        try:
            if not os.path.exists(caminho_pdf):
                return False
            return True
        except Exception as e:
            print(f"Erro ao verificar se o arquivo existe: {e}")
