# Information-Theory

### Purpose 

**InformationTheory.py** implements the following functions useful for information theory calculations for discrete random variables:
- Shannon entropy
- Maximum Shannon entropy (i.e. the entropy of a discrete random variable assuming a uniform distribution)
- KL Divergence or relative entropy: a psuedo-distance measure between two distributions. Often used to find a "good enough" distribution when the true distribution is intractable.
- Size of typical set of random variable sequences according to the Asymptotic Equipartition Property (AEP)
- Permutation counter
- Combination counter (i.e. n choose k)

The **HarmonicSeries** class instantiates a numpy array with the first k numbers of the harmonic series. This is useful for finding the entropy of an alphabet under Zipf's law, a probability distribution over the letters of an alphabet. 

**Simulations.py** applies information theory concepts to specific situations. The **BinaryBayes** class takes a discrete marginal probability distribution and likelihood function over a binary variable and outputs the posterior distribution given an observation. This can be seen as a reduction of entropy in the system, given an observation. 
