#include "body.h"

//contains the (at first) free falling bodies in the many 
//body problem. later electromagentic and dissipative effects may be 
//considered (and much later potentially other effects) Initially it will be 
//newtonaian with no higher order approximations. later it is possible higher 
//order approximations will be considered. 

//since I am initially implementing 
//newtonain mechanics, I am implementing three d space and one 
//dimensional time. 
  
//masses have size and can merge in reality. Im beginning with point masses.
  
Body::Body(vector<double> posinit, double tinit, double massinit),
  pos(posinit),time(tinit),mass(massinit){
  
