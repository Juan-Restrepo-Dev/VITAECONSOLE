# import sys
# sys.path.append("")


from __future__ import annotations

import csv
import io
from itertools import cycle


from math import sin
from typing import TypeVar

from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import Traceback
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.style import Style


from textual import containers, events, lazy, on
from textual.app import (ComposeResult ,RenderResult)
from textual.binding import Binding
from textual.demo.page import PageScreen
from textual.reactive import reactive, var
from textual.screen import Screen
from textual.suggester import SuggestFromList
from textual.theme import BUILTIN_THEMES
from textual.widgets import (
    DataTable,
    Footer,
    Label,
    Markdown,
    Button,
    Input
)
from cvs.read_cv import read_db
from views.export_cv import ExportScreen
WIDGETS_MD = """\
# Data table CV
 
"""
# grid-columns: 96 19 25 21 24 36;
class Datatables(containers.VerticalGroup):
    """Demonstrates DataTables."""

    DEFAULT_CLASSES = "column"
    DATATABLES_MD = """\
## Datatables

A fully-featured DataTable, with cell, row, and columns cursors.
Cells may be individually styled, and may include Rich renderables.

**Tip:** Focus the table and press `ctrl+a`

"""
    DEFAULT_CSS = """    
    DataTable {
        width: 250 !important;        
        height: 16 !important;            
        &.-maximized {
            height: auto !important;
        }
    }
    #group_columns_table{
            grid-size: 6;
            grid-columns: 44% 8.5% 11.5% 9.5% 11% 15.5%;
            grid-rows: 3;
        }
    #personal_data {
            background: gray 80%;
            width: 100%;
        }
    #academic_training {
            background: #EA7E00;
            width: 100%;
        }
    #professional_experience{
            background: #EA30E4;
            width: 100%;
        }
    #personal_references {
            background: rgb(3,81,234) ;
            width: 100%;
        }
    #skills_or_certificates {
            background: #EBD017;
            width: 100%;
        }
    #actions {
            background: #30EA43;
            width: 100%;
        }                  
    
    """
    
    datasd = ""

    def sanitize_data_db():
        data = read_db()
        group_columns = list(data[0].keys())
        columns = list(data[0]["personal_data"].keys())
        values = [list(groupcolumn["personal_data"].values()) for groupcolumn in data  ]
        return group_columns,columns,values

    group_columns, columns, values = sanitize_data_db()
    
    cursors = cycle(["column", "row", "cell", "none"])

    def compose(self) -> ComposeResult:
        
        yield Markdown(self.DATATABLES_MD)
        with containers.Container(id="container-datatable"):
            yield Label("column")
            yield Input("",id="column-cordenates")
            yield Input("",id="row-cordenates")
            yield Input("",id="hover-cordenates")
            yield Input("",id="cell-selected")
            with containers.ItemGrid(id="group_columns_table"):
                for i in self.group_columns:
                    yield Button(str(i.replace("_", " ")), id = i )
                yield Button("actions", id="actions") 
               
            yield DataTable(fixed_columns=1)
   
        
    def on_mount(self) -> None:
       
        personal_data_style = (Style(color = "#EA7E00") , Style(bgcolor = "#EA7E00", color="#FFFFFF",bold=True) )
        academic_training_style =  (Style(color = "#EA7E00") , Style(bgcolor = "#EA7E00", color="#FFFFFF",bold=True) )
        professional_experience_style =  (Style(color = "#EA30E4") , Style(bgcolor = "#EA30E4", color="#FFFFFF",bold=True) )
        personal_references_style =  (Style(color = "rgb(3,81,234)") , Style(bgcolor = "rgb(3,81,234)", color="#FFFFFF",bold=True) )
        skills_style =  (Style(color = "#EBD017") , Style(bgcolor = "#EBD017", color="#FFFFFF",bold=True) )
        table_style =[personal_data_style,academic_training_style,professional_experience_style,personal_references_style,skills_style] 
        actions_butons=[("\u270F","Editar"),("\U0001F5D1","Eliminar"),("\U0001F4E4","Exportar")]      
   
        def button_render(self,label = "", button_style=Style(),label_style = Style(), justify="") -> RenderResult:
            panel = Panel(Text(label,style=label_style, justify="center",overflow="ellipsis"),border_style=button_style)
            
            return panel
        
        table = self.query_one(DataTable)
        table.add_columns(*self.columns)
        for row in self.values:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [
                Text(f"\n{cell}", style = Style(), justify="center") for cell in row
            ]
            table.add_row(*styled_row,height=3)
        # table.add_rows(self.values)
        for column, style in zip(self.group_columns[1:],table_style[1:]):
            table.add_column(column.replace("_", " "),default= button_render(self, label=f"Ver datos",button_style=style[0],label_style=style[1]))

        for action in actions_butons:
            table.add_column(f"{action[1]} {action[0]}",default=Text(f"\n{action[0]}",justify="center"))

        # table.add_columns(*self.TITLES[0])
        # table.add_columns(*self.TITLES[0])
        
        # table.add_rows(ROWS[1:])
    def key_s(self):
        table = self.query_one(DataTable)
        table.cursor_type = next(self.cursors)

    def on_mouse_move(self) -> None:
        table = self.query_one(DataTable)
        self.query_one("#column-cordenates",Input).value = str(table.hover_column)
        self.query_one("#row-cordenates",Input).value = str(table.hover_row)
        if table.hover_column == 0:
            self.screen.styles.animate("background", "#808080", duration=0.5)
        if table.hover_column == 1:
            self.screen.styles.animate("background", "#D01D1D", duration=0.5)
            # self.query_one("#hover-cordenates",Input).value = str(table.hover_coordinate)
    # def on_click(self) -> None:
        # table = self.query_one(DataTable)
        # self.query_one("#hover-cordenates",Input).value = str(table.hover_coordinate)
        # self.query_one("#cell-selected",Input).value = str(table.CellSelected())
    def on_data_table_cell_selected(self) -> None:
        table = self.query_one(DataTable)
        self.query_one("#hover-cordenates",Input).value = str(table.hover_coordinate)
        column = int(table.hover_coordinate.column)
        row = int(table.hover_coordinate.row)
        # actions

        #export
        if column == 12:
            self.app.push_screen(ExportScreen())
            # export_cv(index=row)
        #delete
        #edit

        #expanded data

        
       




    def render(self):
        self.query_one("#column-cordenates",Input).value = str(self.datasd)
        r = self.query_one("#column-cordenates",Input).value
        return Text(str(r))

        


class TableScreen(PageScreen):
    """The Widgets screen"""
    
    CSS = """
    TableScreen { 
        align-horizontal: center;
        Markdown { background: transparent; }
        & > VerticalScroll {
            scrollbar-gutter: stable;
            & > * {                          
                &:even { background: $boost; }
                padding-bottom: 1;
            }
        }
    }
    .column {          
        align: center top;
        &>*{ max-width: 220 !important; }        
    }
    #container-datatable{
        max-width: 220;
    }
    """

    BINDINGS = [Binding("escape", "blur", "Unfocus any focused widget", show=False)]

    def compose(self) -> ComposeResult:
        with lazy.Reveal(containers.VerticalScroll(can_focus=True)):
            yield Markdown(WIDGETS_MD, classes="column")
            yield Datatables()

        yield Footer()


# if __name__ == "__main__":
#     from textual.app import App

#     class GameApp(App):
#         def get_default_screen(self) -> Screen:
#             return TableScreen()

#     app = GameApp()
#     app.run()
