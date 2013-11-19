import re, sys
import CircuitML as cml
import neuroml.v2 as nml
import numpy as np
from numpy.lib.scimath import sqrt
from scipy.sparse import coo_matrix

class Units(object):
    @staticmethod
    def _applyUnit(originalValue, unit):
        if unit == 'm':
            value = originalValue * 1e-3
        if unit == 'u':
            value = originalValue * 1e-6
        elif unit == 'n':
            value = originalValue * 1e-9
        elif unit == 'p':
            value = originalValue * 1e-12
        return value
    @staticmethod
    def read(word):
        v = re.match(r'-?([0-9]*(\.[0-9]+)?)([eE]-?[0-9]+)?[\s]*(V|mV|S|mS|uS|nS|pS|s|ms|F|uF|nF|pF|A|uA|nA|pA|S|mS|uS|nS|pS)', word)
        if not v: raise ValueError
        v = v.groups()

        value = 0.0
        if v[2] and v[0]: value = np.float64(v[0] + v[2])
        elif v[0]: value = np.float64(v[0])
        else: raise ValueError

        if len(v[3]) == 2: value = Units._applyUnit(value, v[3][0])
        if word[0] == '-': value *= -1
        return value

class inputSignalBlock:
    def __init__(self, N, dt, number):
        self.duration = N        # Duration of signal is seconds
        self.timeStep = dt        # Time step of signal in seconds
        self.M = number            # Number of sets of input signals
    def saveInputSignal(self, signal):
        self.inputSignal = signal.copy().astype(np.float32)
    def getInputSignal(self):
        return self.inputSignal.copy()

def parse(inFileName):
    try:
        lpuSpecification = cml.nml.etree_.parse(inFileName)
        rootNode = lpuSpecification.getroot()
        rootTag, rootClass = cml.nml.get_root_tag(rootNode)
        if rootClass is None:
            rootClass = cml.LpuSpecification
        rootObj = rootClass.factory()
    except Exception as e:
        raise IndexError('Utils.parse:  Error trying to parse {0}\n\tInner exception: '.format(inFileName) + e.args[0]), None, sys.exc_info()[2]

    try:
        rootObj.build(rootNode)
    except IOError as e:
        raise IOError('PARSER: Your file ' + inFileName + ' is not in a proper format. Inner I/O error({0}): {1}'.format(e.errno, e.strerror))
    except:
        raise
    return rootObj
def buildSpace(spaceType, shape):
    if (spaceType == 'Grid_1D' or
        spaceType == 'Grid_2D' or
        spaceType == 'Grid_3D'):
        return np.arange(shape, dtype = np.float64)
    elif spaceType == 'Hexagonal':
        return _hexagonalPositions(shape[0], shape[1], 1)
    return None
# TODO: right now it supports only odd number of columns and rows
def _hexagonalPositions(nrow, ncol, radius):
    X = np.tile(np.arange(ncol) * 1.5 * radius, (nrow, 1)) + radius
    Y = np.tile(np.arange(nrow) * sqrt(3) * radius, (ncol, 1)).T + radius
    Y = Y + np.tile([0, sqrt(3) / 2 * radius], (nrow, np.floor(ncol / 2)))
    X = np.reshape(X, (X.size), order = 'F')
    Y = np.reshape(Y, (Y.size), order = 'F')
    return np.array([X, Y]).T
def getId(value): return int(value[value.find('[') + 1:value.find(']')])
def getName(value): return value.split('[')[0]
def getPath(value): return value.split('/')
def isComponent(attribute):
    if issubclass(type(attribute), nml.AbstractCell) or \
        issubclass(type(attribute), nml.ConductanceBasedSynapse) or \
        type(attribute) is cml.LpuOutputIaF or \
        type(attribute) is cml.LpuInputIaF or \
        type(attribute) is cml.LpuSpecification:
            return True
    else:
        return False
def isSimpleElement(elem):
    if issubclass(type(elem), nml.AbstractCell) or \
        type(elem) is cml.LpuOutputIaF or \
        type(elem) is cml.LpuInputIaF:
            return True
    else:
        return False
def getComponents(lpu):
    pass
def getComponentFromArrayById(comp_id, arr):
    for elem in arr:
        if elem.get_id() == comp_id: return elem
def createCOO(component, dictionary):
    if not dictionary.has_key(component):
        return coo_matrix(np.zeros((1, 1))), coo_matrix(np.zeros((1, 1)))
    comp = dictionary[component]
    coo = coo_matrix(dictionary[component])
    nnz = np.count_nonzero(comp)
    conn = coo_matrix(np.ones((comp.shape[0], comp.shape[1]), dtype = type(None)))
    conn.data = np.zeros((nnz, len(coo.data[0].get_PropertiesArray())), dtype = np.float64)
    conn.row = coo.row
    conn.col = coo.col
    return conn, coo
def idxDict(dest, dest_key, pop, ext, qte):
    for i in xrange(qte):
        for val in ext:
            temp = {}
            for key in ext[val]:
                name = pop[:pop.rfind('/')] + '[' + str(i) + ']/' + removeUpperLevel(key)
                # name = pop[:pop.rfind('/')] + '[' + str(i) + ']' + key[key.find('/'):]
                temp[name] = ext[val][key]
            if dest.has_key(val):
                dest[val] = dict(dest[val], **temp)
            else:
                dest[val] = temp
    return
def concatWithChar(arr, ch):
    out = ""
    for s in arr:
        out += s + ch
    return out[:-1]
def removeUpperLevel(string): return string[string.find('/') + 1:]
def removeLowerLevel(string): return string[:string.rfind('/')]
def to_dense(coo):
    temp = np.zeros(coo.shape, dtype = np.object)
    i = 0
    for e in coo.data:
        temp[coo.row[i], coo.col[i]] = e
        i = i + 1
    return temp
def spikes3D(self, spikingActivity, T, dt, splitTime, maxSpikes, noNeurons):
        from mpl_toolkits.mplot3d import axes3d
        import matplotlib.pyplot as plt
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator, FormatStrFormatter
        t = np.arange(0, 1, dt)
        num = int(T / splitTime) # Number of parts in which the time is segmented

        # x-axis represents the neuron tag
        X = np.array([np.arange(noNeurons)] * num)

        # y-axis represents the time window
        f = np.ones([num, noNeurons])
        Y = np.arange(0, T, splitTime)
        Y = Y.reshape(len(Y), 1)
        Y = f * Y
        # z-axis represents the spiking activity of a neuron within a time window
        Z = np.zeros([num, noNeurons])
        for i in range(num):
            for j in range(noNeurons):
                Z[i, j] = len(find(spikingActivity[j, int(i * splitTime / dt) : int((i + 1) * splitTime / dt)] == 1))

        # Generate the 3-D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')
        ax.scatter(X, Y, Z)
        ax.set_xlabel('Neuron Number ->')
        ax.set_ylabel('Time (s) ->')
        ax.set_zlabel('Spike Count ->')
        # ax.plot_wireframe(X, Y, Z)
        # surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
        plt.show()
