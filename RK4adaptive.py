import RK4implicit
import numpy as np

def RK4adaptive(h,t,xvec,f,delta):
    t1,x1=RK4implicit.RK4implicit(h,t,xvec,f)
    t2,x2=RK4implicit.RK4implicit(2*h,t,xvec,f)
    rho=30*h*delta/np.mean(np.abs(x1-x2))
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
    return repeat, hnew, h, t1, x1, rho
