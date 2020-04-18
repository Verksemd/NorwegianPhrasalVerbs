
# лучше чтобы файл со словами был отдельно csv
# !/usr/bin/env python
import wx

slovar = {"se an": "være nøye med noe", "se bort fra": "ikke regne med noe", "se etter": ["passe på", "lete etter", "undersøke"],
"se fram til": "glede seg til noe", "se gjennom": "ta et øverblikk over", "se gjennom fingrene": "overse", "se med på": "forakte",
"se opp fra": "være forsiktig", "se opp til": "beundre", "se over": ["lese gjennom", "kontrollere"], "se på": ["tenke på", "vurdere"],
"se til": ["passe på", "besøke"], "se til at": "sørge for at", "se ut til": "virke som", "se ut som": "ligne"


          }

# Open new window with:
app = wx.App()
window = wx.Frame(None, title="Phrasal verbs dictionary", size=(300, 200))
panel = wx.Panel(window)
window.Show()
# text "This is a dictionary"
label = wx.StaticText(panel, label="Enter the word", pos=(100, 50))
# input "search word definition"
word_input = wx.TextCtrl(panel, pos=(20, 70))
# search result text with "empty text" so it is not visible
search_result = wx.StaticText(panel, pos=(80, 100))
# button "Search"
search_button = wx.Button(panel, label="Search", pos=(150, 70))
#pushing "enter" triggers find_definition()

def word_input_handler(event):
    #if enter is pressed
    if event.GetKeyCode() == 13:
        search_result.SetLabel(find_definition(event.EventObject.Value))


word_input.Bind(wx.EVT_KEY_UP, word_input_handler, word_input)

# On button click get text from input and try to find it in dictionary
panel.Bind(wx.EVT_BUTTON, lambda data: search_result.SetLabel(find_definition(word_input.Value)), search_button)

def find_definition(searching_word):
    searching_word = searching_word.lower()
    for word, meaning in slovar.items():
        # if match exists show definition from dictionary
        if searching_word == word:
            if type(meaning) == list:
                meaning = ", ".join(meaning)
            return meaning

    # if no matches show "No result for WORD"
    return "No definition found"

app.MainLoop()

'''class Clothes():
    def __init__(self, name, size, color):
        self.size = size
        self.color = color
        self.name = name

    def __print(self, text):
        print('dick za vorotnik ' + text)

    def show_description(self):
        self.__print("название:" + self.name + " размер: " + self.size + "цвет: " + self.color)


new_item = Clothes('pajamas', '42', 'black')
new_item_2 = Clothes('dress', '48', 'yellow')


new_item_2.__print('boop')
new_item_2.show_description()'''
