# ConfTur Terzulli
**ConfTur project**'s repository - **Marco Terzulli**'s Internship and Thesis for the **Master Degree in Computer Science** at [**University of Modena and Reggio Emilia**](https://www.unimore.it/).

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

You can do so by running the following command in a Python shell: ```python -m spacy download xx_ent_wiki_sm```

TODO: <br />

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
* 

<p align="right">(<a href="#top">back to top</a>)</p>

## References
* [Repository dblp-to-csv](https://github.com/ThomHurks/dblp-to-csv) - Source of the DBLP XML to CSV Conversion Script

<p align="right">(<a href="#top">back to top</a>)</p>


## Appendix

### Contents of the Project Folder
* ```1 - Citation Dumps Preprocess``` - Workbook containing the notebooks for managing the preprocessing of the starting data on the citations
	* ```preprocess_dblp.ipynb``` -Jupyter Notebook for DBLP dump preprocessing management.
	* ```preprocess_mag.ipynb``` -  Jupyter Notebook for managing the preprocessing of the Microsoft Academics Graph dump. Possibility of using a preprocessed CSV for the Papers file (result from a previous processing using this script).
	* ```preprocess_opencitations.ipynb``` - Jupyter Notebook for managing the preprocessing of the OpenCitations dump. Script for sequential processing and merging of all files in a directory. Possibility of merge with CSV resulting from the processing of a subset of the dump.
	* ```XMLToCSV.py``` - Python script for converting the DBLP Dump from XML to CSV. The script was made by *Thom Hurks* (see References section)

* ```2 - Conference Location Web Scraping``` - Workbook containing notebooks for managing web scraping on conference locations
	* ```Old Files Backup``` - Backup folder for old work files
	* ```1 - dblp_add_locations_from_raw_dblp_dump.ipynb``` - Jupyter Notebook for adding the DBLP conferences locations using the proceedings data extracted from the RAW XML DBLP Dump.
	* ```1 - mag_fix_locations_from_raw_dblp_dump.ipynb``` - Jupyter Notebook for fixing the missing Microsoft Academics Graph conferences locations using the proceedings data extracted from the RAW XML DBLP Dump.
	* ```2 - dblp_location_scraper.ipynb``` - Jupyter Notebook for fixing the missing DBLP conferences locations via web scraping to the DBLP website.
	* ```2 - mag_location_scraper.ipynb``` - Jupyter Notebook for fixing the missing Microsoft Academics Graph conferences locations via web scraping to the DBLP website.
	* ```location_scraper_multithread_utils.py``` - Python file with function definitions for web scraping using multithreading and multiprocessing.
 * 

<p align="right">(<a href="#top">back to top</a>)</p>