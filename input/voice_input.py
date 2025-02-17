import speech_recognition as sr

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_commands(self):
        with sr.Microphone() as source:
            print("Ouvindo...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio, language="pt-BR")
                return command.lower()
            except sr.UnknownValueError:
                return None
            except sr.RequestError as e:
                print(f"Erro no serviço de reconhecimento de voz: {e}")
                return None