#Need to run simulation function to get trafficinfo variable
#Density needs to match one of the possible densities from the number of spaces exactly, i.e. if there are 10 spaces then only densities that are multiples of 0.1 are valid.

def Space_Time_Plot(l,time,lane,density,trafficinfo):
    
    spacefunctions = dict()
    
    n = density*l*lane #determines the car number that the user wants to plot
    
    initpositions = trafficinfo[1][n-1][:,1,:][0]
    print initpositions
    
    k = 0
    for i in range(l):
        if initpositions[i] == 1:
            spacefunctions[k] = i
            k += 1
    
    print spacefunctions
    
    
Space_Time_Plot(l,time,lane,0.3,trafficinfo)
