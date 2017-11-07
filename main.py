from random import choice,randrange,random
from string import ascii_uppercase
import matplotlib.pylab as plt

#String to be reached at final, i.e. the fittest string
idealString = "MY NAME IS PINDIKANTI HITESH. I AM A GOOD BOY"

#Basic Variables to set a limit.
generations = 40
population = 2000

#Fuction to check the fittness of an input string: returns how many characters are at right place 
def checkFitness(string):
    fitness = 0
    for i in range(0,len(idealString)):
        if string[i] == idealString[i]:
            fitness += 1
    return fitness

#Fuction to perform crossovers between 2 strings: random 2 point crossover
def breed(str1,str2):
    i=randrange(0,len(str1))
    j=randrange(0,len(str2))
    if j<i:
        i,j = j,i
    return str1[0:i]+str2[i:j]+str1[j:]

#Function to perform mutation in the string: randomly choose a character and randomly replace it with a new character 
def mutate(string):
    i=randrange(0,len(string))
    return string[0:i]+choice(ascii_uppercase + " " + ".")+string[i+1:]
    


populationFitness = [[0,''.join(choice(ascii_uppercase + " " + ".") for i in range(len(idealString)))] for i in range(population)]
generation_data = []

for gen in range(generations):
     
    for pop in range(population):
        populationFitness[pop][0] = checkFitness(populationFitness[pop][1])

    #arrange population according to their fitness    
    populationFitness.sort(reverse=True)

    #Saving data for graphs
    all_fitness_scores = [populationFitness[i][0] for i in range(population)]
    generation_data.append([gen+1, all_fitness_scores[-1], all_fitness_scores[0], sum(all_fitness_scores)/population])
    
    #display the best member of the current population
    print "Generation ",gen+1," : Fitness = ",populationFitness[0][0]," Best Member = ",populationFitness[0][1]

    #kill the weakest 50% of the population and perform crossovers on the top 50%
    for pop in range(population/2,population):

        #breed 2 strings at random
        populationFitness[pop][1] = breed(populationFitness[randrange(0,population/4)][1],populationFitness[randrange(0,population/4)][1])

        #perform mutation at probability 20%
        if(random()<0.2):
            populationFitness[pop][1] = mutate(populationFitness[pop][1])

#display Graphs
plt.plot([generation_data[i][0] for i in range(generations)],[generation_data[i][2] for i in range(generations)],color='green',label='Max Fitness')
plt.plot([generation_data[i][0] for i in range(generations)],[generation_data[i][3] for i in range(generations)],color='blue',label='Average Fitness')
plt.plot([generation_data[i][0] for i in range(generations)],[generation_data[i][1] for i in range(generations)],color='red',label='Min Fitness')
plt.plot([generation_data[i][0] for i in range(generations)],[len(idealString) for i in range(generations)],color='black',label='Max Possible Fitness')
plt.legend()
plt.title('Genetic Algorithm: population=' +str(population))
plt.xlabel('Generations')
plt.ylabel('Fitness Score')
plt.show()
