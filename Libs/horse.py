"""
    Horse class.
        - age (int): age of the horse
        - sexe (int): 0 --> male, 1 --> female
        - musique (int[]): last positions
        - id (int): unique id
        - from_id(id (int)): returns a Horse instance filled with data corresponding to given id
"""

class Horse:

    def __init__(self, age, sexe, musique, id):
        self.age = age
        self.sexe = sexe
        self.musique = musique
        self.id = id

    @staticmethod
    def from_id(id):
        return Horse(0, 0, [], id)
