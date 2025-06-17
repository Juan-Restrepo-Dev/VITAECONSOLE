"""
An implementation of the "Sliding Tile" puzzle.

Textual isn't a game engine exactly, but it wasn't hard to build this.

"""

from dataclasses import dataclass


from .widgets.inputs import Inputs


from textual import containers, events, on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.demo.page import PageScreen
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Footer, Markdown, Select,  Input, Label

DATA_CV = {}
@dataclass
class NewCV:
    """A dataclass to report the desired game type."""
    # cv:dict
    # personal_data:dict
    # {
    #      "personal_data":{
    #         "name":"Jane Doe",
    #         "id":"1556161166",
    #         "tel":"+57455455454",
    #         "address":" 65wwqeqw",
    #         "email":"janedoe@email.com",
    #         "date_birth":"20/05/1990"
    #      },
    #      "academic_training":[
    #         {
    #            "institute":"ferrini",
    #            "title":"bachiller",
    #            "duration":"5/20/2000 to 15/56/2005"
    #         },
    #         {
    #            "institute":"itm",
    #            "title":"medico general",
    #            "duration":"5/20/2006 to 15/56/2010"
    #         }
    #      ],
    #      "professional_experience":[
    #         {
    #            "company":"sura",
    #            "post":"medico urgencias",
    #            "function_performed":"atendender sala de urgencias",
    #            "duration":"5/20/2000 to 15/56/2005"
    #         },
    #         {
    #            "company":"saviasalud",
    #            "post":"medico urgencias",
    #            "function_performed":"atendender sala de urgencias",
    #            "duration":"5/20/2000 to 15/56/2005"
    #         }
    #      ],
    #      "personal_references":[
    #         {
    #            "name":"Foo Jones",
    #            "relation":"papa",
    #            "tel":"556-342-452"
    #         },
    #         {
    #            "name":"jane Jones",
    #            "relation":"mama",
    #            "tel":"556-342-452"
    #         }
    #      ],
    #      "skills_or_certificates":[
    #         {
    #            "certificate":"Foo Jones",
    #            "date":"12/45/15"
    #         },
    #         ""
    #      ]
    #   }
    

class PersonalData(containers.VerticalGroup, can_focus=True):
    """A dialog to ask the user for the initial cv personal data parameters."""
    ALLOW_MAXIMIZE = True
    DEFAULT_CSS = """
        PersonalData {
            border: thick $primary-muted;
            padding: 0 2;
            width: 150;
            #values {
                width: 1fr;
                Select { margin: 1 0;}
            }
            Button {
                margin: 0 1 1 1;
                width: 1fr;
            }
        }        
    """
    BINDINGS = [
        ("escape", "dismiss"),
        Binding("up", "move('up')", "up", priority=True),
        Binding("down", "move('down')", "down", priority=True),
        Binding("left", "move('left')", "left", priority=True),
        Binding("right", "move('right')", "right", priority=True),
    ]
    INPUT_LABELS = ["name","id","email","tel","dir"]
    PERSONAL_DATA = {}
    def compose(self) -> ComposeResult:
        with containers.VerticalGroup(id="values"):
           
            yield Inputs(self.INPUT_LABELS,"**DATOS PERSONALES**")

        yield Button("Siguiente", variant="primary", id="next")

    # def action_save_and_continue(self) -> None:
    #     self.app.push_screen(CvDialogScreen(AcademicTraining(self.PERSONAL_DATA)))
        

    @on(Button.Pressed,"#next")
    def save_and_continue(self) -> None:

        for i in self.INPUT_LABELS:
            self.PERSONAL_DATA[i] = self.query_one(f"#{i}",Input).value
        DATA_CV["personal_data"] = self.PERSONAL_DATA
        self.app.push_screen(CvDialogScreen(AcademicTraining))    
  
