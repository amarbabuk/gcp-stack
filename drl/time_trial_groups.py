from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "causal-guide-108309.foo_drl.time_trial_groups"

#id,round_id,order,start_truck_ts,racestack_active,racestack_scoring,racestack_lap,racestack_gate,created_at,updated_at
#189,256,2,,0,0,1,0,2021-09-11 22:36:05,2021-09-11 22:36:05

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("round_id", "STRING"),
        bigquery.SchemaField("order", "STRING"),
        bigquery.SchemaField("start_truck_ts", "STRING"),
        bigquery.SchemaField("racestack_active", "STRING"),
        bigquery.SchemaField("racestack_scoring", "STRING"),
        bigquery.SchemaField("racestack_lap", "STRING"),
        bigquery.SchemaField("racestack_gate", "STRING"),
                       
        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/time_trial_groups.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))