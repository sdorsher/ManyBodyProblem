import RK4implicit
import numpy as np

def RK4adaptive(h,dtmax,t,xvec,f,delta):
    t1,x1=RK4implicit.RK4implicit(h,t,xvec,f)
    t2,x2=RK4implicit.RK4implicit(2*h,t,xvec,f)
    #print(x1-x2)
    rho=30*h*delta/np.sqrt(np.sum((x1[0:3]-x2[0:3])**2))
    repeat=False
    hnew=h
    epsilon=1e-6
    if np.abs(np.abs(rho)-1)<epsilon:
        repeat=False
    elif np.abs(rho)>1:
        repeat=False
    elif np.abs(rho)<1:
        repeat=True
    hnew*=rho**.25
    if hnew>=dtmax-epsilon:
        repeat=False
        hnew=dtmax
    tfinal = t1
    xfinal = x1
    if repeat:
        tfinal =t
        xfinal = xvec
    return repeat, hnew, h, tfinal, xfinal, rho
