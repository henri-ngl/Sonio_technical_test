CREATE TABLE IF NOT EXISTS dicom_data(
    filename VARCHAR(10),
    columns INT,
    rows INT,
    manufacturerModelName VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS images_data(
    id INTEGER,
    filename VARCHAR(50),
    file_upload VARCHAR(255),
    drafts JSONB,
    predictions JSONB,
    data JSONB,
    meta JSONB,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    inner_id INTEGER,
    total_annotations INTEGER,
    cancelled_annotations INTEGER,
    total_predictions INTEGER,
    comment_count INTEGER,
    unresolved_comment_count INTEGER,
    last_comment_updated_at TIMESTAMP,
    project INTEGER,
    updated_by INTEGER,
    comment_authors JSONB
);

CREATE TABLE IF NOT EXISTS annotations_data(
    id INTEGER,
    image_id VARCHAR(50),
    completed_by INTEGER,
    was_cancelled BOOLEAN,
    ground_truth BOOLEAN,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    lead_time FLOAT,
    prediction JSONB,
    result_count INTEGER,
    task INTEGER,
    project INTEGER,
    parent_prediction JSONB,
    parent_annotation JSONB
);

CREATE TABLE IF NOT EXISTS results_data(
    id VARCHAR(50),
    annotation_id VARCHAR(50),
    type VARCHAR(50),
    value VARCHAR(50),
    view VARCHAR(50),
    origin VARCHAR(50),
    to_name VARCHAR(50),
    from_name VARCHAR(50)
);