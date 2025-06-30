# POC - Wearable Health Data

This is a proof of concept for acquiring health data from wearable devices, intended for telemetric health analysis.


## Setup to Run Demo Locally

To try this demo, follow the steps below:

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

```bash
source venv/bin/activate
``` 
For Windows, use `venv\Scripts\activate` instead of `source venv/bin/activate`.

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the jupyter lab:

```bash
jupyter lab
```

### Envionment Variables

Before running the demo an .env file must be provided based on the `.env-template` file.
Copy `.env-template` as `.env` and add the environment variables values. 

In a *nix environment:

```bash
cp .env-template .env
```

```txt
# These values can be found in Sahha's dashboard.
# Create a file named `.env` and paste the environment variables with their respective values.
```

## About the demo extracted data

There's a notebook named `export_data.ipynb`, this is an example for calling the api and extracting the data as csv into the `data` directory.
The csv file is named as `health_data_{start_date_extraction}_to_{end_date_extraction}`. For example, `health_data_2025-04-24_to_2025-05-08.csv`.

Here is a quick description of the demo dataset:

| **field name**       | **description**                        | **example value**         |
|----------------------|----------------------------------------|---------------------------|
| date                 | the day of the record                  | 1984-01-30                |
| active_duration      | time of activity in the day in minutes | 76                        |
| gender               | the subject`s gender                   | female                    |
| os                   | device's operational system            | android                   |
| patient              | subject unique identifier              | oqJAHdkajkadAH            |
| timezone             | the gmt timezone                       | -03:00                    |
| steps                | number of steps                        | 1387                      |
| sleep_duration       | total sleep duration in minutes        | 478                       |
| heart_rate_sleep     | average heart rate during sleep        | 53.447                    |
| sleep_deep_duration  | deep sleep phase duration in minutes   | 35                        |
| sleep_light_duration | light sleep phase duration in minutes  | 193                       |
| sleep_rem_duration   | rem sleep phase duration in minutes    | 78                        |
| sleep_start_time     | sleep start datetime                   | 2019-11-22T00:51:30-03:00 |
| sleep_end_time       | sleep finish datetime                  | 2019-11-23T06:22:28-03:00 |



