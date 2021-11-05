resultList = []
speedList = []
pre_result = 0.0
final_result = 0.0

numObserve = int(input("Enter the number of observations: "))

def getRunnerValue(speedList = [], *args):
    for j in range(len(speedList) - 1):
        speedNestedList1 = speedList[j]
        speedNestedList2 = speedList[j + 1]

        if (j + 1) > len(speedList) - 1:
            break

        pre_result = (speedNestedList2[1] - speedNestedList1[1]) / (speedNestedList2[0] - speedNestedList1[0])
        result = abs(pre_result)
        resultList.append(result)
    # Get the absolute value of the result, return it to the main, put each result in another list, and then execute another function to compare results, and get the biggest value and output it

def compareRunnerValue(resultList = [], *args):
    global final_result
    for k in range(len(resultList) - 1):
        if resultList[k] >= final_result:
            final_result = resultList[k]
    return final_result


if numObserve >= 2 and numObserve <= 100000:
    for i in range(numObserve):
        value1, value2 = input("Enter the values: ").split(" ")
        
        value1 = float(value1)
        value2 = float(value2)

        if value1 >= 0 and value1 <= 1000000000 and value2 >= -1000000000 and value2 <= 1000000000:
            value1 = float(value1)
            value2 = float(value2)

            speedList.append([value1, value2])

    sorted(speedList, key = lambda x: (x[0], x[1]))
    getRunnerValue(speedList)
    output = compareRunnerValue(resultList)
    print(output)