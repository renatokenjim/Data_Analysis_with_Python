import numpy as np

def calculate(list):

    if len(list)<9:
        raise ValueError('List must contain nine numbers.')
    # convert into 2D numpy array
    matrix = np.empty((0,3))
    for n in range(int(len(list)/3)):
        arr = list[n*3 : n*3+3]
        matrix = np.vstack((matrix,arr))
    #print(matrix)
    calculations = {}
    
    # mean
    calculations['mean'] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    # variance
    calculations['variance'] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    # std
    calculations['standard deviation'] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    # max, min, sums
    calculations['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    calculations['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    calculations['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

    return calculations