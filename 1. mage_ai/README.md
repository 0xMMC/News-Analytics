<div>
<img src="https://github.com/mage-ai/assets/blob/main/mascots/mascots-shorter.jpeg?raw=true">
</div>

## Getting started

This folder contains a Docker Compose template for setting up Mage as a data orchestration platform. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 

Rename `dev.env` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.

Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started. 

### What just happened?

We just initialized a new mage repository. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to.

This repository should have the following structure:

```
.
├── mage_data
│   └── magic-zoomcamp
├── magic-zoomcamp
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
```

## Additional support is available at the following links:

1. [Mage Docs](https://docs.mage.ai/introduction/overview)
2. [Mage Slack](https://www.mage.ai/chat)
3. [Mage GitHub](https://github.com/mage-ai/mage-ai)