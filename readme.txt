http://stanford.edu/~rezab/sparkclass/
http://stanford.edu/~rezab/sparkclass/slides/itas_workshop.pdf

http://bit.ly/spark-training-2
unzip to C:\Mohan\apps\spark_course\

Example-1
---------
val sc = new SparkContext()
val lines = sc.textFile("logfile.txt")
val errors = lines.filter(_.startsWith("ERROR"))
val messages = errors.map(_.split("\t")(2))
messages.saveAsTextFile("errors.txt") //Kicks of the computation

Example-2 (Machine learning MLib)
---------------------------------
points = sc.sql("select latitude, longitude from tweets")
model = KMeans.train(points, 10)

Example-3 (Spark SQL)
---------------------------------
val teenagers = sc.sql("SELECT name FROM people WHERE age >=13 AND age <=19")
val names = teenagers.map(t =>  "Name: " + t(0)).collect()

Example-4 (Hive - Python)
---------------------------------
hc = HiveContext(sc)
rows = hc.sql("SELECT text, year FROM hivetable")
rows.filter(lambda r: r.year > 2013).collect()

Example-5 (SQL on Json)
---------------------------------
sc.jsonFile("jsonTweets.txt").registerAsTable("tweets")
sc.sql("SELECT text, user.name FROM tweets")
 


Notes
-------
Spark - Extends programming language with distributed collection data-structure named RDD.
RDD -	Resilient distributed datasets
	-	User controlled partitioning, and storage
	-	Automatically rebuild on failure.
	-	Knows their paritioning function. (Hash partitioning)
	-	

Lazy - Lazily evaluated