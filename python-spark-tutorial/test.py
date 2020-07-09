from pyspark import SparkContext, SparkConf


def kv(lst):
    result = []
    for val in lst:
        result.append((val, 1))
    return rdd


if __name__ == "__main__":
    conf = SparkConf().setAppName("create").setMaster("local")
    sc = SparkContext(conf=conf)

    inputStrings = [["a", "b", "c"], ["d", "e"]]
    regularRDDs = sc.parallelize(inputStrings)

    # pairRDD = regularRDDs.map(lambda s: len(s))
    pairRDD = regularRDDs.map(kv)
    result = pairRDD.reduce(lambda x, y: (x,sum(y)))
    # pairRDD.coalesce(1).saveAsTextFile("out/test")
    result.coalesce(1).saveAsTextFile("out/test")
