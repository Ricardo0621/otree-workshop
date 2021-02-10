from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mi_dilema_del_prisionero_re'
    players_per_group = 2
    num_rounds = 2
    pago_ambos_cooperan = -1
    pago_ambos_traicionan = -2
    pago_diferente_traiciona = 0
    pago_diferente_coopera = -3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    traiciona = models.BooleanField(
        label="Por favor, escoja la opción",
        choices = [[True, "Traiciona"],
                [False, "Coopera"]]
        )
    acepta_terminos = models.BooleanField(
        label="Por favor, indique si acepta los términos de esta actividad",
        choices=[[True, "Sí"],
                [False, "No"],
                ],
        default = True        
        ) 
    numero_identificacion = models.IntegerField(label="Por favor, ingrese su número de identificación")
    nombre_completo = models.StringField(label="Por favor, escriba su nombre completo")
    institucion_educativa = models.StringField(
        label="Indique la institución a la que pertenece",
        choices = [
            ["Universidad del Valle", "Universidad del Valle"],
            ["Universidad del Rosario", "Universidad del Rosario"],
            ["Uniminuto", "Uniminuto"],
            ["Otro", "Otro"],
            ],
        widget = widgets.RadioSelect,    
        )
    pregunta_1 = models.IntegerField(
        label = "¿Qué sucede si ambos cooperan?",
        choices = [
            [1, "Ambos somos condenados" ],
            [2, "Soy condenado a 3 años"],
            [3, "Salgo libre"],
            [4, "Ambos sirven un año"]
            ],
        widget = widgets.RadioSelect,       
        )
    pregunta_2 = models.IntegerField(
        label = "¿Qué sucede si ambos traicionan?",
        choices = [
            [1, "El otro sale libre" ],
            [2, "Ambos sirven dos años"],
            [3, "Salgo libre"],
            [4, "Ambos son condenados a 3 años"]
            ],
        widget = widgets.RadioSelect,       
        )    
    def pregunta_1_error_message(self, value):
        if value != 4:
            return "Respuesta incorrecta. Por favor, lea de nuevo las instrucciones"
    def pregunta_2_error_message(self, value):
        if value != 2:
            return "Respuesta incorrecta. Por favor, lea de nuevo"        
