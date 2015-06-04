class game:

    def __init__(self):
        self.totalScore = 0
        self.strikeScore = 0
        self.score = 0
        self.round = 1
        self.frame = 1


    def gameInfo(self):
        return (self.totalScore, self.strikeScore, self.score, self.frame, self.round)

    def roll(self, pins):
        if self.frame < 10:
            if self.round < 3:
                if pins is 10:
                    self.strikeScore = 10
                    self.round = 3
                else:
                    self.score += pins
                    self.round += 1
            else:
                if self.strikeScore is 10:
                    self.totalScore = self.totalScore + self.strikeScore
                    self.strikeScore = 0
                else:
                    self.totalScore += self.score
                self.score = 0
                self.score += pins
                self.round = 2
                self.frame += 1

        elif self.frame is 10:
            pass
            #Hier komt de tiende frame
        else:
            pass
            #This will trigger the end of the game function