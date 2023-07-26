import csv

def findAverageAge(ages):
    return sum(ages) / (len(ages))

def findMajorityRegion(regions):
    hash = {}
    maxValue = 0
    result = ''
    for el in regions:
        if el in hash.keys():
            hash[el] += 1
        else:
            hash[el]= 0
    for key in hash.keys():
        if hash[key] > maxValue:
            maxValue = hash[key]
            result = key
    return result

def findCostIncreaseForSmokers(smokerAndCost):
    numSmokers = 0
    numNonSmokers = 0
    smokersTotalCost = 0
    nonsmokersTotalCost = 0
    for el in smokerAndCost:
        if el[0] == 'yes':
            numSmokers += 1
            smokersTotalCost += float(el[1])
        else:
            numNonSmokers += 1
            nonsmokersTotalCost += float(el[1])
    return (smokersTotalCost/numSmokers) - (nonsmokersTotalCost/numNonSmokers)

def averageCost(costs):
    return (sum(costs)/len(costs))
        

with open('insurance.csv','r',newline='') as file:
    reader = csv.DictReader(file)
    ages = []
    regions = []
    smokersAndCost = []
    totalCosts = []
    totalCostsParents = []
    for row in reader:
        regions.append(row['region'])
        ages.append(int(row['age']))
        smokersAndCost.append([row['smoker'],row['charges']])
        totalCosts.append(float(row['charges']))
        if int(row['children']) > 0:
            totalCostsParents.append(float(row['charges']))
    print("Average age of patients: "+ str(findAverageAge(ages)))
    print('Majority of participants are from: '+findMajorityRegion(regions))
    print("Smokers pay this much more on average than Non-Smokers: "+str(findCostIncreaseForSmokers(smokersAndCost)))
    print("The average costs for a person is: "+str(averageCost(totalCosts)))
    print("The average costs for a person who is a parent is: "+str(averageCost(totalCostsParents)))
