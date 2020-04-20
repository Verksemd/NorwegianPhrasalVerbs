
# лучше чтобы файл со словами был отдельно csv
#сделать две кнопки с лэйблом "Выберите язык перевода": русский, норвежский
# !/usr/bin/env python
if __name__ == "__main__":
    import wx
    import csv

    def get_dictionary(language):
        if language == "norsk":
            file_name = "norsk_slovar.csv"
        elif language == "russian":
            file_name = "russian_slovar.csv"
        else:
            raise Exception("Неизвестный язык словаря")

        with open(file_name, mode='r', encoding="utf-8") as dict_file:
            reader = csv.reader(dict_file)
            return {rows[0]: rows[1] for rows in reader}


    norsk_slovar = get_dictionary("norsk")
    russian_slovar = get_dictionary("russian")

    # Open new window with:
    app = wx.App()
    window = wx.Frame(None, title="Phrasal verbs dictionary", size=(300, 300))
    panel = wx.Panel(window)
    window.Show()
    #choose language
    russian_button = wx.RadioButton(panel, label="Русский", pos=(20, 20))
    norwegian_button = wx.RadioButton(panel, label="Norsk", pos=(150, 20))

    # text "Enter the word"
    label = wx.StaticText(panel, label="Введите слово", pos=(100, 70))
    # input "search word definition"
    word_input = wx.TextCtrl(panel, pos=(20, 100))
    # search result text with "empty text" so it is not visible
    search_result = wx.StaticText(panel, pos=(80, 200))
    # button "Search"
    search_button = wx.Button(panel, label="Search", pos=(150, 100))



    #execute search if enter is pressed
    def word_input_handler(event):
        #if enter is pressed
        if event.GetKeyCode() == 13:
            search_result.SetLabel(find_definition(event.EventObject.Value))

    #displays result
    word_input.Bind(wx.EVT_KEY_UP, word_input_handler, word_input)

    # On "Search" button click get text from input and try to find it in dictionary
    panel.Bind(wx.EVT_BUTTON, lambda data: search_result.SetLabel(find_definition(word_input.Value)), search_button)

    def find_definition(searching_word):
        searching_word = searching_word.lower()

        dictionary = russian_slovar
        if norwegian_button.GetValue():
            dictionary = norsk_slovar

        for word, meaning in dictionary.items():
            # if match exists show definition from dictionary
            if searching_word == word:
                return meaning

        # if no matches show "No result for WORD"
        return "No definition found"

    app.MainLoop()
