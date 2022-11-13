class DescriptorRoad:

    def __init__(self, minusValue):
        self._minusValue = minusValue

    def __get__ (self, instance, owner_class):
        return instance.__dict__[self._minusValue]

    def __set__(self, instance, value):

        if value < 0:
            raise ValueError("значение не может быть отрицательным")
        instance.__dict__[self._minusValue] = value


class Road:

    length = DescriptorRoad("length")
    width = DescriptorRoad("width")

    def __init__(self, length, width,  massa = 12, thickness = 0.7):
        self.length = length
        self.width = width
        self.massa = massa
        self.thickness = thickness
        
    def massa_asphalt (self):
        massa_asphalt_tonne = self.length*self.width*self.massa*self.thickness
        return print(f"{massa_asphalt_tonne/1000} тонн асфальта необходимого для покрытия")


obj = Road(12,1000)
obj.massa_asphalt()

obj = Road(-10,14)
obj.massa_asphalt()