#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def NewtonianForce(mass1,mass2, r):
    return mass1*mass2/r/r;

def RK4(h,t,y,f):
    k1= h*f(t,y)
    k2=h*f(t+h/2.,y+h*k1/2.)
    k3=h*f(t+h/2.,y+h*k2/2.)
    k4=h*f(t+h,y*+h*k3)
    return y+1/6.*(k1+2*k2+2*k3+k4)


#dv1dt=u1
#du1dt=Sum(F1i) excluding F11
#dv2dt=u2
#du2dt=Sum(F2i) excluding F2
#etc


def RHSU(u2):
    return u2;

def RHSF(Farr):
    return (np.sum(Farr,0)-np.trace(Farr))/2.;

def InitialData():
    random.seed(a=36);
    size1=10
    size2=50
    size3=10000
    masscategory1=0.001*np.random.uniform(.9,1.1,size1); #Msun (jupiter)
    masscategory2=0.00001*np.random.uniform(0.2*5,size2); #Msun (Earth)
    masscategory3=0.0000001*np.random.uniform(0.01,100,size3); #comet
    #initially use an in plane orbit with random starting locations relative to the x axis
    phi0category1=np.random.uniform(0,1,size1);
    phi0category2=np.random.uniform(0,1,size2);
    phi0category2=np.random.uniform(0,1,size3);
    orbitangle1=np.zeros(size1);
    orbitangle2=np.zeros(size2);
    orbitangle3=np.zeros(size3);
    

