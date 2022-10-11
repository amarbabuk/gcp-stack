from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "causal-guide-108309.foo_drl.time_trial_group_pilot_times"

#id,time_trial_group_pilot_id,lap_number,time,racestack_time,time_adjusted,penalty_time,finish_truck_ts,created_at,updated_at
#964,307,1,99800,,,,2018-03-04 19:46:39,2018-03-04 19:46:39,2018-03-04 19:54:49

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("time_trial_group_pilot_id", "STRING"),
        bigquery.SchemaField("lap_number", "STRING"),
        bigquery.SchemaField("time", "STRING"),
        bigquery.SchemaField("racestack_time", "STRING"),
        bigquery.SchemaField("time_adjusted", "STRING"),
        bigquery.SchemaField("penalty_time", "STRING"),
        bigquery.SchemaField("finish_truck_ts", "STRING"),
               
        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/time_trial_group_pilot_times.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))