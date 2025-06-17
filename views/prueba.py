# from textual.app import App, ComposeResult
# from textual.widgets import Static


# class GridLayoutExample(App):
#     CSS_PATH = "grid_layout_auto.tcss"

#     def compose(self) -> ComposeResult:
#         yield Static("First column", classes="box")
#         yield Static("Two", classes="box")
#         yield Static("Three", classes="box")
#         yield Static("Four", classes="box")
#         yield Static("Five", classes="box")
#         yield Static("Six", classes="box")


# if __name__ == "__main__":
#     app = GridLayoutExample()
#     app.run()
from rich.text import Text
from textual.app import App, ComposeResult ,RenderResult
from textual.color import Color
from textual.message import Message
from textual.widgets import Static


class ColorButton(Static):
    """A color button."""

    class Selected(Message):
        """Color selected message."""

        def __init__(self, color: Color) -> None:
            self.color = color
            super().__init__()

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def on_mount(self) -> None:
        self.styles.margin = (1, 2)
        self.styles.content_align = ("center", "middle")
        self.styles.background = Color.parse("#ffffff33")
        self.styles.border = ("tall", self.color)

    def on_click(self) -> None:
        # The post_message method sends an event to be handled in the DOM
        self.post_message(self.Selected(self.color))

    def render(self) -> str:
        return str(self.color)


class ColorApp(App):
    def compose(self) -> ComposeResult:
        yield ColorButton(Color.parse("#008080"))
        yield ColorButton(Color.parse("#808000"))
        yield ColorButton(Color.parse("#E9967A"))
        yield ColorButton(Color.parse("#121212"))

    def on_color_button_selected(self, message: ColorButton.Selected) -> None:
        self.screen.styles.animate("background", "#808000", duration=0.5)
        def render() -> RenderResult:
            return Text(str(message.color))
        render()



if __name__ == "__main__":
    app = ColorApp()
    app.run()