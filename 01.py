from abc import ABC, abstractmethod
import json
import os.path
import pickle


class SerializationInterface(ABC):
    """
    Abstract class for serialisation
    """
    @abstractmethod
    def serialize(self, file: str):
        pass

    @abstractmethod
    def deserialize(self, file: str):
        pass


class SerializationJSON(SerializationInterface):
    """
    Class for serialization to json format
    """
    def __init__(self, data=None):
        self.data = data

    def serialize(self, file: str):
        with open(file, 'w', encoding='UTF-8') as f:
            json.dump(self.data, f)

    def deserialize(self, file: str):
        if not os.path.exists(file):
            return None
        with open(file, 'r', encoding='UTF-8') as f:
            dump = json.load(f)
        return dump

    def __str__(self):
        return str(self.data)


class SerializationBIN(SerializationInterface):
    """
    Class for serialization to bin format
    """
    def __init__(self, data=None):
        self.data = data

    def serialize(self, file: str):
        with open(file, 'wb') as f:
            pickle.dump(self.data, f)

    def deserialize(self, file: str):
        if not os.path.exists(file):
            return None
        with open(file, 'rb') as f:
            dump = pickle.load(f)
        return dump

    def __str__(self):
        return str(self.data)


d = SerializationJSON(data={"Empno": 101, "Name": "Ramesh", "Salary": 17000})
print(d)

d.serialize('smth.json')
a = d.deserialize('smth.json')
print(a)

d.serialize('smth.bin')
a = d.deserialize('smth.bin')
print(a)
