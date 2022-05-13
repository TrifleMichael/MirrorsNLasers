from src.Collisons.PolygonCollisionModel import PolygonCollisionModel
from src.Sprites.PolygonSprite import PolygonSprite
from src.Structures import Structure


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


class LaserDetector(Structure):
    def __init__(self, pointList):
        self.collisionModel = PolygonCollisionModel(pointList)
        self.sprite = PolygonSprite(pointList)
        self.sprite.color = (0, 0, 255)

        self.receivers = []

    def draw(self):
        self.sprite.draw()

    def reactToCollision(self):
        for receiver in self.receivers:
            receiver.toggle()
        self.sprite.color = (255, 0, 0)
