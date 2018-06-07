# Translator
Translates word content between languages

#### Import

```Python3
import goslate
```

#### Class

```Python3
class Translation():
```

#### Translating Files

```Python3
  def raw_input_file(self):
        fileName = input("Enter File Path")
        with open(fileName) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return content
```
#### Translating Input
```Python3
def raw_input_user(self):
        userText = input()
        return userText
```        
#### Translator

```Python3
    def translator(self, goslate, text, language):
        translatedText = goslate.translate(text, language)
        print(translatedText)
        return translatedText
```      
        
#### Run It

```Python3
if __name__ = "__main__":
    
    goslate = goslate.Goslate()
    sentence = "Hello, World! How are you feeling today?"
    language = 'fr'
    a.translator(goslate, sentence, language)
```
