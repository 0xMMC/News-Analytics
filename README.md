# News-Analytics

The purpose of this function is to allow users to retrieve news articles on specific topics, 
    and then analyse the content of those articles to extract useful insights, such as sentiment, 
    keywords, and named entities. This information can be used for further analysis or processing.

The function retrieves news articles from the NewsAPI based on a specified topic and date range. 
    It performs the following key tasks:
    1. Constructs a URL for the NewsAPI using the provided parameters (topic, start date, end date).
    2. Sends a GET request to the NewsAPI and processes the JSON response to create a pandas DataFrame 
    containing the article data.
    3. Extracts sentiment scores, keywords, and named entities from the article titles and summaries 
    using various NLP techniques.
    4. Creates additional pandas DataFrames to store the extracted information.
    5. Returns a tuple containing the original article DataFrame and the additional DataFrames with 
    the extracted data.


1) Install terraform:
This allows us to define cloud and on-prem resources in human-readable configuration files that we can version, reuse, and share.
https://developer.hashicorp.com/terraform/install

Note: A service account is necessary to prove to the cloud provider that we have the privileges necessary to create resources.

Download JSON key into the terrafrom folder.

The Project ID in GCP is in Cloud Overview > Dashboard (Project Info area).

Set keys location, project name, bucket name and region in variables.tf
Run:
terraform init
terraform plan
terraform apply

2) Mage setup
Need to set news API as secret
??? Need to install requirements.txt in the Mage Terminal panel
???Run python -m spacy download en_core_web_sm in terminal


- Also create a new service account with Storage Admin and BigQuery Admin privileges and create a key to use the account on the VM. Copy the json key to the mage folder. This is made accessible to the Mage docker image because the docker-compose.yml file has a line under volumes to mount ".:/home/src/" ,which is the source folder, to the docker image.
- We must then edit the io_config.yaml file to point the credentials to the file. We can delete the first path (the manual copy paste of the key) and just point to the file.

GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/path/to/your/service/account/key.json"
