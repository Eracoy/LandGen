import random,math

def cosinter(a, b, x):
    #return(a*(1-x)+b*x); #Linear interpolation return. much faster, but not as smooth
    f = (1 - math.cos(x * 3.1415927)) * .5
    return  a*(1-f) + b*f

def enlarge(small,factor):#expand and interpolate 1d array
    large=[0 for a in range(len(small)*factor)] #output array
    for n in range(len(small)):
        large[factor*n]=small[n] #transfer known values to output
        
    for n in range(len(large)): #interpolate to fill in zeros
        smalln=int(math.floor(n/factor))
        a=small[smalln]
        b=small[(smalln+1)%(len(small))]
        large[n]=cosinter(a,b,(n%factor)/float(factor))

    return large

def enlarge2d(small,factor):
    sx=len(small)
    lx=sx*factor
    half=[[0 for a in range(lx)]for b in range(sx)]
    halfflip=[[0 for a in range(sx)]for b in range(lx)]
    large=[[0 for a in range(lx)]for b in range(lx)]
          
    for n in range(len(small)):#horizontal expand 1
        half[n]=enlarge(small[n],factor)
          
    for a in range(sx):#flip array from AxB to BxA
        for b in range(lx):
            halfflip[b][a]=half[a][b]

    for n in range(lx):#horizontal expand 2
        large[n]=enlarge(halfflip[n],factor)
    
    return large

def perlin(size,amp):
    octave1=[[0 for a in range(size)]for b in range(size)]
    for a in range(size):
        for b in range(size):
            octave1[a][b]=random.randint(-amp,amp)

    output=enlarge2d(octave1,size)
    return output
