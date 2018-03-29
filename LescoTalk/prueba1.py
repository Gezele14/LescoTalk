import pyttsx3
import win32com


def prueba(texto):
    if isinstance(texto,str):
        eng = pyttsx3.init()
        eng.setProperty("rate",130)
        eng.setProperty("volumen",400)
        eng.say("La seña interpretada es")
        eng.say(texto)
        eng.runAndWait()
    else:
        eng.setProperty("rate",130)
        eng.setProperty("volumen",400)
        eng.say("No se reconoce la seña")
        eng.runAndWait()
