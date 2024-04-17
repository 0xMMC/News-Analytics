# News-Analytics

## Description
News-Analytics is a project designed to fetch and analyse news articles on specific topics. By leveraging NewsAPI, it retrieves articles within a specified date range and applies various Natural Language Processing (NLP) techniques to extract sentiment scores, keywords, and named entities. The information is processed by a data pipeline developed with Mage.AI, dbt and PowerBI. Whether for academic research, market analysis, or personal interest, News-Analytics offers a comprehensive solution for understanding the context, impact and reach of news stories.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Installation
Before you begin, ensure you have Python 3.6+ and pip installed on your system.

1. **Terraform Setup**:
   - Install Terraform to manage cloud resources. Follow the installation guide here: [Terraform Installation](https://developer.hashicorp.com/terraform/install).
   - The project is hosted on Google Cloud Platform. However, users are free to use any cloud or on-prem platform by adapting the Mage.AI output nodes and the dbt connection.
   - A service account with appropriate privileges is required for resource creation. The service account private key needs to be copied in the "0. terraform" folder.
   - The service account key location, project name, storage bucket name, and region are set in `variables.tf`.
   - Run the following commands:
   - `terraform init`
   - `terraform plan`
   - `terraform apply`

2. **Mage Setup**:
   - You will need docker and docker-compose installed to set up Mage.AI.
   - Navigate to the "1. mage_ai" folder and run `docker-compose up`.
   - To open the Mage.AI interface, navigate to http://localhost:6789.
   - To connect to the Google Cloud platform (or alternative), you will need to create a new service account with Storage Admin and BigQuery Admin privileges and create a key. Copy the json key to the Mage folder, then edit the io_config.yaml file to point the GOOGLE_SERVICE_ACC_KEY_FILEPATH variable to the credentials file.
   - Register for a free or paid NewsAPI key.
   - Navigate to the "Edit Pipeline" panel, open each of the two pipelines, and add the API key as a secret in the Secrets tab.
   - Configure "news_topics_loop.py" and "news_topics_weekly.py" with your desired time intervals and topics. Please be mindful that the free API only allows a 30 day lookback, 100 API calls per day, and the top 100 news returned per call, sorted by popularity.
   - Ensure that both "news_topics_loop.py" and "news_topics_weekly.py" are set as Dynamic blocks, from the top right three-dot menu > 'Enable block as dynamic', and that 'process_news', 'process_news_sentiments', 'process_news_keywords' and 'process_news_entities' Transformer blocks have "Reduce output" enabled, as per the diagram below.
   - Finally, set your desired BigQuery (or alternative) table names and storage bucket names in the Data Exporter blocks, in the table_id and bucket_name variables.
   - You are free to either run the pipeline manually, set a one-off trigger, or set a recurring schedule.

Note: Project dependencies should be installed automatically when running Docker. If errors relating to Python packages are encountered, you can force install all dependencies by running `pip install -r requirements.txt` and `python -m spacy download en_core_web_sm` in the Mage.AI Terminal panel.

![Data Pipeline Structure](Data%20Pipeline.png?raw=true "Data Pipeline Structure")

3. **dbt Cloud Setup**
   - Sign up for dbt Cloud at [dbt Cloud](https://cloud.getdbt.com/). Choose a plan that suits your needs; there is a free tier available for small projects and trials.
   - Once logged in, create a new project in dbt Cloud by clicking on the "New Project" button and following the prompts. When asked, connect your version control system (e.g., GitHub) and select the repository where you forked or cloned the News-Analytics project.
   - In the dbt Cloud interface, navigate to your project settings to configure your development environment. This involves setting up your database connection to BigQuery (or alternative) by uploading a service account keys file.
   - Navigate to the "2. dbt" folder in your repository. You should see the dbt models defined. Ensure the models are in a directory that dbt Cloud can access, or otherwise copy them in manually.
   - With the models uploaded and the environment configured, you can now run the dbt models. Go to the "Run" tab in dbt Cloud, and you can manually trigger a run or schedule runs at your convenience, or alternatively use the `dbt build` and `dbt run` commands in the console.

4. **PowerBI Setup**
    - PowerBI can be used to visualise and further analyse the outputs. The Desktop version is freely available at [PowerBI Desktop](https://powerbi.microsoft.com/en-us/desktop/).
    - If you already have a Microsoft account, you can sign in to PowerBI. If not, you will need to create an account.4. **Connect to Your Data**:
    - Open the "News_Analytics_Dashboard.pbix" file, go to Home>Transform Data and edit the "Source" step of each query to get data from your BigQuery (or alternative) database. Once all sources are correct, press "Close and Apply" and then "Refresh".
    - You are free to use the provided interactive visuals, edit them, or create new ones using the PowerBI interface.

## Contributing
We welcome contributions to the News-Analytics project! If you would like to help:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/my-new-feature`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to your branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request against the main project.

The repository would especially benefit from:
- More integration options beyond Google Cloud,
- More advanced NLP techniques,
- Increased test coverage,
- Documentation on how to set up a local version of dbt,
- Alternative visualisation platforms.

## License
News-Analytics is released under the Apache 2.0 License. See the [LICENSE file](https://github.com/0xMMC/News-Analytics?tab=Apache-2.0-1-ov-file) for more details.