from feast import FeatureStore, FeatureView, Feature, ValueType, FileSource, Entity

from feast.data_format import ParquetFormat
from datetime import timedelta, datetime
import pandas as pd

store = FeatureStore(repo_path="https://ferndemo.azurewebsites.net")

print(store.list_feature_views())

# df = pd.read_csv("C:\\Users\\xiwu\\Downloads\\driver.csv")
# df["datetime"] = pd.to_datetime(df["datetime"])
# df.to_parquet("C:\\Users\\xiwu\\Downloads\\driver.parquet")

parquet_file_source = FileSource(
    file_format=ParquetFormat(),
    path=".\\tests\\fern\\driver.parquet",
    event_timestamp_column="datetime"
)

entity = Entity(name='drivers', value_type=ValueType.STRING, join_key='drivers')

driver_stats_fv = FeatureView(
    name="driver_activity",
    entities=["drivers"],
    features=[
        Feature(name="completed", dtype=ValueType.INT64),
        Feature(name="avg_distance_completed", dtype=ValueType.FLOAT),
    ],
    batch_source=parquet_file_source,
    ttl=timedelta(seconds=60)
)

store.apply([entity, driver_stats_fv])

entity_df = pd.DataFrame.from_dict(
    {
        "drivers": [1, 2, 3, 4],
        "event_timestamp": [
            datetime(2020, 1, 1),
            datetime(2020, 1, 1),
            datetime(2020, 1, 1),
            datetime(2020, 1, 1),
        ],
    }
)

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "driver_activity:completed",
        "driver_activity:avg_distance_completed",
    ],
).to_df()

print(training_df.head())