from clashroyalebuildabot import Cards
from clashroyalebuildabot.actions.generic.bridge_action import BridgeAction
from clashroyalebuildabot.actions.generic.defense_action import DefenseAction

class MinipekkaAction(BridgeAction, DefenseAction):
    CARD = Cards.MINIPEKKA
