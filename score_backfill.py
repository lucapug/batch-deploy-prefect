from datetime import datetime
from dateutil.relativedelta import relativedelta

from prefect import flow

from score import ride_duration_prediction


@flow
def ride_duration_prediction_backfill():
    start_date = datetime(year=2021, month=4, day=1)
    end_date = datetime(year=2022, month=5, day=1)

    d = start_date

    while d <= end_date:
        ride_duration_prediction(
            taxi_type='green',
            run_id='d038fcff0d5742c58177cf499a456b25',
            run_date=d
        )

        d = d + relativedelta(months=1)


if __name__ == '__main__':
    ride_duration_prediction_backfill()