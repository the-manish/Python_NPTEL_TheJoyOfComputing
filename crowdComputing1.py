# sort function bydefault sorts the data in ascending order
from statistics import mean
#from scipy import stats
Estimates=[23,34,56,67,100,2000,300,500,600,231]
Estimates.sort()
#m=stats.trim_mean(Estimates,0.1)
#print(m)
tv=int(0.1*len(Estimates))
Estimates=Estimates[:len(Estimates)-tv]
print(mean(Estimates))