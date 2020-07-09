from pyspark import SparkContext, SparkConf
from operator import add


def kv(lst):
    result = []
    for val in lst:
        result.append((val, 1))
    return result


if __name__ == "__main__":
    conf = SparkConf().setAppName("create").setMaster("local")
    sc = SparkContext(conf=conf)

    inputStrings = [["a", "a", "c"], ["d", "d"], ["d", "e"]]
    regularRDDs = sc.parallelize(inputStrings)

    rdd_new = regularRDDs.flatMap(lambda x: [(i, 1) for i in x]).reduceByKey(lambda x, y: x + y)

    rdd_new.coalesce(1).saveAsTextFile("out/test")

