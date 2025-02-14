# Title:  	Mad Libs
# Author: 	Thomas Luong
# Purpose:	Creates a story based on verbs, adjectives and nouns that the user inputs
# Usage:	Practice python functions and reusability

# Notes:	Create Mad Libs style game where user inputs certain types of words
#			Story doesn't have to be too long but should have some sort of story line.

# Subgoals:
#			If user puts in a name, change first letter to capital letter
#			Change the word "a" to "an" when next word in sentence begins with a vowel





'''

One day, a curious __(fav noun)__ decided to _(verb)_through a _(adjective)_ forest.
It moved _(adverb)_, hoping to adviod the teriffying _(silly animal sound_ lurking nearby.
Suddenly, out of nowhere, a _(vehicle)_ crashed into a tree, and _(number)_ clowns jumped out!
"Who ordered this chaos?" yelled a frustrrated _(profession)_, holding a plate of _(type of food).
Everyone froze as the clowns started doing backflips.
Just then, the _(silly sounding animal)_ emerged, but instead of being scary,
it shout "_(something you's scream at a ghost)!_"
Everyone laughed so hard, the cloens gave up their act and joined the _(profession)_ for lunch.
The moral of the story? Never trust a _(vehicle)_ with _(number)_ clowns in it.
It might lead to lunch with a _(silly animal sound)_!

'''

from time import sleep
import datetime

now = datetime.datetime.now()

def madlibs():
	print("Madlibs starting, please enter the words below: ")
	print("------------------------------------------------")
	noun = input("Your fav Marvel character: ")
	verb = input("A verb that describe the superpower of that character: ")
	adjective = input("Name an adjective that reminds you of your mom: ")
	adverb = input("Give me an abverb that describes the speed your walking, (ends in -ly): ")
	animal = input("A cute animal: ")
	vehicle = input("A type of vehicle: ")
	number = input("A random number: ")
	profess = input("Give me a profession: ")
	food = input("Your favorite food: ")
	scream = input("A funny quote from a movie/internet meme: ")

	print("\n------------------------------------------------")
	print("Word gathering complete.  Creating story...")
	sleep(5)
	print("\n\nOne day, a curious " + noun + " decided to " + verb + " though a " + adjective + " forest. ")
	sleep(2)
	print("It moved " + adverb + ", hoping to adviod the teriffying " + animal + " lurking nearby.")
	sleep(2)
	print("Suddenly, out of nowhere, a " + vehicle + " crashed into a tree, and " + number + " clowns jumped out!  ")
	sleep(2)
	print("\"Who ordered this chaos?\" yelled a frustrrated " + profess + ", holding a plate of " + food + ". ")
	sleep(2)
	print("Everyone froze as the clowns started doing backflips.")
	sleep(1)
	print("Just then, the " + animal + " emerged, but instead of being scary, ")
	sleep(2)
	print("it shout, \"" + scream+ "!\" ")	
	sleep(2)
	print("Everyone laughed so hard, the cloens gave up their act and joined the " + profess +" for lunch.")
	sleep(2)
	print("The moral of the story? Never trust a " + vehicle + " with " + number + " clowns in it.")
	sleep(2)
	print("It might lead to lunch with a " + animal+ "!")
	sleep(2)
	print("\nTime to generate story: " +str(datetime.datetime.now() - now))
	print("\nThe end.\n\n")

madlibs()


