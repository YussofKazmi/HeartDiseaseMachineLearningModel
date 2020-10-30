import sys
from pyspark.sql.types import DoubleType
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext, SparkConf
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.linalg import Vectors



def parsePoint(line):
    values = [float(0) if x =='?' else float(x) for x in line.split(',')]
    return LabeledPoint(values[13], values[0:13])

sc = SparkContext("local", "PySpark Random Forest Machine Learning Predictor")
data = sc.textFile("input.txt")


parseddata = data.map(parsePoint)

model = RandomForest.trainClassifier(parseddata, numClasses = 2, categoricalFeaturesInfo={}, numTrees = 5, impurity='gini', maxDepth=5, maxBins=32)
testData = ([65,1,4,130,275,0,1,115,1,1,2,0,0]

)
prediction = model.predict(testData)
result = open("OUTPUT", "w")
result.write("Prediction: " + str(prediction) + '\n')
result.close()
