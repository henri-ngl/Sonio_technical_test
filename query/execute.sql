CREATE TABLE IF NOT EXISTS public.final_table AS (
    SELECT
        pid.filename,
        pdd.columns,
        pdd.rows,
        pdd.manufacturerModelName,
        prd.view
    FROM
        public.images_data pid
    LEFT JOIN
        public.dicom_data pdd
        USING(filename)
    LEFT JOIN
        public.annotations_data	pad
        ON pid.id = pad.image_id::integer
    LEFT JOIN
        public.results_data	prd
        ON pad.id = prd.annotation_id::integer
)