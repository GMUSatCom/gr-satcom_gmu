
import numpy as np
from bitarray import bitarray
import pmt
import ctypes
# TODO
# 1. convert bitarray to using numpy.unpackbits()

def indx_gen(max_val):
    n = -1
    while True:
        n += 1
        if n == max_val:
            n = 0
        yield n

class OFDM_Params:
    def __init__(self):
        # Rate code used in signal Field
        self.rate_code = '1101'
        #Channel Spacing
        self.bw = 20
        # the data rate which depends on the channel bandwidth
        self.data_rate = 6
        # the number of coded bits per subcarrier
        self.n_cbpsc = 1
        # number of coded bits per OFDM symbol
        self.n_cbps = 48
        # number of data bits per OFDM symbol
        # BPSK = 1, QPSK = 2, etc
        self.n_dbps = 24
        # This is the coding rate. and represents. a fractrion of data bits over coded bits
        self.r = 1.0/2.0
    def vec_test(self):
        test_bytes = '\x04\x02\x00\x2E\x00\x60\x08\xCD\x37\xA6\x00\x20\xD6\x01\x3C\xF1\x00\x60\x08\xAD\x3B\xAF\x00\x00' + 'Joy, bright spark of divinity, Daughter of Elysium, Fire-insired we trea' + '\x67\x33\x21\xb6'
        # print(len(test_bytes))
        vec = np.fromstring(test_bytes,dtype=np.uint8)
        pmt_vec = pmt.make_u8vector(len(vec),0)
        for i,val in enumerate(vec):
            pmt.u8vector_set(pmt_vec,i,int(val))
        return pmt_vec

class ShortField:
    def __init__(self):
        self.sequence = np.array([1,-1,1,-1,-1,1,-1,-1,1,1,1,1] ,dtype=np.complex64) * complex(1,1) * 1.472
        # the constant 1.472 is sqrt(13/6) in some places in the documentation
        self.subcarriers= ([-24,-20,-16,-12,-8,-4,4,8,12,16,20,24],)
        self.subcarrier_count = 12
        self.periodic_extend_to = 161

class LongField:
    def __init__(self):
        self.sequence = np.array([1, 1,-1,-1,1,1,-1,1,-1,1,1,1,1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1],dtype=np.complex64)
        self.subcarriers = (range(-26,0) + range(1,27),)
        self.subcarriers_count = 52
        self.cyclic_prefix = 64/4
        self.periodic_extend_to = 161


class SignalField:
    valid_bws = [20,10,5]
    valid_rates = [6,3,1.5,9,4.5,2.25,12,18,24,36,48,54,13.5,27]
    max_len = np.uint32((2**12)-1)
    rate = None
    rate_dict = None
    length = None
    bw = None
    signal_tail = '000000'
    # review this later there are most likley errors here since it is hand coded
    rate_dict = {(20,6):'1101',(10,3):'1101',(5,1.5):'1101',(20,9):'1111',(10,4.5):'1111',(5,2.25):'1111',(20,12):'0101',(10,6):'0101',(5,3):'0101',(20,18):'0111',(10,9):'0111',(5,4.5):'0111',(20,24):'1001',(10,12):'1001',(5,6):'1001',(20,36):'1011',(10,18):'1011',(5,9):'1011',(20,48):'0001',(10,24):'0001',(5,12):'0001',(20,54):'0011',(10,27):'0011',(5,13.5):'0011'}
    def __init__(self,bw,rate,length):
        if bw in self.valid_bws:
            self.bw = bw
        else:
            raise Exception("invalid bandwidth. select (20,10,5)")

        if rate in self.valid_rates:
            self.rate = rate
        else:
            raise Exception("invalid rate. make sure it is available for your bandwidth")
        
        if np.uint32(length) < self.max_len:
            self.length = np.uint16(length)
        else:
            raise Exception("length is too long")
        

    def encode(self):
        # calculate parity
        rate = bitarray(self.rate_dict[(self.bw,self.rate)])
        r = bitarray([False])
        length = bitarray("{0:0>12b}".format(self.length)[::-1],endian='big')
        first_part = rate + r + length
        count = 0
        parity = False
        for bit in first_part:
            if bit == True:
                count += 1
        if count % 2: 
            parity = True
        return rate + r + length + bitarray([parity]) + bitarray(self.signal_tail)

    def parse(self):
        # implement later
        pass


