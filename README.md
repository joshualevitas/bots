# How I generate creatures
First we roll a 10 sided die to choose how many links our creature will have. We generate the torso, and then to creatre
the rest of the body of the creature, we roll a 3 sided die to choose which direction the next link will face (stemming from the previously added link).

Initially, every joint has a motor in my creatures, and I add a sensor with 1/2 probability.

# How creatures mutate each generation
Every child mutates with the following probabilities:

    * Remove motor Neuron / Add motor neuron (each with 1/20 probability) 
    * Change neuron weight (3/4)
    * Add / Remove sensor neuron (1/5)
    * Add link (1/20)
    * Remove link (1/20)

# Diagrams

[Generation Diagram](https://imgur.com/W7ry4HE), [Evolution Diagram](https://imgur.com/NmZsP6A)

[Fitness Curve](https://github.com/joshualevitas/bots/blob/a8/Fitnesses.png?raw=true)

Credit to /r/ludobots and pyrosim. All of my work is on top of these two sources, and relies heavily on the work of these two sources in order to try to learn something new.