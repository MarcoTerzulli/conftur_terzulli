# ConfTur Terzulli
Repository contenente i file di lavoro per il progetto ConfTur. Tirocinio di **Marco Terzulli**.

## Indice dei Contenuti
<ol>
	<li>
		<a href="#per-iniziare">Per Iniziare</a>
		<ul>
			<li><a href="#prerequisiti">Prerequisiti</a></li>
			<li><a href="#installaione">Installazione</a></li>
		</ul>
	</li>
	<li><a href="#dump-datasets-citazioni">Dump Datasets Citazioni</a></li>
	<li><a href="#software-usato-per-lo-sviluppo">Software Usato per lo Sviluppo</a></li>
	<li><a href="#problemi-noti">Problemi Noti</a></li>
	<li><a href="#riferimenti">Riferimenti</a></li>
	<li>
		<a href="#appendice">Appendice</a>
		<ul>
			<li><a href="#contenuto-della-cartella-di-progetto">Contenuto della Cartella di Progetto</a></li>
		</ul>
	</li>
</ol>
 
 
## Per iniziare

Le seguenti istruzioni ti permetteranno di avere una copia del progetto funzionante sulla tua macchina locale.

### Prerequisiti

Software da installare affinché il progetto funzioni, e come installarlo.

```
* Una macchina con sistema operativo Windows, Linux o MacOS
* Python 3.7+
* Python Pip3
* TODO
```

Installare le Librerie Python necessarie mediante il seguente comando da shell: ```pip install -r requirements.txt```

### Installazione

TODO: <br />

<p align="right">(<a href="#top">torna in cima</a>)</p>



## Dump Datasets Citazioni
Ai seguenti URL è possibile scaricare i dump dei dataset di partenza utilizzati:
* [DBLP](https://dblp.uni-trier.de/xml/) - Dump Digital Bibliography & Library Project,
* [Microsoft Academics Graph](https://archive.org/download/mag-2021-06-07/mag/) - Dump *MAG* - Piattaforma dismessa. Dump disponibile sulla piattaforma Archive.org
* [OpenCitations COCI](https://opencitations.net/download) - Dump Crossref OpenCitations Index

<p align="right">(<a href="#top">torna in cima</a>)</p>

## Software Usato per lo Sviluppo
* [Jupyter Notebook](https://jupyter.org/) - Piattaforma di sviluppo per il linguaggio Python
* [Visual Studio Code](https://code.visualstudio.com/) - IDE usato per sviluppo e test

<p align="right">(<a href="#top">torna in cima</a>)</p>

## Problemi noti
* 

<p align="right">(<a href="#top">torna in cima</a>)</p>

## Riferimenti
* [Repository dblp-to-csv](https://github.com/ThomHurks/dblp-to-csv) - Source of the DBLP XML to CSV Conversion Script

<p align="right">(<a href="#top">torna in cima</a>)</p>


## Appendice

### Contenuto della Cartella di Progetto
* ```1 - Citation Dumps Preprocess``` - Cartella di lavoro contenente i notebook per la gestione del preprocessing dei dati di partenza sulle citazioni
	* ```preprocess_dblp.ipynb``` - Jupyter Notebook per la gestione del preprocessing del dump di DBLP. (*versione Beta*)
	* ```preprocess_mag.ipynb``` - Jupyter Notebook per la gestione del preprocessing del dump di Microsoft Academics Graph. Possibilità di utilizzo di un CSV preprocessato per il file Papers (risultato da una precedente elaborazione mediante questo script).
	* ```preprocess_opencitations.ipynb``` - Jupyter Notebook per la gestione del preprocessing del dump di OpenCitations. Script per elaborazione e merge sequenziale di tutti i file in una directory. Possibilità di merge con CSV risultato dall'elaborazione di un subset del dump.
	* ```XMLToCSV.py``` - Script Python per la conversione del Dump di DBLP da XML a CSV. Lo script è stato realizzato da *Thom Hurks* (vedere sezione Riferimenti)

* ```2 - Conference Location Web Scraping``` - Cartella di lavoro contenente i notebook per la gestione del web scraping sulle location delle conferenze
	* ```Old Files Backup``` - Cartella di di backup per i vecchi file di lavoro
	* ```1 - dblp_location_scraper.ipynb``` - Jupyter Notebook per la gestione del web scraping sulle location del dump di DBLP.
	* ```1 - location_scraper_multithread_utils.py``` - File Python con le definizioni delle funzioni per il web scraping mediante multithreading e multiprocessing.
	* ```1 - mag_location_scraper.ipynb``` - Jupyter Notebook per la gestione del web scraping sulle location del dump di Microsoft Academics Graph.
	* ```1 - dblp_location_scraper.ipynb``` - Jupyter Notebook per il fix delle location di DBLP mancanti utilizzando il dump di DBLP.
	* ```1 - mag_location_scraper.ipynb``` - Jupyter Notebook per il fix delle location di Microsoft Academics Graph mancanti utilizzando il dump di DBLP.
 * TODO
 * 

<p align="right">(<a href="#top">torna in cima</a>)</p>