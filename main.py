import flet as ft

import controller as c
import model as m
import view as v


def main(page: ft.Page):
    # Setup model, view, control according to MVC pattern
    model = m.MultiDictionary()
    controller = c.SpellChecker()
    view = v.Interface(page, controller)

ft.app(target=main)