class AcademicTraining(containers.VerticalGroup, can_focus=True):
    """A dialog to ask the user for create new Academic training."""
    # def __init__(self, prueba):
    #     super().__init__()
    #     self.prueba = prueba
    ALLOW_MAXIMIZE = True
    DEFAULT_CSS = """
       AcademicTraining {
            background: $boost;
            border: thick $primary-muted;
            padding: 0 2;
            width: 150;
            #values {
                width: 1fr;
                Select { margin: 1 0;}
            }
            Button {
                margin: 0 1 1 1;
                width: 1fr;
            }
        }        
    """
    BINDINGS = [
        ("escape", "dismiss"),
        Binding("up", "move('up')", "up", priority=True),
        Binding("down", "move('down')", "down", priority=True),
        Binding("left", "move('left')", "left", priority=True),
        Binding("right", "move('right')", "right", priority=True),
    ]
    INPUT_LABELS = ["institute","title","duration"]
    ACADEMIC_TRAINING = []
    def compose(self) -> ComposeResult:
        with containers.VerticalGroup(id="values"):
           
            yield Inputs(self.INPUT_LABELS,"**FORMACION ACADEMICA**")
            yield Button("Añadir otra formacion academica", variant="success", id="add_new_academic_training")
            yield Button("Siguiente", variant="primary", id="next")


    @on(Button.Pressed,"#next")
    def save_and_continue(self) -> None:
        academic_training = {}
        for i in self.INPUT_LABELS:
            academic_training[i] = self.query_one(f"#{i}",Input).value
        self.ACADEMIC_TRAINING.append(academic_training)
        DATA_CV["academic_training"] = self.ACADEMIC_TRAINING
        self.app.push_screen(CvDialogScreen(ProfessionalExperience))    

    @on(Button.Pressed,"#add_new_academic_training")
    def save_and_repeat(self) -> None:
        academic_training = {}
        for i in self.INPUT_LABELS:
            academic_training[i] = self.query_one(f"#{i}",Input).value
        self.ACADEMIC_TRAINING.append(academic_training)
        self.app.push_screen(CvDialogScreen(AcademicTraining))        
  
class ProfessionalExperience(containers.VerticalGroup, can_focus=True):
    """A dialog to ask the user for create new professional experience."""
    # def __init__(self, prueba):
    #     super().__init__()
    #     self.prueba = prueba
    ALLOW_MAXIMIZE = True
    DEFAULT_CSS = """
      ProfessionalExperience {
            background: $boost;
            border: thick $primary-muted;
            padding: 0 2;
            width: 150;
            #values {
                width: 1fr;
                Select { margin: 1 0;}
            }
            Button {
                margin: 0 1 1 1;
                width: 1fr;
            }
        }        
    """
    BINDINGS = [
        ("escape", "dismiss"),
        Binding("up", "move('up')", "up", priority=True),
        Binding("down", "move('down')", "down", priority=True),
        Binding("left", "move('left')", "left", priority=True),
        Binding("right", "move('right')", "right", priority=True),
    ]
    INPUT_LABELS = ["company","post","function_performed","duration"]
    PROFESSIONAL_EXPERIENCE = []
    def compose(self) -> ComposeResult:
        with containers.VerticalGroup(id="values"):
           
            yield Inputs(self.INPUT_LABELS,"**EXPERIENCIA LABORAL**")
            yield Button("Añadir otra Experiencia laboral", variant="success", id="add_new_professional_experience")
            yield Button("Siguiente", variant="primary", id="next")


    @on(Button.Pressed,"#next")
    def save_and_continue(self) -> None:
        professional_experience = {}
        for i in self.INPUT_LABELS:
            professional_experience[i] = self.query_one(f"#{i}",Input).value
        self.PROFESSIONAL_EXPERIENCE.append(professional_experience)
        DATA_CV["professional_experience"] = self.PROFESSIONAL_EXPERIENCE
        self.app.push_screen(CvDialogScreen(PersonalReferences))    

    @on(Button.Pressed,"#add_new_professional_experience")
    def save_and_repeat(self) -> None:
        professional_experience = {}
        for i in self.INPUT_LABELS:
            professional_experience[i] = self.query_one(f"#{i}",Input).value
        self.PROFESSIONAL_EXPERIENCE.append(professional_experience)
        self.app.push_screen(CvDialogScreen(ProfessionalExperience))        

