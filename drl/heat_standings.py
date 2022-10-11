from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.heat_standings"

#id,heat_id,event_pilot_id,rank,points,minimum_time,iris_dnf,time_type,finish_truck_ts,created_at,updated_at
#36072,881,357,6,0,DNF,0,,,2019-08-23 05:01:16,2019-08-23 05:01:16

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("heat_id", "STRING"),
        bigquery.SchemaField("event_pilot_id", "STRING"),
        bigquery.SchemaField("rank", "STRING"),
        bigquery.SchemaField("points", "STRING"),
        bigquery.SchemaField("minimum_time", "STRING"),
        bigquery.SchemaField("iris_dnf", "STRING"),
        bigquery.SchemaField("time_type", "STRING"),
        bigquery.SchemaField("finish_truck_ts", "STRING"),

        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/heat_standings.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))