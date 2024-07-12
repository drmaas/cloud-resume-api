# cloud-resume-api

AWS services that enhance my resume with a site counter, built for the [cloud resume challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/)

## Setup

1. Install the [aws sam cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html#install-sam-cli-instructions) 

1. Setup [virtual environment](https://docs.python.org/3/library/venv.html)
```bash
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

2. Build
```bash
sam build
```

1. Test
```bash
pytest
```

1. Deploy
```bash
sam deploy
```