class PersonalReferences(containers.VerticalGroup, can_focus=True):
    """A dialog to ask the user for the new personal references."""

    ALLOW_MAXIMIZE = True
    DEFAULT_CSS = """
       PersonalReferences {
            background: $boost;
            border: thick $primary-muted;
            padding: 0 2;
            width: 150;
            #values {
                width: 1fr;
                Select { margin: 1 0;}
            }
            Button {
                margin: 0 1 1 1;
                width: 1fr;
            }
        }        
    """
    BINDINGS = [
        ("escape", "dismiss"),
        Binding("up", "move('up')", "up", priority=True),
        Binding("down", "move('down')", "down", priority=True),
        Binding("left", "move('left')", "left", priority=True),
        Binding("right", "move('right')", "right", priority=True),
    ]
    INPUT_LABELS = ["name","relation","tel"]
    PERSONAL_REFERENCES = []
    def compose(self) -> ComposeResult:
        with containers.VerticalGroup(id="values"):
           
            yield Inputs(self.INPUT_LABELS,"**PERSONAL REFERENCES**")
            yield Button("Añadir otra Referencia personal", variant="success", id="add_new_personal_references")
            yield Button("Siguiente", variant="primary", id="next")


    @on(Button.Pressed,"#next")
    def save_and_continue(self) -> None:
        personal_references = {}
        for i in self.INPUT_LABELS:
            personal_references[i] = self.query_one(f"#{i}",Input).value
        self.PERSONAL_REFERENCES.append(personal_references)
        DATA_CV["personal_references"] = self.PERSONAL_REFERENCES
        self.app.push_screen(CvDialogScreen(SkilsOrCertificates))    

    @on(Button.Pressed,"#add_new_personal_references")
    def save_and_repeat(self) -> None:
        personal_references = {}
        for i in self.INPUT_LABELS:
            personal_references[i] = self.query_one(f"#{i}",Input).value
        self.PERSONAL_REFERENCES.append(personal_references)
        self.app.push_screen(CvDialogScreen(PersonalReferences))        

class SkilsOrCertificates(containers.VerticalGroup, can_focus=True):
    """A dialog to ask the user for the new skill or certificate parameters."""
    def __init__(self, *args):
        super().__init__()
        if args:
            self.args = args[0][0]
        else:
            self.args = ("Default")     

    ALLOW_MAXIMIZE = True
    DEFAULT_CSS = """
       SkilsOrCertificates {
            background: $boost;
            border: thick $primary-muted;
            padding: 0 2;
            width: 150;
            #values {
                width: 1fr;
                Select { margin: 1 0;}
            }
            Button {
                margin: 0 1 1 1;
                width: 1fr;
            }
        }        
    """
    BINDINGS = [
        ("escape", "dismiss"),
        Binding("up", "move('up')", "up", priority=True),
        Binding("down", "move('down')", "down", priority=True),
        Binding("left", "move('left')", "left", priority=True),
        Binding("right", "move('right')", "right", priority=True),
    ]
    # SKILL_OR_CERTIFICATE = self.args[0]
    OPTIONS = ["Skill","Certificate"]
    SKILL_LABELS = ["name","skill"]
    CERTIFICATE_LABELS = ["name","link","date"]
    def compose(self) -> ComposeResult:
        with containers.VerticalGroup(id="values"):
            if self.args == "Skill":
                yield Inputs(self.SKILL_LABELS,"**SKILLS**")
                yield Button("Volver a elegir", variant="warning", id="backtoselect")
                yield Button("Añadir otra Referencia personal", variant="success", id="add_new_personal_references")
                yield Button("Siguiente", variant="primary", id="next")
            elif self.args == "Certificate":
                yield Inputs(self.CERTIFICATE_LABELS,"**CERTIFICATES**")
                yield Button("Volver a elegir", variant="warning", id="backtoselect")
                yield Button("Añadir otra Referencia personal", variant="success", id="add_new_personal_references")
                yield Button("Siguiente", variant="primary", id="next")
            else:
                yield Markdown("# SKILLS OR CERTIFICATES")
                yield Label("**Seleciona que quieres anadir una skill o un certificado**")
                yield Label("Seleciona skill o un certificado")
                yield Select.from_values(
                    self.OPTIONS,
                    # value="Skill",
                    prompt="Skill or certificate",
                    id="skill_or_certificate",
                    allow_blank=True,
                )
                yield Button("Volver", variant="warning", id="back")

            



    @on(Select.Changed,"#skill_or_certificate")
    def change_inputs(self, event: Select.Changed) -> None:
        a = str(event.value)
        self.change(a)
        # self.query_one("#skill_or_certificate", Select).value = event.value
            # self.app.push_screen(CvDialogScreen(SkilsOrCertificates))


    @on(Button.Pressed,"#next")
    def save_and_continue(self) -> None:
        personal_references = {}
        # for i in self.INPUT_LABELS:
        #     personal_references[i] = self.query_one(f"#{i}",Input).value
        # self.PERSONAL_REFERENCES.append(personal_references)
        # DATA_CV["personal_references"] = self.PERSONAL_REFERENCES
        # self.app.push_screen(CvDialogScreen(AcademicTraining))    

    @on(Button.Pressed,"#add_new_personal_references")
    def save_and_repeat(self) -> None:
        personal_references = {}
        # for i in self.INPUT_LABELS:
        #     personal_references[i] = self.query_one(f"#{i}",Input).value
        # self.PERSONAL_REFERENCES.append(personal_references)
        # self.app.push_screen(CvDialogScreen(PersonalReferences))        
    # @on(Button.Pressed,"#change")

    @on(Button.Pressed,"#backtoselect")
    def back_to_select(self) -> None:
        self.app.push_screen(CvDialogScreen(SkilsOrCertificates,"default"))



    def change(self,skill_or_certificate) -> None:
        self.app.push_screen(CvDialogScreen(SkilsOrCertificates,skill_or_certificate))
        # else:
        #     yield Markdown(f"args no existe {self.args}")    
       
           
            # for i in self.INPUT_LABELS:
            #     personal_references[i] = self.query_one(f"#{i}",Input).value
            # self.PERSONAL_REFERENCES.append(personal_references)
            # DATA_CV["personal_references"] = self.PERSONAL_REFERENCES
            # self.app.push_screen(CvDialogScreen(AcademicTraining)) 
    def on_refresh_select(self) -> None:
         self.app.push_screen(CvDialogScreen(SkilsOrCertificates))


