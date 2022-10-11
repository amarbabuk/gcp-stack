from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.heats"

#id,race_id,racestack_uuid,order,restarts,show_standings,production_notes,start_truck_ts,racestack_active,racestack_scoring,racestack_start_ts,racestack_finish_ts,created_at,updated_at
#1016,271,972c2e85-9149-450d-96ef-d53a2d203de9,1,0,1,,,0,0,1620046562628,1620046591634,2021-05-03 12:52:01,2021-05-03 12:57:04

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("race_id", "STRING"),
        bigquery.SchemaField("racestack_uuid", "STRING"),
        bigquery.SchemaField("order", "STRING"),
        bigquery.SchemaField("restarts", "STRING"),
        bigquery.SchemaField("show_standings", "STRING"),
        bigquery.SchemaField("production_notes", "STRING"),
        bigquery.SchemaField("start_truck_ts", "STRING"),
        bigquery.SchemaField("racestack_active", "STRING"),
        bigquery.SchemaField("racestack_scoring", "STRING"),
        bigquery.SchemaField("racestack_start_ts", "STRING"),
        bigquery.SchemaField("racestack_finish_ts", "STRING"),

        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/heats.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))