# the traffic2 function must be defined before running
# l -> length of road
# time -> time steps of the simulation
# mv -> max velocity
# lane -> number of lanes
# returns a tuple of information necessary to run Space_Time_Plot

# note that the size of l with effect the runtime the most

def simulation(l,time,mv,lane):
    import numpy
    import pylab as py
    
    #initialize variables
    velarray = numpy.zeros((time))
    avgvelocity = numpy.zeros((l))
    avgcurrent = numpy.zeros((l))
    velocity = dict()
    loc = dict()
    

    for i in range(l): #runs the traffic simulation from from 1 car per lane to a car density of 1
        passdic = traffic2(i+1,l,time,mv,lane)
        velocity[i] = passdic['velocity']
        loc[i] = passdic['location']

        
        #builds an array of the average current for each density
        avgcurrent[i] = sum(velocity[i][:,time,:][0])/(float(lane*l))
    
    
        
    d = py.arange(1./l,1+1./l,1./l)
    py.plot(d,avgcurrent)
    
    py.ylim(0,(max(avgcurrent)+1))
    
    py.xlabel('density')
    py.ylabel('average current')
    py.title('Traffic Current')
    py.grid(True)
    py.show()
    
    return velocity,loc

