class Person():
    def __init__(self, tellsTheTruth):
        self.am = int(tellsTheTruth)
    
    def said(self, condition):
        return condition if self.am else not condition

    def isLiar(self):
        return not self.am

    def isTruthTeller(self):
        return self.am

def list_all_solutions(num, keys):
    solutions = []
    for i in map(lambda x: (num + 2 - len(bin(x))) * "0" + bin(x)[2:], range(2**num)):
        all_conditions_satisfied_thus_far = True
        for j in keys:
            if not j(map(Person, i)):
               all_conditions_satisfied_thus_far = False
               break
        if all_conditions_satisfied_thus_far: solutions.append(i)
    return solutions
    
# Your code below! You should describe the problem and it will (hopefully) solve it

print 'test case: ten liars and truth tellers sit around a circular table. Two of them state "both my neighbors are liars." The other eight people state: "Both my neighbors are truth tellers." How many truth tellers could possibly be in this group?'

print 'First, suppose the two who said "both my neighbors are liars" are sitting next to one another:'

print(list_all_solutions(10,
     [
         lambda people:
         people[0].said(
             people[9].isLiar() and people[1].isLiar()
         ),
         lambda people:
         people[1].said(
             people[0].isLiar() and people[2].isLiar()
         ),
         lambda people:
         people[2].said(
             people[1].isTruthTeller() and people[3].isTruthTeller()
         ),
         lambda people:
         people[3].said(
             people[2].isTruthTeller() and people[4].isTruthTeller()
         ),
         lambda people:
         people[4].said(
             people[3].isTruthTeller() and people[5].isTruthTeller()
         ),
         lambda people:
         people[5].said(
             people[4].isTruthTeller() and people[6].isTruthTeller()
         ),
         lambda people:
         people[6].said(
             people[5].isTruthTeller() and people[7].isTruthTeller()
         ),
         lambda people:
         people[7].said(
             people[6].isTruthTeller() and people[8].isTruthTeller()
         ),
         lambda people:
         people[8].said(
             people[7].isTruthTeller() and people[9].isTruthTeller()
         ),
         lambda people:
         people[9].said(
             people[8].isTruthTeller() and people[0].isTruthTeller()
         )
     ]
))

print "Next, suppose they are sitting with one person between them:"

print(list_all_solutions(10,
     [
         lambda people:
         people[0].said(
             people[9].isLiar() and people[1].isLiar()
         ),
         lambda people:
         people[1].said(
             people[0].isTruthTeller() and people[2].isTruthTeller()
         ),
         lambda people:
         people[2].said(
             people[1].isLiar() and people[3].isLiar()
         ),
         lambda people:
         people[3].said(
             people[2].isTruthTeller() and people[4].isTruthTeller()
         ),
         lambda people:
         people[4].said(
             people[3].isTruthTeller() and people[5].isTruthTeller()
         ),
         lambda people:
         people[5].said(
             people[4].isTruthTeller() and people[6].isTruthTeller()
         ),
         lambda people:
         people[6].said(
             people[5].isTruthTeller() and people[7].isTruthTeller()
         ),
         lambda people:
         people[7].said(
             people[6].isTruthTeller() and people[8].isTruthTeller()
         ),
         lambda people:
         people[8].said(
             people[7].isTruthTeller() and people[9].isTruthTeller()
         ),
         lambda people:
         people[9].said(
             people[8].isTruthTeller() and people[0].isTruthTeller()
         )
     ]
))

print "next, suppose there are two people sitting between them"

print(list_all_solutions(10,
     [
         lambda people:
         people[0].said(
             people[9].isLiar() and people[1].isLiar()
         ),
         lambda people:
         people[1].said(
             people[0].isTruthTeller() and people[2].isTruthTeller()
         ),
         lambda people:
         people[2].said(
             people[1].isTruthTeller() and people[3].isTruthTeller()
         ),
         lambda people:
         people[3].said(
             people[2].isLiar() and people[4].isLiar()
         ),
         lambda people:
         people[4].said(
             people[3].isTruthTeller() and people[5].isTruthTeller()
         ),
         lambda people:
         people[5].said(
             people[4].isTruthTeller() and people[6].isTruthTeller()
         ),
         lambda people:
         people[6].said(
             people[5].isTruthTeller() and people[7].isTruthTeller()
         ),
         lambda people:
         people[7].said(
             people[6].isTruthTeller() and people[8].isTruthTeller()
         ),
         lambda people:
         people[8].said(
             people[7].isTruthTeller() and people[9].isTruthTeller()
         ),
         lambda people:
         people[9].said(
             people[8].isTruthTeller() and people[0].isTruthTeller()
         )
     ]
))

print "next, suppose there are three people sitting between them"

print(list_all_solutions(10,
     [
         lambda people:
         people[0].said(
             people[9].isLiar() and people[1].isLiar()
         ),
         lambda people:
         people[1].said(
             people[0].isTruthTeller() and people[2].isTruthTeller()
         ),
         lambda people:
         people[2].said(
             people[1].isTruthTeller() and people[3].isTruthTeller()
         ),
         lambda people:
         people[3].said(
             people[2].isTruthTeller() and people[4].isTruthTeller()
         ),
         lambda people:
         people[4].said(
             people[3].isLiar() and people[5].isLiar()
         ),
         lambda people:
         people[5].said(
             people[4].isTruthTeller() and people[6].isTruthTeller()
         ),
         lambda people:
         people[6].said(
             people[5].isTruthTeller() and people[7].isTruthTeller()
         ),
         lambda people:
         people[7].said(
             people[6].isTruthTeller() and people[8].isTruthTeller()
         ),
         lambda people:
         people[8].said(
             people[7].isTruthTeller() and people[9].isTruthTeller()
         ),
         lambda people:
         people[9].said(
             people[8].isTruthTeller() and people[0].isTruthTeller()
         )
     ]
))

print "next, suppose there are four people sitting between them"

print(list_all_solutions(10,
     [
         lambda people:
         people[0].said(
             people[9].isLiar() and people[1].isLiar()
         ),
         lambda people:
         people[1].said(
             people[0].isTruthTeller() and people[2].isTruthTeller()
         ),
         lambda people:
         people[2].said(
             people[1].isTruthTeller() and people[3].isTruthTeller()
         ),
         lambda people:
         people[3].said(
             people[2].isTruthTeller() and people[4].isTruthTeller()
         ),
         lambda people:
         people[4].said(
             people[3].isTruthTeller() and people[5].isTruthTeller()
         ),
         lambda people:
         people[5].said(
             people[4].isLiar() and people[6].isLiar()
         ),
         lambda people:
         people[6].said(
             people[5].isTruthTeller() and people[7].isTruthTeller()
         ),
         lambda people:
         people[7].said(
             people[6].isTruthTeller() and people[8].isTruthTeller()
         ),
         lambda people:
         people[8].said(
             people[7].isTruthTeller() and people[9].isTruthTeller()
         ),
         lambda people:
         people[9].said(
             people[8].isTruthTeller() and people[0].isTruthTeller()
         )
     ]
))