class CvDialogScreen(PageScreen):
    def __init__(self, stage, *args):
        super().__init__()
        self.stage = stage
        self.args = args
    DEFAULT_CSS = """
    CvDialogScreen {
        align: center middle;
        hatch: right $panel;
        layer: CvDialogScreen;
        width: 100;
        background: $panel;
        border: thick $primary-darken-2; 
        &:focus {
            border: heavy $success;
        }
    }
    """

    
    def compose(self) -> ComposeResult:
        if self.args :
            yield self.stage(self.args)
            self.stage.focus(self)
            

        else:
            yield self.stage()
            self.stage.focus(self)
            
        yield Footer()
  



class CreateCvInstructions(containers.VerticalGroup):
    DEFAULT_CSS = """\
    CreateCvInstructions {        
        layer: instructions;
        width: 100;
        background: $panel;
        border: thick $primary-darken-2; 
        Markdown {
            background: $panel;
        }
        
    }

"""
    INSTRUCTIONS = """\
# Instrucciones

Aqui prodras crear una nueva CV.

Para hacerlo llena todos los inputs solicitados recuarda no dejar ninguno vacio o no podras avanzar. <br>  


Cada que guardes podras ver la nueva CV en en listado de CV. <br>  

**Importante!**. Despues de añadir una *formacion academica* una *experiencia laboral*, una *referencia persona* o  
una *skill o certificado* no podras modificarlo al devolverte solo podras anadir un valor nuevo para modificarlo  
deberas hacerlo desde la tabla de CV. <br>  

    """

    def compose(self) -> ComposeResult:
        yield Markdown(self.INSTRUCTIONS)
        with containers.Center():
            yield Button("Crear Nueva CV", action="screen.new_cv", variant="success")



class CreateCvScreen(PageScreen):
    """The screen containing the game."""

    DEFAULT_CSS = """
    CreateCvScreen{       
        align: center middle;
        layers: CreateCvInstructions CvDialogScreen;     
    }
    """

    # BINDINGS = [("n", "new_game", "New Game")]

    def compose(self) -> ComposeResult:
        yield CreateCvInstructions()
        yield Footer()



    def action_new_cv(self) -> None:
        self.app.push_screen(CvDialogScreen(PersonalData))




if __name__ == "__main__":
    from textual.app import App

    class CreateCvApp(App):
        def get_default_screen(self) -> Screen:
            return CreateCvScreen()

    app = CreateCvApp()
    app.run()
