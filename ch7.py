# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:42:05 2022

@author: Dolagy Baky
"""

import random
import networkx as nx
import string
import matplotlib.pyplot as plt
import networkx as nx
from simulation import Simulation
G = nx.gnm_random_graph(20, 50)
nx.draw(G)



def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'asleep'
    return state



print(initial_state(G))



G = nx.gnm_random_graph(20, 50)
nx.draw(G)



def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = random.choice('ABCD')
    return state


initial_state(G)

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        # Caveat: what if the node has no neighbors?
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state



test_state = initial_state(G)
state_transition(G, test_state)







sim = Simulation(G, initial_state, state_transition, name='Voter Model')

sim.draw()

sim.run(40)


sim.draw()


sim.plot()




def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state




def state_transition_async(G, current_state):
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state

def state_transition_async(G, current_state):

    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state




sim = Simulation(G, initial_state, state_transition_async, name='Async Voter Model')
sim.run(40)
sim.plot()


def stop_condition(G, current_state):
    unique_state_values = set(current_state.values())
    is_stopped = len(unique_state_values) <= 1
    return is_stopped


sim = Simulation(G, initial_state, state_transition, stop_condition, name='Voter model')
sim.run(100)

sim.steps

sim.plot()



def state_transition_async_rewiring(G, current_state):

    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
         
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]

            neighbor = random.choice(list(G.neighbors(node)))
            if current_state[node] != current_state[neighbor]:
                G.remove_edge(node, neighbor)
            
    return current_state



sim = Simulation(G, initial_state, state_transition_async_rewiring, stop_condition,
                 name='Voter Model with rewiring')
sim.draw()




sim.run(40)
sim.draw()
sim.plot()
G = nx.gnm_random_graph(20, 50)
nx.draw(G)

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'S'
    
    patient_zero = random.choice(list(G.nodes))
    state[patient_zero] = 'I'
    return state


initial_state(G)



MU = 0.1
BETA = 0.1

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'I':
            if random.random() < MU:
                next_state[node] = 'S'
        else: # current_state[node] == 'S'
            for neighbor in G.neighbors(node):
                if current_state[neighbor] == 'I':
                    if random.random() < BETA:
                        next_state[node] = 'I'

    return next_state

test_state = initial_state(G)
state_transition(G, test_state)

sim = Simulation(G, initial_state, state_transition, name='SIS model')


sim.draw()
sim.run(25)
sim.draw()

sim.plot()
