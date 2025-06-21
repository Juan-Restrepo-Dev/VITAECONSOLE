from textual.app import App, ComposeResult,RenderResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Header, Label,ListView,ListItem,Digits,MarkdownViewer,Static
from term_image.image import from_file,Size
from rich.console import Console
from rich.text import Text
from rich import  box
from rich.panel import Panel


html = from_file("./download-html-icon.png",width = 30)
pdf = from_file("./download-pdf-icon.png",width = 30)
# image.forced_support    
# image.width = 20
# image.height = 20
def img_render(image)->RenderResult:
        img_ansi = Text.from_ansi(str(image))
        return img_ansi

class ExportScreen(ModalScreen):
    """Screen with a dialog to expor CV."""

    DEFAULT_CLASSES = "export-dialog"
    CSS_PATH = "export.tcss"
  
    def compose(self) -> ComposeResult:
        # yield ListView(
        #       ListItem(Static(img_render())),
        #     )
        yield Static((img_render(html) + img_render(pdf)),id="icons-container")
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            
            ListView(
                ListItem(Label(Button("Export html",variant="html",id="exportHtml"),img_render(html))),
                ListItem(Button("Export PDF",variant="pdf",id="ExportPdf"),img_pdf(pdf)),
                ListItem(),
            ),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()
