import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    self.args = args
    self.contents = []

    for key,value in self.args.items():
      for i in range(value):
        self.contents.append(key)
    self.contents1 = copy.deepcopy(self.contents)

  def draw(self, drawNum):
    self.contents = self.contents1[:]
    choices = []
    for i in range(drawNum):
      if self.contents == []:
        return choices
      random.seed()
      randChoice = random.choice(self.contents)
      self.contents.remove(randChoice)
      choices.append(randChoice)

    return choices
      
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected = []
  m = 0
  n = num_experiments
  
  for key, value in expected_balls.items():
    for i in range(value):
      expected.append(key)
  
  newExpected = copy.deepcopy(expected)
  
  for i in range(n):
    newDraw = hat.draw(num_balls_drawn)
    newExpected = expected[:]
    for j in range(len(newDraw)):
      for k in range(len(newExpected)):
        if newDraw[j] == newExpected[k]:
          newExpected.remove(newExpected[k])
          break
    if len(newExpected) == 0:
      m += 1
  
  return m/n