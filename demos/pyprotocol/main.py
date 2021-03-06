from objp.util import pyref

class MyProtocol:
    def getAnswer_(self, arg: int) -> str: pass

class PyMain:
    def __init__(self, callback: pyref):
        self.callback = callback
    
    def execute(self):
        print("Hello from Python. Let's do a callback on our class conforming to our protocol.")
        print(self.callback.getAnswer_(42))
