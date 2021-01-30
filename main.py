import statistics
from statistics import mode

def most_common(List):
    return(mode(List))

List = [1,2,3,1,2,3,2]
print(most_common(List))