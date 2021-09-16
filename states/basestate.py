class Base:

    def __init__(self) : pass

    def enter(self, **params) :
        self.render()

    def leave(self) : pass

    def render(self) : pass

    def update(self, params) : pass