from googletrans import Translator

translator = Translator()

matn = "Salom"
tarjima = translator.translate(matn, src='uz', dest='en')

print(tarjima.text)