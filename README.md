# DB ARCHITECTURE

![architechture DB.png](architechture%20DB.png)

This exercise focuses on creating a DICOM file processing pipeline.
DICOM is a format used to store and exchange medical images and related patient information, facilitating interoperability 
and ensuring compatibility between different imaging devices and healthcare systems. 

To read these files, you can use [PyDicom](https://pydicom.github.io/pydicom/stable/old/getting_started.html#introduction).

In addition to the DICOM files, we have corresponding annotations stored in a JSON file. 
These annotations describe the specific part of the fetus being examined (referred to as the view). 

For this exercise, you are required to:

1. Create a PostgreSQL database to store the output data from the pipeline. You should have at least two tables: one for DICOM data and another for annotation data. 
   Design the database architecture that best fits the problem according to your judgment. You can utilize Docker to host your own database.

2. Develop a Python script that extracts the following minimal information from:
   - DICOM files: `Columns`, `Rows`, and `ManufacturerModelName` fields, at a minimum.
   - Annotations file: The names of the views associated with each image (e.g., Heart, ...).
   - You are also encouraged to include any other relevant data that you think is necessary.

3. Insert the extracted data into the PostgreSQL database.

You're expected to deliver the necessary files to enable the pipeline to run on any other computer that already has Python and Docker installed. 
Therefore, there's no need for you to send us a DB dump.

Tips:
  - Note that the DICOM file names may not perfectly match those in the annotations. However, you should still be able to accurately match them.
  - [Psycopg](https://www.psycopg.org/) is the standard Python package for interacting with

