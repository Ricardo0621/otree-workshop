from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consentimiento(Page):
    form_model = 'player'
    form_fields = ['numero_identificacion', 'nombre_completo', 'acepta_terminos', 'institucion_educativa']
    
    def is_displayed(self):
        return self.round_number == 1

class Instrucciones(Page):
    form_model = 'player'
    form_fields = ['pregunta_1', 'pregunta_2']

    def is_displayed(self):
        return self.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['traiciona']    

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        jugador_1, jugador_2 = self.group.get_players()
        if jugador_1.traiciona: #Jugador 1 traiciona
            if jugador_2.traiciona: #Jugador 2 también traiciona
                jugador_1.payoff = Constants.pago_ambos_traicionan #Ambos traicionan
                jugador_2.payoff = Constants.pago_ambos_traicionan #Ambos traicionan
            else: #Jugador 2 coopera
                jugador_1.payoff  = Constants.pago_diferente_traiciona #Sale libre
                jugador_2.payoff  = Constants.pago_diferente_coopera #Paga la máxima pena
        else: #Jugador 1 coopera
            if jugador_2.traiciona:
                jugador_1.payoff = Constants.pago_diferente_coopera #Paga la máxima pena
                jugador_2.payoff = Constants.pago_diferente_traiciona #Sale libre
            else:
                jugador_1.payoff = Constants.pago_ambos_cooperan #Pagan 1 año
                jugador_2.payoff = Constants.pago_ambos_cooperan #Pagan 1 año

class Results(Page):
    pass

class ResultadosCombinados(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        todos_los_jugadores = self.player.in_all_rounds()
        pago_combinado = 0
        for player in todos_los_jugadores:
            pago_combinado += player.payoff
        return {
            'pago_combinado': pago_combinado
        }    

page_sequence = [Consentimiento, Instrucciones, Decision, ResultsWaitPage, Results, ResultadosCombinados]
# page_sequence = [Decision, ResultsWaitPage, Results]
