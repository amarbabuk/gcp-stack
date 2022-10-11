from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.rounds"

#id,event_id,name,order,kind,standings_grouping,official_results,created_at,updated_at
#330,44,Finals,6,0,1,0,2021-09-11 22:35:21,2021-09-11 22:35:21

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("event_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("order", "STRING"),
        bigquery.SchemaField("kind", "STRING"),
        bigquery.SchemaField("standings_grouping", "STRING"),
        bigquery.SchemaField("official_results", "STRING"),
       
        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/rounds.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))