from clashroyalebuildabot import Cards
from clashroyalebuildabot.actions.generic.def_bridge_action import DefBridgeAction
from clashroyalebuildabot.actions.generic.defense_action import DefenseAction

class CannonAction(DefBridgeAction, DefenseAction):
    CARD = Cards.CANNON
