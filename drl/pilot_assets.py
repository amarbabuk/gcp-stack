from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "causal-guide-108309.foo_drl.pilot_assets"

#id,pilot_id,filename,label,asset_type,primary,created_at,updated_at
#39,72,FoxurFPV_Home4.mp4,FoxurFPV,0,0,2019-03-04 03:50:44,2019-03-07 02:54:05

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("pilot_id", "STRING"),
        bigquery.SchemaField("filename", "STRING"),
        bigquery.SchemaField("label", "STRING"),
        bigquery.SchemaField("asset_type", "STRING"),
        bigquery.SchemaField("primary", "STRING"),

        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/pilot_assets.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))