# Conference Location Fix

For this phase of the work you have two possibilities:
* use the data already obtained from a previous work
* obtain new clean conferences locations data making queries to the DBLP website

During our tests we found out that DBLP servers were refusing the connections from our IPs, making our web scraper unreliable.
For this reason, we decided to use the conference location data obtained from a previous thesis work that you can fine [here](https://github.com/lbedogni/conftur).

## Use the Data Already Obtained from a Previous Work

Run the notebooks included in the ```2_1 - Conference Location from Old Works folder```.

## Obtain New Clean Conferences Locations Data Making Queries to the DBLP Website

Run the notebooks included in the ```2_2 - Conference Location Web Scraping```.

**Note**: the web scraper section is a work-in-progress and is not completed yet. We decided to continue our work using old data since we were stuck because DBLP was randomly blocking our incoming connections making our web scraper useless.