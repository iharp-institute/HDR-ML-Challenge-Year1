# Harnessing the Data Revolution - Machine Learning Challenge (Theme: Anomaly Detection)
This is a repository for the Anomaly Detection challenge for the NSF HDR Institute for Harnessing Data and Model Revolution in the Polar Regions (iHARP).

# Motivation
Sea level observations from the National Data Buoy Center (NDBC) buoys along the US East Coast are essential for monitoring activities and have significant societal impacts. These buoys, equipped with advanced instruments, provide continuous real-time data on tidal variations, storm surges, and long-term sea level trends. This data is transmitted via satellite to shore-based stations, offering detailed records crucial for predicting and monitoring coastal flooding, a major threat to coastal communities.
Understanding storm surges and long-term sea level rise helps in issuing timely warnings, preparing for severe weather events, and implementing coastal protection measures to combat erosion.

# Problem Setting
The iHARP anomaly prediction and detection challenge aims to predict anomalous sea-level observations from daily tide gauge data along the U.S. East Coast affected by changes in the sea-level elevation values on the Atlantic Ocean. Anomalies in sea-level data can be caused by various weather and climate variability events, such as storm surges caused by hurricanes, mid-latitude storms, and tsunamis, or long-timescale weather and climate variability such as El Niño Southern Oscillation (ENSO). The ability to predict sea-level rise and detect anomalies has significant implications for coastal communities, aiding in the preparation for and mitigation of flood risks. Moreover, this challenge encourages the development of innovative approaches and solutions that can enhance our understanding of coastal processes and improve the accuracy of sea-level forecasts.

# Challenge Goal
1. Predict anomalous sea-level observations from daily tide gauge data along the U.S. East Coast affected by changes in the sea-level elevation values on the Atlantic Ocean.
2. Utilize machine learning techniques to predict dates of sea-level anomalies at various stations on the U.S. East Coast. 

# Data Description
The iHARP challenge dataset consists of the buoy hourly sea-level measurements from 12 tide gauge stations along the U.S. East Coast from 1993 to 2013 (20 years).

   # Training Data
   1. *CSV Format as 'Training_Anomalies_Station_Data'*
   
      Here, each station's data is a separate time series, labeled with known anomalies. 

      --> Refer to the *input_data* folder in this repository.

   2. *NetCDF Format as 'Copernicus_ENA_Satelite_Maps_Training_Data'*

      For additional reference, NetDCF files are provided containing the sea-level elevation values on the Atlantic Ocean          for the same period. Note: The satellite data provides an image of sea level over the entire ocean basin but does not        give an accurate measure of sea level along the coast, as the satellite cannot measure it near land.

      --> To understand the structure of each file, refer to the *metadata* in this repository for a sample of metadata for            Date 01/01/1993.

      --> Due to the size of the data, refer to the *public_data* in this repository for a sample of the data for January in           the year 1993.  

   # Test Data
   Submitted models are evaluated on a held-out test set spanning 10 years, from 2014 to 2023, for the same coastal stations.

# Model Submission
   # A. Example Model
   --> For a *demo model*, refer to the *baseline_model* in this repository.

   --> For a sample model structure, which will be ingested in the challenge platform, refer to 'codabench_files' in this          repository. Other programs to facilitate the ingestion and scoring of submitted models on Codabench are also                 available.
   
   # B. Expected Output
   A single .csv file where each row should represent a single day/date. The columns should show station locations where       the anomalies are being detected. Binary values (0 for false, 1 for true) to predict the presence of an anomaly in each      of the stations. 

  --> Refer to the reference_data folder to understand the structure of each file. See submission sample - *'demo_sla.csv'*.

   # C. Evaluation Metrics
   The performance of the anomaly detection models will be evaluated using the following metrics: 

   1. Precision = True Positives / (True Positives + False Positives)
   2. Recall = True Positives / (True Positives + False Negatives)
   3. F1 Score = 2 * (Precision * Recall) / (Precision + Recall)


# License
This project is licensed under the MIT License.

