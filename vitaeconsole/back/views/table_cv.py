# import sys
# sys.path.append("")


from __future__ import annotations

import csv
import io
from itertools import cycle


from math import sin

from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import Traceback

from textual import containers, events, lazy, on
from textual.app import ComposeResult
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

)
from cvs.read_cv import read_db
WIDGETS_MD = """\
# Widgets

The Textual library includes a large number of builtin widgets.

The following list is *not* exhaustive…
 
"""

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
        width: 100;        
        height: 16 !important;            
        &.-maximized {
            height: auto !important;
        }
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
    
    """
    
    datasd = {}
     
    def sanitize_data_db():
        data = read_db()
        group_columns = list(data[0].keys())
        columns = list(data[0]["personal_data"].keys())
        # columns = [colum for groupcolumn in data[0].values() for colum in groupcolumn]
        values = []
        values.append(list(data[0]["personal_data"].values()))
        # values = [valor for diccionario in data for valor in diccionario.values()]
        # values = [valor for valor in data[0]["personal_data"].values() ]
        # group_columns.append(data[0])
        for cv in data:
            
            print("hola")
            # for group_columns, columns in cv.items():
            #     group_columns.append(group_columns[0])
            #     columns.append(columns)

        return group_columns,columns,values

    group_columns, columns, values = sanitize_data_db()
    
    cursors = cycle(["column", "row", "cell", "none"])

    def compose(self) -> ComposeResult:
        
        yield Markdown(self.DATATABLES_MD)
        with containers.VerticalGroup():
            yield Markdown("groupcolumns: " + str(self.group_columns))
            yield Markdown("columns: " + str(self.columns))
            yield Markdown("values: " + str(self.values))
            with containers.ItemGrid(min_column_width=20):
                for i in self.group_columns:
                    yield Label(str(i.replace("_", " ")), id = i )
               
            yield DataTable(fixed_columns=1)
   
        
    def on_mount(self) -> None:
        
        table = self.query_one(DataTable)
        table.add_columns(*self.columns)
        table.add_rows(self.values)
        # table.add_columns(*self.TITLES[0])
        # table.add_columns(*self.TITLES[0])
        
        # table.add_rows(ROWS[1:])
    def key_c(self):
        table = self.query_one(DataTable)
        table.cursor_type = next(self.cursors)
        


class TableScreen(PageScreen):
    """The Widgets screen"""

    CSS = """
    WidgetsScreen { 
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
