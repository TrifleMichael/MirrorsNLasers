from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def trigger(self, *args, **kwargs):
        pass


class LogicManager:
    def __init__(self):
        self.receivers = {}
        self.emmiters = {}

    def addReciever(self, receiver, id):
        self.receivers[id] = receiver
        if id in self.emmiters:
            self.emmiters[id].receivers.append(receiver)

    def addEmmiter(self, emmiter, id):
        self.emmiters[id] = emmiter
        if id in self.receivers:
            emmiter.receivers.append(self.receivers[id])
