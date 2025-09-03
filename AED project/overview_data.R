
library(arrow)



interventions_bxl = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/interventions_bxl.parquet.gzip")
interventions_bxl2 = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/interventions_bxl2.parquet.gzip")
interventions1 = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/interventions1.parquet.gzip")
interventions2 = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/interventions2.parquet.gzip")
interventions3 = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/interventions3.parquet.gzip")
cad9 = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/cad9.parquet.gzip")
aed_locations = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/aed_locations.parquet.gzip")
ambulance_locations = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/ambulance_locations.parquet.gzip")
mug_locations = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/mug_locations.parquet.gzip")
pit_locations = read_parquet("C:/Users/eloua/Desktop/modern data analytics/group project/data/pit_locations.parquet.gzip")