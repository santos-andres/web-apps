
# gis-web-app

Simple GIS webapp with Streamlit and deployed in Azure

## Setup
Optionnal if using GIT:

1. Install git and checkout the [git code repository]

Optionnal if python project:

2. Install [anaconda]/[miniconda] python version 3.6+
3. Change working directory the project root directory
4. Create the self contained conda environment. Open anaconda prompt and go to the project root directory and enter the command:

    `pip install -r requirements.txt`

5. .. Place your own project specific setup steps here e.g. copying data files ...


## Using the Python Conda environment

Once the Python Conda environment has been set up, you can

* Activate the environment using the following command in a terminal window:

    * Windows: `activate my_environment`
    * Linux, OS X: `source activate my_environment`
    * The __environment is activated per terminal session__, so you must activate it every time you open terminal.

* Deactivate the environment using the following command in a terminal window:

    * Windows: `deactivate my_environment`
    * Linux, OS X: `source deactivate my_environment`
               
* Delete the environment using the command (can't be undone):

    * `conda remove --name my_environment --all`

## Initial File Structure

```
├── config                   <- Config files 
│
├── data                     <- All the data
│
├── models                   <- Trained models
│
├── reports                  <- Visual exports (Tableau, Qlik, PowerBI, Images etc.)
│
├── scripts                  <- All scripts and code snippets
│
├── src                      <- Production ready code
│
├── tests                    <- Test cases
│  
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── requirements.txt         <- Essential python packages used in the project
│  
└── README.md                <- The top-level README for developers using this project.
```

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more 
than once then it should be placed into a common script / module under src and unit tests added. The same applies for 
any other non trivial code to ensure the correct functioning.

To run tests, install pytest and then from the repository root run
 
```
pytest
```

## Development Process
Contributions to this project are greatly appreciated and encouraged.

To contribute an update simply:

* Create a new branch / fork for your updates.
* Check that your code follows the PEP8 guidelines (line lengths up to 120 are ok) and other general conventions within this document.
* Ensure that as far as possible there are unit tests covering the functionality of any new code.
* Update the yml file for the python environment if new packages are installed
* Check that all existing unit tests still pass.
* Edit this document if needed to describe new files or other important information.
* Create a pull request.

## Data Architecture

The data folder is where all data related to the project should go. However, to ensure organization and clarity, we employ a medallion structure with staging, transformation, and output directories inside the data directory. This helps you know where to look for the data within your repo by assigning a role to each directory. Additionally, robust documentation on metadata for each file should be maintained to facilitate understanding of every datapoint.

### Staging
The staging directory contains all the 'raw' data and should remain unmodified to avoid altering client or project data. This ensures that there is no risk of altering the client or project's data. Additionally, it should be organized into subdirectories that correspond to the nature of the data. For example, staging/category/file.csv.

However, if the initial data changes, whether due to a new version or when working with a new daily file, it is necessary for you to archive the data. This can be achieved by using the following convention: staging/category/YYYY/MM/DD/file.csv. This approach allows access to previous versions, ensuring the ability to use the most recent one as the default. Refrain from saving any changes to the data in the staging directory.

### Transformation

The transformation directory will store the standardized version of transformed raw, storing cleaned data. In here is were cleaned data will be stored. Key transformations include managing missing values, standardizing formats or data types, and adjust data errors. However, no aggregations should be done to it just yet, this is saved for the data that will be stored in output. It is crucial to document these transformations and maintain metadata to provide a comprehensive understanding of the data processing history.

### Output

The output directory stores user or visualization ready data resides. In here you can find aggregated data that will be instrumental for data driven decisions, dashboards, and reports. Only data from the transformation directory should be used as the source ensuring that only cleaned and standardized data will be used for the aggregations. The level of granularity for the data in the output directory should be user or task specific. For example, sales_location1_Jan1990_Dec2000.csv.

## Contacts
* Author: Andres
* Agilytic team: Andres
* Client: internal

## References
* https://jerome_belp@bitbucket.org/jerome_belp/cookiecutter-agilytic.git - The master template for this project
* http://docs.python-guide.org/en/latest/writing/structure/
* https://drivendata.github.io/cookiecutter-data-science/

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
   [miniconda]: <https://docs.conda.io/en/latest/miniconda.html>
