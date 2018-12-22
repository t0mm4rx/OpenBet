"""
    Race class.
        - runners (Runner[]): list of runners
        - field (int): the id of the field
        - is_passed (bool): is the run has passed or not ? if so, result should not be null
        - result (int[]): list of runners number in the order of the race
"""

class Race:
    
    def __init__(self, field, runners, result = []):
        self.field = field
        self.runners = runners
        if (len(result)) == 0:
            self.is_passed = False
        else:
            self.is_passed = True
        self.result = result
