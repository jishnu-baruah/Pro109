import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics

df = pd.read_csv('./Pro109/data.csv')
mathList = df['math score'].tolist()
# print(mathList)

meanmath = statistics.mean(mathList)
# meanmath = sum(mathList)/len(mathList)
stdDevmath = statistics.stdev(mathList)
medianmath = statistics.median(mathList)
# modemath = statistics.mode(mathList)
modemath = meanmath

# math
firtstStdStartH, firtstStdEndH = meanmath - \
    stdDevmath, meanmath+stdDevmath
secondStdStartH, secondStdEndH = meanmath - \
    (2*stdDevmath), meanmath+(2*stdDevmath)
thirdStdStartH, thirdStdEndH = meanmath - \
    (3*stdDevmath), meanmath+(3*stdDevmath)
fourthStdStartH, fourthStdEndH = meanmath - \
    (4*stdDevmath), meanmath+(4*stdDevmath)

mathListWithinFirtstStdH = [
    result for result in mathList if result > firtstStdStartH and result < firtstStdEndH]

mathListWithinSecondStdH = [
    result for result in mathList if result > secondStdStartH and result < secondStdEndH]

mathListWithinThirdStdH = [
    result for result in mathList if result > thirdStdStartH and result < thirdStdEndH]

mathListWithinFourthStdH = [
    result for result in mathList if result > fourthStdStartH and result < fourthStdEndH]


print('{}% (percentage) of data lies between the first standard deviation'.format(
    (len(mathListWithinFirtstStdH)*100)/(len(mathList))))

print('{}% (percentage) of data lies between the second standard deviation'.format(
    (len(mathListWithinSecondStdH)*100)/(len(mathList))))

print('{}% (percentage) of data lies between the third standard deviation'.format(
    (len(mathListWithinThirdStdH)*100)/(len(mathList))))

print('{}% (percentage) of data lies between the fourth standard deviation'.format(
    (len(mathListWithinFourthStdH)*100)/(len(mathList))))


print("Mean,Mode,Median,StdDev of math is -> {},{},{},{} respectively".format(
    meanmath, modemath, medianmath,  stdDevmath))
