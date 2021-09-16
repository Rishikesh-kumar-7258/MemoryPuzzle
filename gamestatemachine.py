class GameStateMachine:

    def __init__(self, states={}):

        self.current = {}
        self.states = states

    def change(self, state, params={}):

        assert state in self.states

        self.current.leave()
        self.current = self.states[state]
        self.current.enter(params)

    def update(self, params=None):

        self.current.update(params)