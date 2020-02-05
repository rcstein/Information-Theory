"""Classes and functions for Information Theory concepts

Classes:

HarmonicSeries for calculation of alphabet entropy under Zepf's law
    
BinaryBayes for modeling binary-input, binary-output channel with Bayes theorem and entropy functions

MiscFuncs contains functions for calculating entropy, kl divergence, typical set, number of permutations, etc.
    
author: Rebecca Stein

"""

import numpy as np
from math import factorial
import networkx as nx
import matplotlib.pyplot as plt

class HarmonicSeries():
    """First n numbers in harmonic series"""

    def __init__(self, n):

        temp = np.arange(1,n+1)
        f = lambda x: 1. / x
        vf = np.vectorize(f)
        self.series = vf(temp)

    def add(self):
        """Return sum of first n numbers in harmonic series"""

        return np.sum(self.series)

class MiscFuncs():

    def __init__(self):
        pass

    def entropy(self,X):
        """Return entropy of probability vector X"""
    
        f = lambda x: x * np.log2(x)
        vf = np.vectorize(f)
        return -1 * np.sum(vf(X))

    def max_entropy(self,N):
        """Return entropy of event with N outcomes assuming uniform distribution"""
    
        return np.log2(N)

    def kl_divergence(self,px,qx):
        """Return KL divergence between p(x) and q(x)"""

        f = lambda p,q: p * np.log2(p.q)
        vf = np.vectorize(f)
        return np.sum(vf(px,qx))

    def zipf(self,k):
        """Return entropy of alphabet with k symbols following Zipf's law

        Zipf's law: if k letters are ordered according to frequency, the probability of
        each letter equals c / k, where k is the letter's place in the order and c is a
        normalizing constant.
        """
        
        series = HarmonicSeries(k)
        c = 1 / series.add()
        probs = c * series.series
        return self.entropy(probs) 
     
    def typical_set(self,n,H):
        """Return size of typical set given length n and entropy H. Uses AEP (Asymptotic Equapartition Property): |A_e^n| -> 2^nH as n -> infinity.
            A_e^n is set of typical sequences of length n with limit in probability -> 1 - e
        """

        return 2**(n*H)

    def count_perms(self,n,k, with_replace = True):
        """Return number of possible permutations of k elements from set size n."""

        if with_replace:
            return n ** k
        else:
            return (factorial(n) / factorial(n-k))

    def n_choose_k(self,n,k):
        """Return number of combinations of k elements from set size n."""

        return self.count_perms(n,k,with_replace = False) / factorial(k)

Funcs = MiscFuncs()

if __name__ == "main":
    Funcs = MiscFuncs()
