from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.heat_pilots"

#id,event_pilot_id,heat_id,channel,time,racestack_time,time_adjusted,penalty_time,dnf_order,iris_dnf,racestack_dnf_order,racestack_dnf_time,racestack_dnf_reason,checkpoints,checkpoints_adjusted,extra_points,finish_truck_ts,advances,eliminated,created_at,updated_at
#1980,149,319,,,,,,1,0,,,,,,,2017-03-04 00:23:55,0,0,2017-03-03 23:02:00,2017-05-26 18:04:50

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("event_pilot_id", "STRING"),
        bigquery.SchemaField("heat_id", "STRING"),
        bigquery.SchemaField("channel", "STRING"),
        bigquery.SchemaField("time", "STRING"),
        bigquery.SchemaField("racestack_time", "STRING"),
        bigquery.SchemaField("time_adjusted", "STRING"),
        bigquery.SchemaField("penalty_time", "STRING"),
        bigquery.SchemaField("dnf_order", "STRING"),
        bigquery.SchemaField("iris_dnf", "STRING"),
        bigquery.SchemaField("racestack_dnf_order", "STRING"),
        bigquery.SchemaField("racestack_dnf_time", "STRING"),
        bigquery.SchemaField("racestack_dnf_reason", "STRING"),
        bigquery.SchemaField("checkpoints", "STRING"),
        bigquery.SchemaField("checkpoints_adjusted", "STRING"),
        bigquery.SchemaField("extra_points", "STRING"),
        bigquery.SchemaField("finish_truck_ts", "STRING"),
        bigquery.SchemaField("advances", "STRING"),
        bigquery.SchemaField("eliminated", "STRING"),

        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/heat_pilots.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))