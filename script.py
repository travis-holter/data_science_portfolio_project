# This line imports the csv package which is required to read the .csv file, specifically using DictReader.
import csv

# This section contains methods that take data, peform calculations, and retrun a useful aggregate/result.

# This method takes in a list of ages and returns their average. The list is expected to contain ints.
def findAverageAge(ages):
    # This is the formula to calculate an average.
    return sum(ages) / (len(ages))

# This method takes in a list of regions and returns the one that is the most populated.
def findMajorityRegion(regions):
    hash = {}
    maxValue = 0
    result = ''
    # This loop populates a dictionary/hash with the regions, and then counts their occurance.
    for el in regions:
        if el in hash.keys():
            hash[el] += 1
        else:
            hash[el]= 0
    # This loop goes through the regions/keys in the hash and sets the one with the most vaules to result variable.
    for key in hash.keys():
        if hash[key] > maxValue:
            maxValue = hash[key]
            result = key
    return result

# This method takes in a 2d list that contains [smoking status, medical costs] and returns how much smokers pay more than non-smokers, on average.
# In the 'smoking' column, a row contains either 'yes' or 'no'.
def findCostIncreaseForSmokers(smokerAndCost):
    numSmokers = 0
    numNonSmokers = 0
    smokersTotalCost = 0
    nonsmokersTotalCost = 0
    # This loop goes through list and populates the above variables with the totals of smokers/nonsmokers and their total costs.
    for el in smokerAndCost:
        if el[0] == 'yes':
            numSmokers += 1
            smokersTotalCost += float(el[1])
        else:
            numNonSmokers += 1
            nonsmokersTotalCost += float(el[1])
    # This line returns the difference in the averages of costs for smokers compared to non smokers.
    return (smokersTotalCost/numSmokers) - (nonsmokersTotalCost/numNonSmokers)

# This method takes in a list of costs and returns their average. It expects the list to contain ints.
def averageCost(costs):
    return (sum(costs)/len(costs))
        
# This block opens the csv file, organizes the data, calls the methods above, and prints the results.
with open('insurance.csv','r',newline='') as file:
    reader = csv.DictReader(file)
    ages = []
    regions = []
    smokersAndCost = []
    totalCosts = []
    totalCostsParents = []
    # This loop goes through the data and populates the above lists to be used as arguments for the methods.
    for row in reader:
        regions.append(row['region'])
        ages.append(int(row['age']))
        smokersAndCost.append([row['smoker'],row['charges']])
        totalCosts.append(float(row['charges']))
        if int(row['children']) > 0:
            totalCostsParents.append(float(row['charges']))
    # These lines call the methods and print the results. There is some string formatting and rounding so the display looks nice and is readable.
    print("Average age of patients: "+ str(round(findAverageAge(ages),1))+" years")
    print('Majority of participants are from: '+findMajorityRegion(regions))
    print("Smokers pay this much more on average than Non-Smokers: $"+str(round(findCostIncreaseForSmokers(smokersAndCost),2)))
    print("The average costs for a person is: $"+str(round(averageCost(totalCosts),2)))
    print("The average costs for a person who is a parent is: $"+str(round(averageCost(totalCostsParents),2)))
