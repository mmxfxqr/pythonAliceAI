import os
import pyaudio
import json
import pyautogui  # Убедись, что эта строка есть
from vosk import Model, KaldiRecognizer

# Путь к модели Vosk
model_path = "./vosk"
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Настройка PyAudio для захвата голоса
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("Говорите команду:")

while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result_json = json.loads(result)
        text = result_json.get('text', '')
        print(f"Распознанный текст: {text}")
        
        # Пример реакции на команды
        if "выключить компьютер" in text:
            os.system("shutdown /s /t 0")
        elif "перезагрузить компьютер" in text:
            os.system("shutdown /r /t 0")
        elif "запустить документ" in text:
            os.system("start winword")
        elif "закрыть окно" in text:
            pyautogui.hotkey('alt', 'f4')
        elif "открой блокнот" in text:
            os.system("notepad")  # Открыть блокнот
        elif "открой браузер" in text:
            os.system("start chrome")  # Открыть браузер Chrome
        elif "открой проводник" in text:
            os.system("explorer")  # Открыть проводник Windows
        elif "воспроизвести музыку" in text:
            os.system("start wmplayer")  # Открыть Windows Media Player
        elif "открой калькулятор" in text:
            os.system("calc")  # Открыть калькулятор
        # Добавляй свои команды сюда
