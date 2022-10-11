from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "causal-guide-108309.foo_drl.pilot_season_stats"

#id,season_id,pilot_id,avg_event_place,avg_heat_place,heat_wins,dnfs,finish_percent,created_at,updated_at
#4,6,13,7.5,3.38,3,18,60,2019-08-16 19:50:35,2019-09-10 07:12:02

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("season_id", "STRING"),
        bigquery.SchemaField("pilot_id", "STRING"),
        bigquery.SchemaField("avg_event_place", "STRING"),
        bigquery.SchemaField("avg_heat_place", "STRING"),
        bigquery.SchemaField("heat_wins", "STRING"),
        bigquery.SchemaField("dnfs", "STRING"),
        bigquery.SchemaField("finish_percent", "STRING"),

        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/pilot_season_stats.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))