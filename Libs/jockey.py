"""
    Jockey class.
        - age (int): age
        - sexe (int): 0 --> male, 1 --> female
        - last results (int[]): array of last positions
        - id (int): unique id
        - from_id(id (int)): returns a Jockey instance filled with data corresponding to given id
"""

class Jockey:

    def __init__(self, age, sexe, last_results, id):
        self.age = age
        self.sexe = sexe
        self.last_results = last_results
        self.id = id

    @staticmethod
    def from_id(id):
        return Jockey(0, 0, [], id)
