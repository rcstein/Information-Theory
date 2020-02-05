from InformationTheory import *

class Simulations():
""" Collection of specific examples applying information theory concepts"""
	
    def __init__(self):
        pass
        
	def sum_two_dice(self):
        """Return pdf of Z where Z = X + Y and X,Y are outcomes of rolling two fair six-sided dice

            Returns a dictionary where keys are z and values are p(z)
            """
        pz = {}
        for z in range(2,13):
            pz[z] = 0
            x = 1
            while x < 7:
                y = z - x
                if 0 < y < 7:
                    pz[z] += (1./6 * 1./6)
                x += 1
        return pz
                         
class BinaryBayes(Simulation):
"""Posterior of binary event given marginal probabilities and likelihoods"""

def __init__(self, events, indicators, likelihood):
    """events - dictionary with events as keys and marginal probabilities as values
        indicators - 1x2 array of possible observations
        likelihood - 2x2 matrix of likelihoods, where upper left entry is a true positive and lower right entry is a true negative"""

    self.events = np.fromiter(events.keys(), dtype = 'U25')
    self.marginals = np.fromiter(events.values(),dtype = float)
    self.indicators = indicators
    self.likelihood = likelihood

def posterior(self,observation):
    """Return posterior of success given evidence"""
    
    y = self.indicators.index(observation)
    C = self.evidence(observation)
    return self.likelihood[0,y] * self.marginals[0] / C

def evidence(self, observation):
    """Return marginal probability of an observation"""

    y = self.indicators.index(observation)
    return np.dot(self.likelihood[:,y],self.marginals)

def entropy(self, conditional = False):
    """Return entropy of event space prior to observation if conditional is False, entropy conditional on observation otherwise."""

    if not conditional:
        return Funcs.entropy(self.marginals)
    else:
        # need to figure out simpler way to do this without loops / with kl divergence function
        H = 0
        for x in [0,1]:
            for y in [0,1]:
                joint = self.marginals[x] * self.likelihood[x,y]
                H += joint * np.log2(joint/self.evidence(self.indicators[y]))
        return -H

def mi(self):
    """Return mutual information between events and observations using equation I(X;Y) = H(X) - H(X|Y)"""

    return self.entropy() - self.entropy(conditional = True)
