# Harnessing the Data Revolution - Machine Learning Challenge (Theme: Anomaly Detection)
This is a repository for the Anomaly Detection challenge for the NSF HDR Institute for Harnessing Data and Model Revolution in the Polar Regions (iHARP).

# Problem
The iHARP anomaly prediction and detection challenge aims to predict anomalous sea-level observations from daily tide gauge data along the US East Coast affected by changes in the sea-level elevation values on the Atlantic Ocean. Anomalies in sea-level data can be caused by various weather and climate variability events, such as storm surges caused by hurricanes, mid-latitude storms, and tsunamis, or long-timescale weather and climate variability such as El Niño Southern Oscillation (ENSO). The ability to predict sea-level rise and detect anomalies has significant implications for coastal communities, aiding in the preparation for and mitigation of flood risks. Moreover, this challenge encourages the development of innovative approaches and solutions that can enhance our understanding of coastal processes and improve the accuracy of sea-level forecasts.

# Data Description


# Training Data
This challenge leverages a comprehensive training dataset spanning 20 years.

1. CSV Format as 'Training_Anomalies_Station_Data' -> This data represents buoy hourly sea-level measurements from 12 tide gauge stations along the US East Coast from 1993 to 2013 (for 20 years). Each station's data is a separate time series, labeled with known anomalies.
2. NetCDF Format as 'Copernicus_ENA_Satelite_Maps_Training_Data' -> For additional reference, NetDCF files are provided containing the sea-level elevation values on the Atlantic Ocean for the same period of 1993 to 2013 (for 20 years) for the 12 coastal stations. Note: The satellite data gives an image of the sea level over the whole ocean basin, but does not give us an accurate measure of the sea level at the coast, as the satellite cannot measure the sea level close to land.


# Test Data
Model submissions are evaluated on a test set of 10 years from 2014 to 2023 for the same coastal stations.
The dataset is available here.




