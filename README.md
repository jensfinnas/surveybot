# Surveybot

Generate a survey bot.

`python example.py`

## Install

You must have [virtualenv](https://virtualenv.pypa.io/en/stable/) installed locally then you can install the robot with
the following command:

```
make install
```

Or build it inside a Docker container (without any other dependencies):

```
docker build -t chartbot .
```

## Run

You **have to set up** the following environment variables from the [Twitter console](https://apps.twitter.com/):

| Variable | Description |
| --- | --- |
| `CONSUMER_KEY` | Twitter Consumer Key (API Key) |
| `CONSUMER_SECRET` | Twitter Consumer Secret (API Secret) |
| `ACCESS_TOKEN` | Twitter Access Token |
| `ACCESS_TOKEN_SECRET` | Twitter Access Token Secret |

Then run:

```
python example.py
```
