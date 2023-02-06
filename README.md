# Scorpion Bot

I made a bot that I tried to make resemble a scorpion. It has six legs (3 on either side) and one "tail" (or rear leg). I noticed early on that there was some emergent behavior / evolution: It seemed as though the scorpion was trying to stand on its tail. It would jump and sometimes land on the tail, but most likely it would jump onto its tail and then fall over. I tried to evolve the robot to end up stable on its tail (but was ultimately unsuccessful. I did, however, think this emergent behavior was very interesting. I tried changing the fitness to see how high the robot would end up, meaning that standing on its tail would be its best bet. This helped a little, but ultimately did not change much.




Here is a video of a random scorpion bot in action (running very slowly on my old computer): https://youtu.be/5kVQc5WRqng

Here is a video of my first round of evolved scorpion: https://youtu.be/fnjXMIRRdMc




I then tried adding some differently shaped cubes to allow the scorpion to balance more easily:

Cube tail: https://youtu.be/BMk09wuztFk

Platform tail: https://youtu.be/uyFC89F2mgU

These new tails ended up being too heavy to allow the scorpion to jump onto its tail, so i removed them and reverted the fitness function to the original (x value), and now the scorpion consistently evolves to jump onto its tail again:

https://youtu.be/HawoMP2De9c




I do not know exactly why my bot exhibits this behavior, but again, I find it interesting. Adding more legs certainly changed the gait and behavior of my bot (relative to the quadruped), but it did not exactly improve it according to our original definition of fitness. More work into this, as well as a much more sophisticated understanding of what's going on under the hood could be an illuminating project and allow for a better understanding of this behavior.




To match our original definition of fitness (x coordinate), one could change the joint axes on the legs to move as spiders legs do (forward and backward as opposed to up and down). 








