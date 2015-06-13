dir(sc)		=> Gives list of function & attribute available.
help(sc)	=> Gives detailed documentation of function & attribute available with samples. Similar to Javadoc API.
help(sc.parallelize)	=> Help on method parallelize in module pyspark.context:

Sample function in python
-------------------------
def sub(value):
    """"
    	Multiline help text
    """
    return (value - 1)
-------------------------


We'll see that sc.parallelize() generates a pyspark.rdd.PipelinedRDD when its input is an xrange. 
And a pyspark.RDD when its input is a range.

Debug
*	print xrangeRDD.toDebugString()
*	print xrangeRDD.getNumPartitions()
*	Prefer (for debugging) RDD.transformation1(), RDD.action1() and RDD.transformation2() and RDD.action2()
*	Use following function to peek into RDD => first(), take(), top(), takeOrdered(), and reduce()
* 	take(1) and first() returns same result. Since partitioned, No guranteed order.
*	Key advantage of using takeOrdered() instead of first() or take() is that takeOrdered() returns a deterministic result.
*	takeOrdered() returns the list sorted in ascending order. 
*	The top() action is similar to takeOrdered() except that it returns the list in descending order.
* 	reduce(function), The function should be commutative and associative, as reduce() is applied at the partition level and then again to aggregate results from partitions.
* 	(sc
 .parallelize(data)
 .map(lambda y: y - 1)
 .filter(lambda x: x < 10)
 .collect())
*	Write a quick TestCase.
	from test_helper import Test
	Test.assertEquals(makePlural('rat'), 'rats', 'incorrect result: makePlural does not add an s') 
 


map(f), the most common Spark transformation, is one such example: 
it applies a function f to each item in the dataset, and outputs the resulting dataset. 
When you run map() on a dataset, a single stage of tasks is launched. 
A stage is a group of tasks that all perform the same computation, but on different input data. 
One task is launched for each partitition, as shown in the example below. A task is a unit of execution that runs on a single machine. 
When we run map(f) within a partition, a new task applies f to all of the entries in a particular partition, and outputs a new partition. 
In this example figure, the dataset is broken into four partitions, so four map() tasks are launched.

PySpark Setup
--------------
http://www.kuntalganguly.com/2015_06_01_archive.html
http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/
http://pgbovine.net/ipython-notebook-first-impressions.htm

 
 
sudo apt-get install python-pip ipython ipython-notebook
sudo pip install --upgrade ipython tornado

re.sub(r"['_,!\-\"\\\/}{?\.]",'',text)