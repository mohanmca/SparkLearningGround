organization := "Nikias"
name := "SparkLearningGround"
scalaVersion := "2.11.6"

libraryDependencies ++= Seq(
  "ch.qos.logback" % "logback-classic" % "1.0.0" % "runtime" withSources(),
  "org.scalatest" % "scalatest_2.11" % "2.2.4" % "test"  withSources(),
  "org.scalacheck" % "scalacheck_2.11" % "1.12.2"  withSources(),
  "junit"% "junit" % "4.12"  withSources()
)
 
 


