from modules.commandlinebot import CommandlineBot

x = CommandlineBot("twine-parser/result.json", image_folder="assets/images/")

x.start_conversation()