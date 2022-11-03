# ConfTur Terzulli
**ConfTur project**'s repository - **Marco Terzulli**'s Internship and Thesis for the **Master Degree in Computer Science** at [**University of Modena and Reggio Emilia**](https://www.unimore.it/).
<br><br>
This repository contains code which analyzes data for studying the correlation between the *"touristicy"* of conference venue and its articles impact.

## Table of Contents
<ol>
	<li>
		<a href="#get-started">Get Started</a>
		<ul>
			<li><a href="#prerequisites">Prerequisites</a></li>
			<li><a href="#installation">Installation</a></li>
		</ul>
	</li>
	<li><a href="#citation-datasets-dumps">Citation Datasets Dumps</a></li>
	<li><a href="#software--used-for-developmento">Software Used for Development</a></li>
	<li><a href="#known-issues">Known Issues</a></li>
	<li><a href="#references">References</a></li>
	<li>
		<a href="#appendix">Appendix</a>
		<ul>
			<li><a href="#contents-of-the-project-folder">Contents of the Project Folder</a></li>
		</ul>
	</li>
</ol>
 
 
## Get Started

The following instructions will allow you to have a working copy of the project on your local machine.

### Prerequisites

Software to install for the project to work, and how to install it.

```
* A Windows, Linux or MacOS machine
* Python 3.7+
* Python Pip3
```

Install the necessary Python Libraries using the following shell command: ```pip install -r requirements.txt```

### Installation

#### Download of the Spacy Pipelines
Before getting started, be sure to download the Spacy Pipelines that is needed for the NLP operations.

You can do so by running the following command in a Python shell: ```python -m spacy download en_core_web_lg```

<p align="right">(<a href="#top">back to top</a>)</p>



## Citation Datasets Dumps
At the following URLs it is possible to download the dumps of the starting datasets used in this project:
* [DBLP](https://dblp.uni-trier.de/xml/) - Dump Digital Bibliography & Library Project,
* [Microsoft Academics Graph](https://archive.org/download/mag-2021-06-07/mag/) - Dump *MAG* - Disused platform. Dump available on the **Archive.org** platform
* [OpenCitations COCI](https://opencitations.net/download) - Dump Crossref OpenCitations Index

<p align="right">(<a href="#top">back to top</a>)</p>

## Software Used for Development
* [Jupyter Notebook](https://jupyter.org/) - Development platform for the Python language
* [Visual Studio Code](https://code.visualstudio.com/) - IDE used for development and testing

<p align="right">(<a href="#top">back to top</a>)</p>

## Known Issues
No known issues so far.

<p align="right">(<a href="#top">back to top</a>)</p>

## References
* [Repository dblp-to-csv](https://github.com/ThomHurks/dblp-to-csv) - Source of the DBLP XML to CSV Conversion Script included in the *"1 - Citation Dumps Preprocess"* folder. All the rights of that script go to **Thom Hurks**, its author.


<p align="right">(<a href="#top">back to top</a>)</p>


## Appendix

### Contents of the Project Folder

* **Dataset Creation Pipeline** - This folder cointains the whole pipeline for the creation of the used datasets
	* **1 - Citation Dumps Preprocess** - Folder containing the notebooks for managing the preprocessing of the starting data on the citations
		* ```preprocess_dblp.ipynb``` - Jupyter Notebook for DBLP dump preprocessing management.
		* ```preprocess_mag.ipynb``` -  Jupyter Notebook for managing the preprocessing of the Microsoft Academics Graph dump. Possibility of using a preprocessed CSV for the Papers file (result from a previous processing using this script).
		* ```preprocess_opencitations.ipynb``` - Jupyter Notebook for managing the preprocessing of the OpenCitations dump. Script for sequential processing and merging of all files in a directory. Possibility of merge with CSV resulting from the processing of a subset of the dump.
		* ```XMLToCSV.py``` - Python script for converting the DBLP Dump from XML to CSV. The script was made by *Thom Hurks* (see References section)

	* **2 - Conference Location Web Scraping** - Folder containing the notebooks for managing the web scraping of the conference locations
		* ```1 - dblp_add_locations_from_raw_dblp_dump.ipynb``` - Jupyter Notebook for adding the DBLP conferences locations using the proceedings data extracted from the RAW XML DBLP Dump.
		* ```1 - mag_fix_locations_from_raw_dblp_dump.ipynb``` - Jupyter Notebook for fixing the missing Microsoft Academics Graph conferences locations using the proceedings data extracted from the RAW XML DBLP Dump.
		* ```2 - dblp_location_scraper.ipynb``` - Jupyter Notebook for fixing the missing DBLP conferences locations via web scraping to the DBLP website.
		* ```2 - mag_location_scraper.ipynb``` - Jupyter Notebook for fixing the missing Microsoft Academics Graph conferences locations via web scraping to the DBLP website.
		* ```location_scraper_multithread_utils.py``` - Python file with function definitions for web scraping using multithreading and multiprocessing.
	
	* **3 - Citation and Conference Data Join** - Folder containing the notebooks for managing the citation and locations data join operations between the COCI, DBLP and MAG processed datasets
		* ```1 - DBLP and MAG Data Join.ipynb``` - Jupyter Notebook for the join operations between the DBLP and MAG processed dumps.
		* ```2 - DBLP+MAG and COCI Data Join.ipynb``` - Jupyter Notebook for the join operations between the DBLP + MAG (joined dumps) and the COCI processed dumps.
		* ```3 - DBLP + MAG Join with COCI RAW for By Year Citations.ipynb``` - Jupyter Notebook for the join operations between the DBLP + MAG (joined dumps) and the COCI RAW dump. This notebook is going to produce a new dataset containing the papers citations for every year (extracted from the RAW COCI dump).
	
	* **4 - Citation and Conference Locations Data Cleanup** - Folder containing the notebooks for managing the disambiguation and normalization operations of the conference locations contained in the joined datasets.
		* ```Conference Locations Data Cleanup.ipynb``` - Jupyter Notebook for the disambiguation and normalization operations of the conference locations contained in the joined datasets.
	
	* **5 - Conference Ranking Data Integration** - Folder containing the notebooks for managing the integration of some conference ranking metrics.
		* ```1 - Citation and Locations Dataset Preparation.ipynb``` - Jupyter Notebook for the preparation of the cleaned Conference Citations and Locations dataset to the conference ranking data integration.
		* ```2 - CORE Conference Ranking Integration.ipynb``` - Jupyter Notebook for the integration of the CORE Conference Ranking to the cleaned Conference Citations and Locations dataset.
		* ```2 - GRIN Conference Rating Integration.ipynb``` - Jupyter Notebook for the integration of the GRIN Conference Rating to the cleaned Conference Citations and Locations dataset.
	
	* **6 - Conference Acceptance Rate Data Integration** - Folder containing the notebooks for managing the integration of the conferences acceptance rate data.
		* ```1 - Poggi Data Integration.ipynb``` - Jupyter Notebook for the integration of the conferences acceptance rate data obtained by **Prof. Francesco Poggi** (Prof at the University of Modena and Reggio Emilia) to the cleaned Conference Citations and Locations dataset.
	
	* **7 - Conference Names Fix** - Folder containing the notebooks for managing the fix of some conference names special cases.
		* ```Conference Names Fix.ipynb``` - Jupyter Notebook for the fix of some conference names special cases, that I didn't notice during the first processing and scraping operations.

	* **8 - Citation Datasets Separation for the Analysis** - Folder containing the notebooks for managing the separation of the different citation data sources from the joined datasets, making the data ready for our analysis.
		* ```Citation Datasets Separation for the Analysis.ipynb``` - Jupyter Notebook for the separation of the different citation data sources from the joined datasets. This notebook is going to create single datasets for the MAG and COCI citations (but keeping the location infos together). The new datasets are going to have a common structure, making them ready for our analysis.

	* **9 - Turistic Indexes Web Scraping** - Folder containing the notebooks for managing the web scraping of the Turistic Indexes.
		* ```Citation Datasets Separation for the Analysis.ipynb``` - Jupyter Notebook for the creation of the SWP (Size of the Wikepedia) Index via Web Scraping.

	* **10 - Touristic Indexes Join and Cleanup** - Folder containing the notebooks for managing the join and cleanup of the Turistic Indexes, which have been gathered by **Marco Lupis** (bechelor's degree student in Computer Science at the University of Modena and Reggio Emilia).
		* ```1 - city_touristic_indexes_join.ipynb``` - Jupyter Notebook for the join of all the city touristic indexes.
		* ```2 - country_touristic_indexes_cleanup.ipynb``` - Jupyter Notebook for the cleanup of country touristic index database.
 
* **Analysis** - This folder cointaining the notebook with the scripts used by our analysis
	* ```Analysis.ipynb.ipynb``` - Jupyter Notebook containing the scripts used by our analysis and some comments for the obtained results.

<p align="right">(<a href="#top">back to top</a>)</p>