import numpy as np
import math
import OrbitDiffEqAdaptive
def timestepAdaptive(numsteps,dt,xyuvaeqellipse,outputevery,delta):
    masses,xvec0,avec0=xyuvaeqellipse
    ODEeq= OrbitDiffEqAdaptive.OrbitDiffEqAdaptive(masses,xvec0,avec0,0.0,delta)
    #ODEeq.print2D()
    t=0.0
    star1x=[]
    star2x=[]
    star1a=[]
    star2a=[]
    times=[]
    rhoarr=[]
    dtarr=[]
    star1x.append(xvec0[0])
    star2x.append(xvec0[1])
    star1a.append(avec0[0])
    star2a.append(avec0[1])
    times.append(0.0)
    rhoarr.append(1.)
    dtarr.append(dt)
    outputevery=1
    for i in np.arange(1,numsteps):

        masses,xvec,avec,t,dt,dtlast,rho=ODEeq.timestepRK4ODE(i,dt)
        #ODEeq.print2D()
        if i%outputevery==0:
            star1x.append(xvec[0])
            star2x.append(xvec[1])
            star1a.append(avec[0])
            star2a.append(avec[1])
            times.append(t)
            dtarr.append(dtlast)
            rhoarr.append(rho)
    npstar2x=np.array(star2x)
    npstar1x=np.array(star1x)
    npstar2a=np.array(star2a)
    npstar1a=np.array(star1a)
    nptimes=np.array(times)

    return nptimes, npstar1x, npstar2x, npstar1a, npstar2a
