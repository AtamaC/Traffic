# Note that the Space Time plot function must be run before the Traffic
# Animation and that they must both use the same density

# 'space' is the variable returned by the Space Time Plot Function
def Traffic_Animation(space,l,time,lane,density):
    import Tkinter as tk
    import numpy as np
    
    cars = dict()
    v = dict()
    spots = dict()
    
    n = int(density*l*lane)
    w = 1200/l
    window = tk.Tk()
    canvas = tk.Canvas(window, width = 1200, height = lane*(w+50))
    canvas.pack()
    
    for i in range(n):
        cars[i] = [canvas.create_rectangle(w*space[i][0],20,w*space[i][0]+w,20+w,fill="red")]
        cars[i].append(w*space[i][0])
        
    for i in range(l-1):
        spots[i] = canvas.create_line(w*(i+1),0,w*(i+1),lane*(w+50))
    
    for k in range(n):
        v[k] = []
    
    for t in range(time - 1):
        for k in range(n):
            p1 = space[k][t]
            p2 = space[k][t+1]
            v[k].append(int((round((p2 - p1)*w/10))))
    
    
    for t in range(time - 1):
        for p in range(10):
            for i in range(n):
                if cars[i][1] < 1200:
                    dx = v[i][t]
                else:
                    dx = -(1200 - v[i][t])
                cars[i][1] += dx
                canvas.move(cars[i][0],dx,0)
                canvas.after(10)
                canvas.update()

    window.mainloop()
