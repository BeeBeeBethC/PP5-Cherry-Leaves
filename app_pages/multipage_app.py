import streamlit as st


class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

    def app_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
