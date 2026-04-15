from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def handle(self, context):
        pass


class Water:

    def __init__(self):
        self.state = LiquidState()

    def change_state(self):
        self.state.handle(self)


class SolidState(State):

    def handle(self, context: Water):
        print("Вода в твердом состоянии (лед)")
        print("Можно менять на жидкость")
        context.state = LiquidState()


class LiquidState(State):

    def handle(self, context: Water):
        print("Вода в жидком состоянии")
        print("Можно менять на газ")
        context.state = GasState()


class GasState(State):

    def handle(self, context: Water):
        print("Вода в газообразном состоянии (пар)")
        print("Можно менять на твердое")
        context.state = SolidState()


if __name__ == "__main__":
    water = Water()

    water.change_state()
    water.change_state()
    water.change_state()
