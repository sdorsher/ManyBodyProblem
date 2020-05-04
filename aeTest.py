def localMinimumIndex(values):
    mins=[]
    secondtolastval=values[0]
    lastval=values[1]
    for i in np.arange(2,len(values)):
        thisval=values[i]
        if thisval>lastval and lastval<secondtolastval:
            mins.append(i-1)
        secondtolastval=lastval
        lastval=thisval
    return mins

def findPerApHelion(npstar1x,theta0,ecc0,rad0):
    b=np.tan(theta0)
    x0,y0=npstar1x[0,0],npstar1y[0,1]
    mostb = []
    mostb1 = np.abs(1-npstar1x[:,1]/npstar1x[:,0]/b)
    mostb2=np.abs(1-b/npstarx1[:,1]*npstar[:,0])
    for b1,b2 in zip(mostb1,mostb2):
        mostb.append(min(b1,b2))
    indexminmostb=np.argmin(mostb) #aphelion
    indexminmostb2=np.argmin(mostb[20:20+indexminmostb-20]) #perihelion
    assert np.abs(npstarx1[0,0]-npstar1[indexminmostb,0])<1, "did not find aphelion"
    assert np.abs(indexminmostb2/indexminmostb-1)<0.05, "did not find perihelion"
    mins=localMinimumIndex(mostb[0:indexminmostb2+1])
    coordper=[npstar1x[mins[0],0],npstar1x[mins[0],1]]
    coordap=[npstar1x[indexminmostb2,0], npstar1x[indexminmostb2,1]]
    print("aphelion", coordap)
    print("perihelion", coordper)
    rp=np.sqrt(np.sum(np.array(coordper)**2))
    ra=np.sqrt(np.sum(np.array(coordap)**2))
    print("r_ap", ra)
    print("r_per", rp)
    a=1/2*(rp+ra)
    print("a", a)
    e=(ra-rp)/(ra+rp)
    print("e",e)
    deltaa=np.abs(a-rad0)/rad0
    deltae=np.abs(e-ecc0)/ecc0
    print("delta a", deltaa)
    print("delta e", deltae)
    return coordper,coordap,rp,ra,e,a,deltae,deltaa
