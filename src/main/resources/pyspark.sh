 sample = [  (i, range(i)) for i in range(10) ]
 sampleRdd = sc.parallelize(sample)
 print sampleRdd.count()
 print sampleRdd.keys().count()
 print sampleRdd.values().count()
 valuesRdd=sampleRdd.flatMap(lambda (a,b): b)
 print valuesRdd.count()