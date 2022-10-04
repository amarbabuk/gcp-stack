from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "causal-guide-108309.foo_drl.race_standings"

#id,race_id,event_pilot_id,rank,points,advances,finish_positions,wins,minimum_time,time_type,created_at,updated_at
#578,33,17,6,7,,,0,DNF,,2017-03-24 16:58:45,2017-03-24 16:58:45

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("race_id", "STRING"),
        bigquery.SchemaField("event_pilot_id", "STRING"),
        bigquery.SchemaField("rank", "STRING"),
        bigquery.SchemaField("points", "STRING"),
        bigquery.SchemaField("advances", "STRING"),
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
uri = "gs://spls/gsp394/tables/race_standings.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))