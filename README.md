# cloud-resume-api

AWS services that enhances my resume, built for the [cloud resume challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/)

## Setup

1. Install the [aws sam cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html#install-sam-cli-instructions) 

1. Install [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#unixmacos), then `pyenv install 3.10`

1. Build
```bash
sam build
```

1. Test
```bash
python -m venv venv
. ./venv/bin/activate
cd tests
pytest
```

1. Deploy
```bash
sam deploy
```
