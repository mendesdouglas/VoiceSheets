from VoiceSheets.output.voice_output import VoiceOutput
from VoiceSheets.input.voice_input import VoiceInput
from VoiceSheets.processing.command_parser import CommandParser

class App:
    def __init__(self):
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput()
        self.command_parser = CommandParser()

    def run(self):
        self.voice_output.speak("Olá, como posso ajudar?")
        while True:
            command = self.voice_input.listen_commands()
            if command:
                self.command_parser.execute_routine(command)



if __name__ == "__main__":
    app = App()
    app.run()
