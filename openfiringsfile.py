from numpy import load

data = load('D:/Electrophysiological_Data/myriad_output/08082022/wpsoutput13/firings.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])