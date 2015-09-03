# band name generator
import random


titles = ["gigantic", "sour", "steamy", "gross", "stupid",
          "ironic", "greasy", "tangy", "smelly", "small",
          "inventive", "spherical", "spiritual", "green",
          "blue", "pot bellied", "pickled", "prickly"]
          
adjs = ["tiny", "fat", "shiny", "ecclectic", "fluffy", "bright",
        "corrupt", "aggressive", "alarming", "amazing", "magical",
        "courageous", "fierce", "colorless", "red", "thoughtless",
        "smart", "delirious", "fabulous", "fergalicious", "dangerous"]
        
plural_nouns = ["apples", "oranges", "kiwis", "clementines",
                "wildabeasts", "mammoths", "rabbits", "sloths", "crashes",
                "spices", "eggs", "herbs", "pony tails", "bears", "snitches",
                "unicorns", "kermits", "signs", "indians", "cowboys", "cheerleader",]
                
def title():
	''' This function chooses a random title for the name '''
	return random.choice(titles)
	
def adj():
	''' This function chooses a random adj for the band '''
	return random.choice(adjs)
	
def plural_noun():
	return random.choice(plural_nouns)
	
def main():
	while true:
		name = raw_input("enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()
		
main()