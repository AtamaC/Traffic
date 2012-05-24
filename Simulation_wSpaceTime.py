#Need to run simulation function to get trafficinfo variable
#Density needs to match one of the possible densities from the number of spaces exactly, i.e. if there are 10 spaces then only densities that are multiples of 0.1 are valid.

def Space_Time_Plot(l,time,lane,density,trafficinfo):
    
    spacefunctions = dict()
    
    n = int(density*l*lane) #determines the car number that the user wants to plot
    
    initpositions = trafficinfo[1][n-1][:,1,:][0]
    print initpositions
    
    k = 0
    for i in range(l):
        if initpositions[i] == 1:
            spacefunctions[k] = [i]
            k += 1
    
    
    # builds a dictionary of lists with all the cars' distance traveled over the length of the simulation
    for i in range(time):
        for j in range(n):
            spacefunctions[j].append(trafficinfo[0][n-1][0,i,j]+spacefunctions[j][i])
    
    print spacefunctions
    
    
Space_Time_Plot(l,time,lane,0.3,trafficinfo)