def parity(input):
    sum = 0
    for b in  input:
        if b == True:
            sum += 1
    return sum % 2

def convolutional_encoder(input):
    # input is a bitarray()
    #
    output = bitarray()
    state = bitarray([False]* 7)
    for b in input:
        state.insert(0,b)
        state.pop()
        # switch from hardcoding these values
        #                                      1011011 orig
        #                                      1101101
        output.append(parity(state & bitarray('1011011'))) # wifi standard octal numbers 0133 and 0171
        #                                      1111001 orig                                      
        #                                      1001111                                      
        output.append(parity(state & bitarray('1111001')))
    return output

def puncturer(input,rate="2_3"):
    # input is the parity bit stream
    # expand to high throughput and DMG 1/2 2/3 3/4 5/6
    # make some object that has all of this hardcoded information
    r2_3 = [[1,1,1,1,1,1],[1,0,1,0,1,0]]
    r3_4 = [[1,1,0,1,1,0,1,1,0],[1,0,1,1,0,1,1,0,1]]

    if rate == "2_3":
        r = r2_3
    else:
        r = r3_4

    combined = [0] *(len(r[0]) + len(r[1]))
    combined[0::2] = r[0]
    combined[1::2] = r[1]

    remainder = len(input) % len(combined)
    combined =  (len(input)/len(combined)) * combined + combined[0:remainder]

    assert(len(input) == len(combined))
    for i in range(0,len(input)):
        if not combined[i]:
            input.pop(i)
    return input

def interleaver(input,reverse,ncbps,nbpsc):
    """
    reverse = deinterleave
    ncbps is the number of bits in an ofdm symbol. This changes based on modulation type
    nbpsc is the number of bits per subcarrier, or the number of bits in one ofdm symbol, 
    for bpsk this would be 1, for qpsk this would be 2 etc.
    """
    assert(len(input) % ncbps == 0)
    first = [0] * ncbps
    second = [0] * ncbps
    out = bitarray([0] * len(input))
    s = max([1,nbpsc/2])
    
    for j in range(0,ncbps):
        first[j] = s * j/s + (j + (16*j)/ncbps) % s

    for i in range(0,ncbps):
        second[i] = 16 * i - (ncbps -1) * ((16*i)/ncbps)
    
    for i in range(0,len(input)/ ncbps):
        for k in range(0,ncbps):
            if reverse:
                out[i*ncbps + second[first[k]]] = input[i * ncbps + k]
            else:
                out[i * ncbps + k] = input[i * ncbps + second[first[k]]]
    return out


def scrambler(inpt,state):
    state = bitarray(state)
    output = bitarray('')
    inpt = bitarray(inpt)
    for i in inpt:
        feedback = state[6] ^ state[3]
        output.append(i ^ feedback)
        state.insert(0,feedback)
        state.pop()


    return output
class conv_coder():
    def __init__(self):
        self.state = np.zeros(7,dtype=np.uint8)

    def code_bit(self,bit):
        assert(bit == 1 or bit == 0)
        assert(type(bit) == type(np.uint8(1)))
        gen1 = np.array([1,0,1,1,0,1,1],dtype=np.uint8)
        gen2 = np.array([1,1,1,1,0,0,1],dtype=np.uint8)
        self.state = np.roll(self.state,1)
        self.state[0] = bit 
        print(self.state)
        bit1 = parity(self.state & gen1)
        bit2 = parity(self.state & gen2)

        return np.array([bit1,bit2],dtype=np.uint8)
        

if __name__ == "__main__":
    ncbps = 192
    nbpsc =  4
    # assert(len(input) % ncbps == 0)
    first = np.zeros(ncbps)
    second = np.zeros(ncbps)

    out = "idk"
    s = max([1,nbpsc/2])
    
    for j in range(0,ncbps):
        print(j+ (16*j)/ncbps)
        first[j] = s * (j/s) + (j + (16*j)/ncbps) % s
    # print(first)
    
    for i in range(0,ncbps):
        second[i] = 16 * i - (ncbps -1) * ((16*i)/ncbps)
    print(max(second))
    pass