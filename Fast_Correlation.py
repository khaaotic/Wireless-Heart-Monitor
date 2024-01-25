import numpy as np
from matplotlib import pyplot as plt

def Fast_Correlation(x,y):
  xylen = len(x) + len(y) - 1
  XFTT = np.fft.fft(x,xylen)
  YFFT = np.fft.fft(np.conj(y[::-1]), xylen)
  xyfreq = np.fft.ifft(XFFT * YFFT)
  return xyfreq
