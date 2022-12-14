from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.seasons"

#id,scoring_id,name,start_date,end_date,stats_calculated_at,created_at,updated_at
#1,4,Season 1,2016-01-01,2016-12-31,,2016-07-05 22:00:15,2016-07-13 02:32:59

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("scoring_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("start_date", "STRING"),
        bigquery.SchemaField("end_date", "STRING"),
        bigquery.SchemaField("stats_calculated_at", "STRING"),
               
        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/seasons.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))