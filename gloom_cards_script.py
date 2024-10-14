import translation
import win32com.client
import os

psApp = win32com.client.Dispatch("Photoshop.Application")
doc = psApp.Application.ActiveDocument



#main text
translated_text = translation.city_cards_front[1]["main"]
main_text_layer = doc.ArtLayers["main"]
main_text = main_text_layer.TextItem
translated_text = translated_text.replace("\n", "\r")
main_text.contents = translated_text

#options
options = translation.city_cards_front[1]["options"]
translated_text = "Opção A: " + options[1] + "\r" + "Opção B: " + options[1]
options_text_layer = doc.ArtLayers["options"]
options_text = options_text_layer.TextItem
options_text.contents = translated_text

#id
id_text_layer = doc.ArtLayers["id"]
id_text = id_text_layer.TextItem
id_text.contents = str(translation.city_cards_front[0]["id"])


#export file
# for text in text_samples:
#     text_layer.contents = text
#     options = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
#     options.format = 13
#     options.quality = 100
#     index = text_samples.index(text)
#     png = f"C:\\Users\\anton\\Desktop\\{index}.jpg"
#     doc.Export(ExportIn=png, ExportAs=2, Options=options)
