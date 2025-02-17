class LocatarioEntity:
    def __init__(self, index, malote, digitalizador, pasta, data_digitalizacao, endereco, tipo, nome, quantidade, nome_arquivo, nome_pasta):
        self.index = index
        self.nome = nome
        self.malote = malote
        self.digitalizador = digitalizador
        self.pasta = pasta
        self.data_digitalizacao = data_digitalizacao
        self.endereco = endereco
        self.tipo = tipo
        self.quantidade = quantidade
        self.nome_arquivo = nome_arquivo
        self.nome_pasta = nome_pasta

        # Métodos GET
        def get_index(self):
            return self._index

        def get_nome(self):
            return self._nome

        def get_malote(self):
            return self._malote

        def get_digitalizador(self):
            return self._digitalizador

        def get_pasta(self):
            return self._pasta

        def get_data_digitalizacao(self):
            return self._data_digitalizacao

        def get_endereco(self):
            return self._endereco

        def get_tipo(self):
            return self._tipo

        def get_quantidade(self):
            return self._quantidade

        def get_nome_arquivo(self):
            return self._nome_arquivo

        def get_nome_pasta(self):
            return self._nome_pasta

        # Métodos SET
        def set_index(self, index):
            self._index = index

        def set_nome(self, nome):
            self._nome = nome

        def set_malote(self, malote):
            self._malote = malote

        def set_digitalizador(self, digitalizador):
            self._digitalizador = digitalizador

        def set_pasta(self, pasta):
            self._pasta = pasta

        def set_data_digitalizacao(self, data_digitalizacao):
            self._data_digitalizacao = data_digitalizacao

        def set_endereco(self, endereco):
            self._endereco = endereco

        def set_tipo(self, tipo):
            self._tipo = tipo

        def set_quantidade(self, quantidade):
            self._quantidade = quantidade

        def set_nome_arquivo(self, nome_arquivo):
            self._nome_arquivo = nome_arquivo

        def set_nome_pasta(self, nome_pasta):
            self._nome_pasta = nome_pasta

        def __str__(self):
            return f"ProprietarioEntity({self.index}, {self.nome}, {self.malote}, {self.digitalizador}, {self.pasta})"