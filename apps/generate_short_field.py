import numpy as np
l = np.zeros(64,dtype=np.complex64)
l[-24+32]=complex(1,1)
l[-16+32]=complex(1,1)
l[-4+32]=complex(1,1)
l[12+32]=complex(1,1)
l[16+32]=complex(1,1)
l[20+32]=complex(1,1)
l[24+32]=complex(1,1)
l[-20+32]=complex(-1,-1)
l[-12+32]=complex(-1,-1)
l[-8+32]=complex(-1,-1)
l[4+32]=complex(-1,-1)
l[8+32]=complex(-1,-1)
l = l * 1.472 # This is sqrt(13/6) in other places in the documentation
ifft = np.fft.ifft(l,n=64)
time_domain = np.concatenate((ifft,ifft,ifft))
time_domain = time_domain[:161]
return time_domain

 
