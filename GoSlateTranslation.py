import goslate

class Translation():

    def raw_input_file(self):
        fileName = input("Enter File Path")
        with open(fileName) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return content

    def raw_input_user(self):
        userText = input()
        return userText

    def translator(self, goslate, text, language):
        translatedText = goslate.translate(text, language)
        print(translatedText)
        return translatedText

if __name__ = "__main__":
    
    goslate = goslate.Goslate()
    sentence = "Hello, World! How are you feeling today?"
    language = 'fr'
    a.translator(goslate, sentence, language)
