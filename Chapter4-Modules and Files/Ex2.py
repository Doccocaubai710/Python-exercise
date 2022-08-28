import numpy as np
def convert(a):
    res = np.array(a[0] / np.sum(a[0]))
    
    for i in range(1, a.shape[0]):
        res = np.concatenate( (res, a[i] / np.sum(a[i])))
    return res.reshape(a.shape)
print(convert(np.arange(0, 9).reshape(3, 3)))