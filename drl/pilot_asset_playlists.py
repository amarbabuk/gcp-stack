from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "causal-guide-108309.foo_drl.pilot_asset_playlists"

#id,pilot_asset_id,take_type,playlist_id,order,text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,created_at,updated_at
#5011,1,1,4,1,standing,score,&nbsp;,"",&nbsp;,"",d9ff00,GAB707,DRL_Podium_DefaultSponsor__DRL.jpg,Heat 1,Group 1,Golden Heat,5,2022-01-06 04:52:18,2022-01-06 04:52:18

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("pilot_asset_id", "STRING"),
        bigquery.SchemaField("take_type", "STRING"),
        bigquery.SchemaField("playlist_id", "STRING"),
        bigquery.SchemaField("order", "STRING"),
        bigquery.SchemaField("text1", "STRING"),
        bigquery.SchemaField("text2", "STRING"),
        bigquery.SchemaField("text3", "STRING"),
        bigquery.SchemaField("text4", "STRING"),
        bigquery.SchemaField("text5", "STRING"),
        bigquery.SchemaField("text6", "STRING"),
        bigquery.SchemaField("text7", "STRING"),
        bigquery.SchemaField("text8", "STRING"),
        bigquery.SchemaField("text9", "STRING"),
        bigquery.SchemaField("text10", "STRING"),
        bigquery.SchemaField("text11", "STRING"),
        bigquery.SchemaField("text12", "STRING"),
        bigquery.SchemaField("text13", "STRING"),

        bigquery.SchemaField("created_at", "STRING"),
        bigquery.SchemaField("updated_at", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/pilot_asset_playlists.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))