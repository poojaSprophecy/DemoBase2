from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pip2.config.ConfigStore import *
from pip2.udfs.UDFs import *
from prophecy.utils import *
from pip2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pip2")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pip2", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pip2")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
