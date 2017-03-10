
def find_missing(a,b):

    c=set(a) ^ set(b)
  
    if a==b:
        return(0)
    
    elif  len (a)==len (b):
    
        return(0)
    
    else:
    
   
        return list(c)
