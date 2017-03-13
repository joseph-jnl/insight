import random

class MarkovNode(object):
    '''
    Markov state with link and probability to other states
    '''

    def __init__(self, val):
        self.val = val
        self.probs = {}

    def change_state(self):
        '''
        Return state given dictionary of transition probabilities
        '''
        x = random.random()
        cumulative_probability = 0.0
        for node, prob in self.probs.items():
            cumulative_probability += prob
            if x < prob:
                break
        return node


p = [('a', 'a', 0.3),
     ('a', 'b', 0.6),
     ('a', 'c', 0.1),
     ('b', 'a', 0.2),
     ('b', 'b', 0.2),
     ('b', 'c', 0.6),
     ('c', 'a', 0.3),
     ('c', 'b', 0.3),
     ('c', 'c', 0.2),
     ('c', 'd', 0.2),
     ('d', 'a', 0.1),
     ('d', 'b', 0.3),
     ('d', 'c', 0.2),
     ('d', 'd', 0.4),
     ]

# Get unique node vals
vals = set([i[0] for i in p])

# Create markov nodes
nodes = {}

for val in vals:
    nodes[val] = MarkovNode(val)

# Set nodes transition probabilities
for node in nodes:
    nodes[node].probs = dict([i[1:] for i in p if i[0]==node])


def simulationMK(k, nodes):
    '''
    Simulate k simulations of Markov chain given in nodes and return 
    the number of times each state occured
    '''
    outcomes = {}
    current = nodes[p[0][0]]

    for sim in range(k):
        current = nodes[current.change_state()]
        if current.val in outcomes.keys():
            outcomes[current.val] += 1
        else:
            outcomes[current.val] = 1

    return outcomes

print(simulationMK(100, nodes))