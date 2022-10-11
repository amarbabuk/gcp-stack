from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.round_standings"

#id,round_id,event_pilot_id,rank,points,finish_positions,wins,minimum_time,time_type,created_at,updated_at
#3584,271,513,1,,,,0:40.5,,2021-08-23 21:02:46,2021-08-23 21:02:46

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("round_id", "STRING"),
        bigquery.SchemaField("event_pilot_id", "STRING"),
        bigquery.SchemaField("rank", "STRING"),
        bigquery.SchemaField("points", "STRING"),
        bigquery.SchemaField("finish_positions", "STRING"),
        bigquery.SchemaField("wins", "STRING"),
        bigquery.SchemaField("minimum_time", "STRING"),
        bigquery.SchemaField("time_type", "STRING"),
       
        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/round_standings.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))