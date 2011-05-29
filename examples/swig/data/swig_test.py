import fft
import time
import math

def main():
    print "Running fast FFT in C from Python"

    reals = fft.floatArray(256)
    imags = fft.floatArray(256)
    for i in range(0, 256):
        x = i / 256.0
        reals[i] = math.asin(x)
        imags[i] = 0

    # call C function
    fft.smbFft(reals, imags, 256, 1)

    print "FFT complete"
    # print magnitudes
    for i in range(0,256):
        real = reals[i]
        imag = imags[i]
        print math.sqrt(real*real + imag*imag)

    time.sleep(2)    
    

if __name__ == "__main__":
    main()
