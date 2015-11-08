"""
Problem description:
a Thief who goes to Smaug's Lair. He finds M treasures. Each treasure has some Weight and some
Gold value. But Bilbo cannot really take all of that. He could only carry a certain Maximum
Weight. But being a smart hobbit, he wants to Maximize the value of the treasures he takes.
Given the values for weights and value of the treasures and the maximum weight that Bilbo
could carry, could you find a good solution?

So in this problem we have an 1xM array of Weight Values W, Gold Values G and a value for
the maximum weight wMAX that Bilbo can carry. We want to find out an 1xM array X of 1's
and 0's, which holds weather Bilbo Carries a particular treasure or not. This array needs
to follow the constraint WXT<wMAX and we want to maximize GXT for a particular state X.
(Here the T means transpose)

MCMC:

1. Pick a random index from the state and toggle the index value.
2. Check if we satisfy our constraint. If yes this state is the proposal state.
3. Else pick up another random index and repeat.

Define scoring function as
    score(X) = exp(\beta * G*X^T)
The state with higher energy comes with lower probability
p = 1/Z*exp(-energy)
"""

import numpy as np
import random
import math

# weight vector
W = [20,40,60,12,34,45,67,33,23,12,34,56,23,56]
# gold vector
G = [120,420,610,112,341,435,657,363,273,812,534,356,223,516]
# weight constraint
W_max = 150

def score_state_log(X,G,Beta):
    """
    This function takes a state X , The gold vector G and a Beta Value and return the Log of score
    """
    return Beta*np.dot(X,G)

# This function takes as input a state X and the number of treasures M, The weight vector W and the maximum weight W_max
# and returns a proposal state
def create_proposal(X,W,W_max):
    M                      = len(W)
    random_index           = random.randint(0,M-1)
    #print random_index
    proposal               = list(X)
    proposal[random_index] = 1 - proposal[random_index]  #Toggle
    #print proposal
    if np.dot(proposal,W)<=W_max:
        return proposal
    else:
        return create_proposal(X,W,W_max)

# Toss a random coin with robability of head p. If coin comes head return true else false.
def random_coin(p):
    unif = random.uniform(0,1)
    if unif>=p:
        return False
    else:
        return True

def MCMC_Golddigger(n_iter,W,G,W_max, Beta_start = 0.05, Beta_increments=.02):
    """
    Takes as input a text to decrypt and runs a MCMC algorithm for n_iter. Returns the state having maximum score and also
    the last few states
     """
    M            = len(W)
    Beta         = Beta_start
    current_X    = [0]*M # We start with all 0's
    state_keeper = []
    best_state   = ''
    score        = 0

    for i in range(n_iter):
        state_keeper.append(current_X)
        proposed_X             = create_proposal(current_X,W,W_max)

        score_current_X        = score_state_log(current_X,G,Beta)
        score_proposed_X       = score_state_log(proposed_X,G,Beta)
        acceptance_probability = min(1,math.exp(score_proposed_X-score_current_X))
        if score_current_X>score:
            best_state = current_X
        if random_coin(acceptance_probability):
            current_X = proposed_X
        if i%500==0:
            Beta += Beta_increments
        # You can use these below two lines to tune value of Beta
        #if i%20==0:
        #    print "iter:",i," |Beta=",Beta," |Gold Value=",np.dot(current_X,G)

    return state_keeper,best_state

max_state_value =0
Solution_MCMC = [0]
for i in range(10):
    state_keeper,best_state = MCMC_Golddigger(50000,W,G,W_max,0.0005, .0005)
    state_value=np.dot(best_state,G)
    if state_value>max_state_value:
        max_state_value = state_value
        Solution_MCMC = best_state
    print "{}th search".format(i),str(Solution_MCMC)

print "MCMC Solution is :" , str(Solution_MCMC) , "with Gold Value:", str(max_state_value)
