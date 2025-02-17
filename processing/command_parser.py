from VoiceSheets.output.voice_output import VoiceOutput
from VoiceSheets.processing.task_manager import TaskManager

class CommandParser:
    def __init__(self):
        self.voice_output = VoiceOutput()
        self.task_manager = TaskManager()


    def execute_routine(self, command):
        """Executa uma rotina com base no comando de voz."""
        if "abrir navegador" in command:
            self.voice_output.speak("Abrindo o navegador.")
            # Aqui você pode adicionar o código para abrir o navegador
            print("Navegador aberto.")
        elif "contar" in command:
            self.voice_output.speak("contar pastas do windows")
            self.voice_output.speak(self.task_manager.get_folders())
        elif "proprietário" in command:
            self.task_manager.atualizar_proprietario()
        elif "locatário" in command:
            self.task_manager.atualizar_locatario()
        elif "cinza" in command:
            self.voice_output.speak("Pressionando a tecla F3...")
            self.voice_output.speak(self.task_manager.press_f3())
        elif "preto" in command:
            self.voice_output.speak("Pressionando a tecla F1...")
            self.voice_output.speak(self.task_manager.press_f1())
        elif "hora" in command:
            self.voice_output.speak(self.task_manager.get_hour())
        elif "sair" in command:
            self.voice_output.speak("Saindo do programa.")
            exit()
        else:
            self.voice_output.speak("Comando não reconhecido.")

