class TestHello():
    def __init__(self,config,options) -> None:
        self.config = config
        self.options = options
        
    def test_hello(self):
        print('hello!')