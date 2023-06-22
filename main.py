import os
from typing import Any
import pydicom
import json
import psycopg2
from psycopg2.extras import execute_values
from pathlib import Path

parent_directory = Path(__file__).parent
data_folder = f"{parent_directory}/data"
annotation_file = f"{data_folder}/annotation_data.json"
query_file = f"{parent_directory}/query/execute.sql"

# Postgres' connection details
db_host = 'localhost'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'postgres'


def convert_field_to_json(data: dict) -> dict:
    """
    This function convert to json all dict and list values
    :param data:
    :return data converted:
    """
    for k, v in data.items():
        if isinstance(v, dict) or isinstance(v, list):
            data[k] = json.dumps(v)
    return data


def get_dicom_data() -> list:
    """
    Get data from DICOM files
    """
    dicom_data = []
    for filename in os.listdir(data_folder):
        if filename.endswith('.dcm'):
            dataset = pydicom.dcmread(f"{data_folder}/{filename}")
            columns = dataset.Columns
            rows = dataset.Rows
            manufacturer_model_name = dataset.ManufacturerModelName

            dicom_info = {
                'filename': filename[:-4],
                'columns': columns,
                'rows': rows,
                'manufacturerModelName': manufacturer_model_name,
            }
            dicom_data.append(dicom_info)

    return dicom_data


def get_images_data() -> dict[str, Any]:
    """
    Get data from annotation files
    """
    images_data = []
    annotations_data = []
    results_data = []

    with open(annotation_file) as file:
        annotation_json_data = json.load(file)

    for image in annotation_json_data:
        for annotation in image.pop('annotations'):
            for result in annotation.pop('result'):
                result['annotation_id'] = annotation['id']
                result["view"] = "-".join(result["value"]["choices"])
                result["value"] = json.dumps(result["value"])
                results_data.append(convert_field_to_json(result))

            annotation['image_id'] = image['id']
            annotation["prediction"] = json.dumps(annotation["prediction"])
            annotations_data.append(convert_field_to_json(annotation))

        image['filename'] = image['file_upload'].split("-")[1][:-4]
        images_data.append(convert_field_to_json(image))

    data = {
        "images_data": images_data,
        "annotations_data": annotations_data,
        "results_data": results_data
    }

    return data


def insert_data_base_table():
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()

    table_dict = get_images_data()
    table_dict['dicom_data'] = get_dicom_data()

    for table_name, table_data in table_dict.items():
        column_names = table_data[0].keys()
        values = [[row[k] for k in column_names] for row in table_data]

        insert_query = "INSERT INTO {} ({}) VALUES %s;".format(table_name, ', '.join(column_names))

        execute_values(cursor, insert_query, values)

    conn.commit()
    cursor.close()
    conn.close()


def retrieve_final_table() -> None:
    """
    Compute all the base table to retrieve the final one
    """
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()

    with open(query_file, 'r') as file:
        query = file.read()

    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    insert_data_base_table()
    retrieve_final_table()

