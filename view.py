import flet as ft


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        # Row 1

        self._confermaRow1 = ft.Text(value='you MUST select a language')
        self._selzionaLingua = ft.Dropdown(label='Scelect Language',
                                           options=[ft.dropdown.Option('None'), ft.dropdown.Option('italian'),
                                                    ft.dropdown.Option('english'),
                                                    ft.dropdown.Option('spanish')], width=750,
                                           on_change=self.confermaSelezione1
                                           )
        row1 = ft.Row([self._selzionaLingua, self._confermaRow1])

        # Row 2
        self._confermaRow2 = ft.Text(value='you MUST select a type')
        self._tipoRicerca = ft.Dropdown(label='Select search type',
                                        options=[ft.dropdown.Option('None'), ft.dropdown.Option('Default'),
                                                 ft.dropdown.Option('Linear'),
                                                 ft.dropdown.Option('Dichotomic')],
                                        on_change=self.confermaSelezione2
                                        )
        self._txtInput = ft.TextField(label='Insert your text')
        self._searchButton = ft.ElevatedButton(text='Spell Check', on_click=self.handleSpellCheck)
        row2 = ft.Row([self._tipoRicerca, self._txtInput, self._searchButton, self._confermaRow2])

        # Row 3
        self._txtOutput = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        row3 = ft.Row([])

        self.page.add(row1, row2, self._txtOutput)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def confermaSelezione1(self, e):
        if self._selzionaLingua.value == 'None':
            self._confermaRow1.value = 'you MUST select a language'
        else:
            self._confermaRow1.value = 'selected language'
        self.page.update()

    def confermaSelezione2(self, e):
        if self._tipoRicerca.value == 'None':
            self._confermaRow2.value = 'you MUST select a type'
        else:
            self._confermaRow2.value = 'selected type'
        self.page.update()

    def handleSpellCheck(self, e):
        if self._selzionaLingua.value != 'None' and self._tipoRicerca.value != 'None' and self._txtInput.value != '':
            risultato = self.__controller.handleSentence(self._txtInput.value, self._selzionaLingua.value,
                                             self._tipoRicerca.value)
            self._txtOutput.controls.append(ft.Text(f'Frase inserita: {self._txtInput.value}\n'
                                                    f'Parole errate: {risultato[0]}\n'
                                                    f'Tempo richiesto dalla ricerca: {risultato[1]}\n'))
            self.page.update()
        else:
            pass