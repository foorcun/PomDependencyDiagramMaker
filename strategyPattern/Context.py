class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self,pomContent, parent):
        return self.strategy.doOperation(pomContent, parent)