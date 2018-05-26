import random
from sets import Set

    
def matchLines(rxLine, rxSet) :
    return (rxLine in rxSet)

try:
    fp = open('juice.dat', 'r')  

    line = fp.readline()
    while line :
        if "beginSet" in line :
            instructionSet = Set()
            line = fp.readline()
            while ("endSet" not in line):
                instructionSet.add(line)
                line = fp.readline()
            print instructionSet
            
            copySet = instructionSet.copy()

            inSet = True
            while (inSet and ((len(instructionSet) > 0))) : 
                rxLine = ''.join(random.sample(copySet, 1))
                if (matchLines(rxLine, instructionSet)) :
                    instructionSet.remove(rxLine);
                else :
                    inSet = False
                    
            if (inSet) :
                print "PASS"
            else :
                print "FAIL"
                
finally:
    fp.close()
    

