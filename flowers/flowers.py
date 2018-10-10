#Austin P

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


#Load dataset straight from UCI repo
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

peakData = False

if peakData:
	#shape of the dataset
	print(dataset.shape)#150x5

	#peak a bit
	print(dataset.head(20))

	# class distribution
	print(dataset.groupby('class').size())#50 of each

#data visualization ===============

#1var

showPlots = False

if showPlots:
	# box and whisker plots
	dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
	plt.show()

	#histograms
	dataset.hist()
	plt.show()


#multivar

showMatrix = False

if showMatrix:
	# scatter plot matrix
	scatter_matrix(dataset)
	plt.show()
	#diagonal grouping of some pairs
	# = predictable relationship






















