import RK4implicit
import numpy as np

def RK4adaptive(h,t,xvec,f,delta):
    t1,x1=RK4implicit.RK4implicit(h,t,xvec,f)
    t2,x2=RK4implicit.RK4implicit(2*h,t,xvec,f)
    rho=30*h*delta/np.mean(np.abs(x1-x2))
    repeat=False
    hnew=h
    if rho>1:
        repeat=False
    elif rho<1:
        repeat=True
    elif rho==1:
        repeat=False
    hnew*=rho**.25
    return repeat, hnew, h, t1, x1, rho
