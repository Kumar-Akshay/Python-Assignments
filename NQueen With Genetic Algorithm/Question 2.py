import random #randomNumber
import copy #Deepcopy


#Random seletion of best goal fitness for population
def GeneticNQueens(population, fitness):
	generations = 100000 #Max Generation
	n = generations
	GoalFitness = Compute_GoalFitness(len(random.choice(population)))
	print ("\nProblem dimension: ", len(random.choice(population)), "x", len(random.choice(population))) 
	print ("Population size: ", len(population)) 
	print ("Fitness Goal Value: ", GoalFitness)
	print ("\nrunning...") 
	FitnessValue = {}
	for i in range(len(population)):
		FitnessValue[i] = FitnessFinder(population[i], GoalFitness)
	while n > 0: 
		new_population = []
		new_FitnessValue = {}
		a,m = FitnessInfo(FitnessValue) 
		for i in range(len(population)):
			x = random_selection(population, FitnessValue)
            #reproduce 
			child = reproduce(x)
			if random.uniform(0,1) < 0.2:#Mutation Probability compare
				child = mutation(copy.deepcopy(child)) #Child Mutation
			child_fitness = FitnessFinder(child, GoalFitness) #Child Fitness
			if child_fitness >= GoalFitness:
                #Result Array of possible position in chess board 
				print ("\n\n result\n All Possible Possition Of Queens in Chess Board \n", child," \n found in ", generations-n, " generations.\n" )
				return child
			new_FitnessValue[i] = child_fitness
			new_population.append(child)
		population = new_population
		FitnessValue = new_FitnessValue
		n -= 1
	print ("\nno solution found.\n")
	return None

def random_selection(population, FitnessValue):
	selection = None
	runningtotal = 0
	fitness_total = []
	for i in range(len(population)):
		runningtotal += FitnessValue[i]
		fitness_total.append(runningtotal)
	prob = random.uniform(0, fitness_total[-1])
	for i in range(len(population)):
		if fitness_total[i] > prob:
			return population[i]

#these range from a simple bit mutation flipping random Number
def mutation(child):
	return switch(1, child)

#Selection to better solutions chromosomes
def reproduce(x):
	return switch(1, x)

#Compute Fitness
def Compute_GoalFitness(n):
	GoalFitness = 0
	for i in range(n):
		GoalFitness += i
	return GoalFitness

#Find FitNess of Choromosone
def FitnessFinder(individual, GoalFitness):
	fitness_value = GoalFitness
	for i in range(len(individual)):
		j = 1
		while j < len(individual)-i:
			if (individual[i] == individual[i+j]+j) or (individual[i] == individual[i+j]-j):
				fitness_value -= 1
			j += 1
	return fitness_value


#Show the N*N Queen Possible Fitnesss
def FitnessInfo(d): 
	n = len(d)
	total = 0
	for i in range(n):
		total += d[i]
	a = total/n
	m = max(d.values())
	return a, m	


#made a population with random function
def switch(n, target):
	for i in range(n):
		j = random.randint(0, len(target)-1)
		k = random.randint(0, len(target)-1)
		target[j], target[k] = target[k], target[j]
	return target 


#Main
n = 8 #Total Number Of Queen 
population = []
base = list (range(1,n+1))#each chromosome will be a string of 8 numbers ranging from 1-8
for i in range(4):#initial population of four
	population.append(switch(5, copy.deepcopy(base)))
	#function Call 
GeneticNQueens(population, FitnessFinder)
