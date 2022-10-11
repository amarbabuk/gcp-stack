
https://www.cloudskillsboost.google/games/3139
Lab-1
https://www.cloudskillsboost.google/games/3139/labs/19212

gs://spls/gsp394/tables

gsutil ls gs://spls/gsp394/tables

gsutil cat  gs://spls/gsp394/tables/colors.csv


pip install --upgrade google-cloud-bigquery



from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
# table_id = "your-project.your_dataset.your_table_name"
table_id = "qwiklabs-gcp-02-7312262849d7.drl.colors"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("stripe_available", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("dark", "STRING"),
        bigquery.SchemaField("med", "STRING"),
        bigquery.SchemaField("light", "STRING"),
    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
# uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
uri = "gs://spls/gsp394/tables/colors.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))


gs://spls/gsp394/tables/colors.csv
gs://spls/gsp394/tables/event_crossings.csv
gs://spls/gsp394/tables/event_pilots.csv
gs://spls/gsp394/tables/event_standings.csv
gs://spls/gsp394/tables/events.csv
gs://spls/gsp394/tables/heat_pilot_crossings.csv
gs://spls/gsp394/tables/heat_pilots.csv
gs://spls/gsp394/tables/heat_standings.csv
gs://spls/gsp394/tables/heats.csv
gs://spls/gsp394/tables/pilot_asset_playlists.csv
gs://spls/gsp394/tables/pilot_assets.csv
gs://spls/gsp394/tables/pilot_season_stats.csv
gs://spls/gsp394/tables/pilots.csv
gs://spls/gsp394/tables/race_standings.csv
gs://spls/gsp394/tables/races.csv
gs://spls/gsp394/tables/round_standings.csv
gs://spls/gsp394/tables/rounds.csv
gs://spls/gsp394/tables/scorings.csv
gs://spls/gsp394/tables/seasons.csv
gs://spls/gsp394/tables/time_trial_group_pilot_crossings.csv
gs://spls/gsp394/tables/time_trial_group_pilot_times.csv
gs://spls/gsp394/tables/time_trial_group_pilots.csv
gs://spls/gsp394/tables/time_trial_groups.csv


Q1
Events in a Certain City
SELECT name FROM `qwiklabs-gcp-02-7312262849d7.drl.events` where city = 'Miami'

Q2
Event Pilot Names
select name, first_name, last_name, e.pilot_id, event_id from `qwiklabs-gcp-02-7312262849d7.drl.pilots` p, `qwiklabs-gcp-02-7312262849d7.drl.event_pilots` e where p.id = e.pilot_id

Q3
Pilots Who Flew in an Event
select p.name, v.name  from `qwiklabs-gcp-02-7312262849d7.drl.pilots` p, `qwiklabs-gcp-02-7312262849d7.drl.event_pilots` e, `qwiklabs-gcp-02-7312262849d7.drl.events` v 
where p.id = e.pilot_id
and v.id = e.event_id
and 
and parse_date('%Y-%m-%d', v.end_date) < current_date()

Q4
Average Time of Rank 1 Round Finish
SELECT time
 (timestamp_seconds
   (CAST
     (AVG
       (UNIX_SECONDS
         (PARSE_TIMESTAMP('%H:%M.%S', minimum_time))
       )
   AS INT64)
   )
 ) avg
 from `qwiklabs-gcp-02-7312262849d7.drl.round_standings`
 where rank = '1'

 Q5
 Clean and Combine Time Trial Data
 
 insert into `qwiklabs-gcp-02-7312262849d7.drl.time_trial_cleaned`(time_trial_group_pilot_times_id,time_trial_group_pilot_id,time_trial_group_id,round_id,time) values (
select t.id time_trial_group_pilot_times_id, p.id time_trial_group_pilot_id, g.id time_trial_group_id, g.round_id round_id, 'time' time
from `qwiklabs-gcp-02-7312262849d7.drl.time_trial_group_pilot_times` t, `qwiklabs-gcp-02-7312262849d7.drl.time_trial_group_pilots` p, `qwiklabs-gcp-02-7312262849d7.drl.time_trial_groups` g
where t.time_trial_group_pilot_id = p.id
and g.id = p.time_trial_group_id
)


Lab-2
 https://www.cloudskillsboost.google/games/3139/labs/19213

 gsutil cp gs://spls/gsp396/DRL2.ipynb .

!gsutil ls gs://{BUCKET}/model
gs://qwiklabs-gcp-01-38db58a6af4e/model/
gs://qwiklabs-gcp-01-38db58a6af4e/model/keras_metadata.pb
gs://qwiklabs-gcp-01-38db58a6af4e/model/saved_model.pb
gs://qwiklabs-gcp-01-38db58a6af4e/model/assets/
gs://qwiklabs-gcp-01-38db58a6af4e/model/variables/


 !gcloud ai models upload \
  --region=us-east1 \
  --display-name=drl-pilot-ranking \
  --container-image-uri=us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-8:latest \
  --artifact-uri=gs://{BUCKET}/model


https://github.com/googleapis/python-aiplatform/blob/main/samples/snippets/prediction_service/predict_custom_trained_model_sample.py

predict_custom_trained_model_sample(
    project="828836705604",
    endpoint_id="4690657341580771328",
    location="us-east1",
    instance_dict={"pilot_id": "11", "ename": "Practice", "events_name": "Project Manhattan", "minimum_time": "80.0"}
)
