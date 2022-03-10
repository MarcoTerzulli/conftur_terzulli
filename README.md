# conftur_terzulli

# Tirocinio-Multitraccia-DB
Repository contenente il nuovo database per la gestione dei pannelli fotovoltaici. Progettato e realizzato da **Marco Terzulli**

## 1 Contenuto della cartella di progetto
 * Interfaccia_Web - Cartella contenente le pagine web per un interfaccia front e back end di base
	* php - Cartella con tutta la parte backend e frontend (il frontend viene comunque elaborato dal backend con php)
		* css - Cartella contenente i fogli di stile delle pagine
		* js - Cartella contenente script javascript
		* dichiarazione_moduli.php - Homepage della sezione dichiarazione moduli e contributo ambientale
		* area_report.php - Homepage dell'area report
		* [...] Seguono file con le altre schermate

 * query_0_createdb.sql - Query di creazione utente e database
 * query_1_create_tables.sql - Query di creazione delle tabelle
 * query_2_create_triggers.sql - Query di creazione dei trigger di controllo
 * query_3_create_index.sql - Query per la creazione degli indici sulle tabelle
 
 * Import_Tabelle_FileMaker - Cartella contenente gli script di importazione delle tabelle e gli export di filemaker
	* DB_import_tables.py - Script di importazione
	* DB_script_utils.py - Racchiude funzioni utili
	* DB_scripts_configuration.py - File di configurazione per l'import e la connessione al DB
	* [...] Seguono file di export di FileMaker XLS e CSV
 
 * Script_Caricamento_Tracciati - Cartella contenente lo script per il caricamento giornaliero dei tracciati
	* DB_insert_tracciati.py - Script per il caricamento giornaliero dei tracciati
	* DB_script_utils.py - Racchiude funzioni utili
	* DB_scripts_configuration.py - File di configurazione per l'import e la connessione al DB
	* test_generatore_tracciato.py - Script per la generazione di un tracciato di test (usato per il debug)
 
 
## 2 Per iniziare

Le seguenti istruzioni ti permetteranno di avere una copia del progetto funzionante sulla tua macchina locale.

### 2.1 Prerequisiti

Software da installare affinché il progetto funzioni, e come installarlo.

```
* Una macchina con sitema operativo Windows, Linux o MacOS
* Python 3.7+
* Python Pip3
* PostrgreSQL 12.2+
* Server PHP
```

### 2.2 Creazione della Base di Dati

La creazione della base di dati è suddivisa in più passi: <br />

1. *Creazione del DataBase e dell'utente admin* <br />
Eseguire, su una console di postgresql, il file query_0_createdb.sql

2. *Creazione delle tabelle* <br />
Eseguire, su una console di postgresql, il file query_1_create_tables.sql <br />
*ATTENZIONE*: potrebbe essere necessario selezionare lo schema ftv_db, creato al passo precedente.

3. *Creazione dei trigger di controllo* <br />
Eseguire, su una console di postgresql, il file query_2_create_triggers.sql <br />

4. *Creazione degli indici* <br />
Eseguire, su una console di postgresql, il file query_3_create_index.sql <br />
*ATTENZIONE*: per ragioni di efficienza, gli indici vanno creati solo dopo l'importazione dei dati.

### 2.3 Importazione dei dati

La cartella Import_Tabelle_FileMaker contiene lo script di importazione ed un file di configurazione, oltre ai file esportati da FileMaker per i test.
*Premessa*: lo script di importazione è stato realizzato con filtri ad hoc per il formato ed i problemi presenti negli export dai file forniti da Multitraccia. Tale script potrebbe non funzionare nel modo corretto con file o dati molto differenti.
<br />
1. *Selezione degli export da usare* <br/>
È possibile impostare i file a livello globale dal file di configurazione DB_scripts_configuration.py. In alternativa, si possono selezionare singolarmente (per ogni tabella) agendo sui parametri delle rispettive funzioni presenti nello script DB_import_tables.py

2. *Importazione tabelle*<br/>
L'importazione avviene eseguento lo script DB_import_tables.py. Lo script è configurato per usare i file specificati nel file di configurazione. Di default, lo script importa tutte le tabelle tranne quella dei moduli (data la sua dimensione).<br />
*ATTENZIONE*: non sono state fornite alcune tabelle (come quelle relative all'anagrafica dei produttori) per ragioni di privacy; non conoscendo la struttura effettiva del file, lo script utilizzerà dati di prova; non sono state realizzate le funzioni per caricare i dati dai relativi file; ai moduli viene "collegato" un listino di test per tale ragione (*È ESSENZIALE MODIFICARE LO SCRIPT IN QUESTA PARTE*)

3. *Creazione degli indici nel DB*<br/>
Vedere sezione 2.2, paragrafo 4.

## 3 Fruizione delle pagine Web
La seguente sezione illustra come predisporre i file necessari alla fruizione del sito.

### 3.1 Installazione
Per accedere alle pagine web è essenziale disporre di un server PHP. <br/>

Copiare il contenuto della cartella Interfaccia_Web in modo opportuno nella cartella adibita al server PHP.<br/>

### 3.2 Descrizione pagine
I file dichiarazione_moduli.php ed area_report rappresentano rispettivamente le pagine home delle sezioni Dichiarazione Moduli ed Area Report.<br/>
Le pagine sono state pensate per essere integrate all'interno del sito web, sfruttando i suoi menù di navigazione (header e footer).<br/>
*ATTENZIONE*: gli script PHP necessitano di informazioni recuperate dalla sessione dell'utente loggato; tuttavia, questa parte non è stata affrontata e quindi sono state predisposte delle variabili di test.

### 3.3 Upload Tracciati
La pagina caricamento_tracciati.php permette il caricamento dei file txt dei tracciati sul server; i file vengono salvati all'intenro di cartelle con il codice fiscale come nome, a loro volta poste all'interno di una cartella "uploads".<br/>
*ATTENZIONE*: è necessario impostare il percorso corretto per la creazione della cartella dedicata agli upload!

## 4 Caricamento dei tracciati nel DataBase
Il caricamento dei tracciati sul server avviene mediante l'apposita pagina del sito, come descritto nel punto 3.3.<br/>
L'inserimento dei tracciati nel DataBase viene effettuato mediante l'utilizzo dello script DB_insert_tracciati.py.<br/>
*ATTENZIONE*: È necessario specificare il percorso della cartella upload sul server<br/>
*ATTENZIONE*: Lo script necessita dell'accesso con pribilegi elevati (anche in scrittura) alla cartella uploads per l'eliminazione dei file txt elaborati<br/>
*ATTENZIONE*: Lo script è predisposto per l'invio della mail con la dichiarazione mediante protocollo SMTP; è necessario configurare l'invio e specificare l'indirizzo del server SMTP<br/>


## 5 Software usato per lo sviluppo
* [JetBrains Pycharm](https://www.jetbrains.com/pycharm/) - IDE usato per sviluppo e test
* [JetBrains DataGrip](https://www.jetbrains.com/datagrip/) - IDE usato per sviluppo e test
* [JetBrains webStorm](https://www.jetbrains.com/webstorm/) - IDE usato per sviluppo e test
* [JetBrains PHPStorm](https://www.jetbrains.com/phpstorm/) - IDE usato per sviluppo e test
* PostgreSQL - DBMS 
* VMWare Workstation PRO - HyperVisor per la virtualizzazione di MacOS con FileMaker
* FileMaker Pro 10 -  DBMS del database originario
* MacOSX 10.6 e 10.5 - OS delle macchine virtuali del server originario
* XAMPP - Server PHP

## 6 Problemi noti

* Il database prevede dei domini per i tipi di dato che non possono essere utilizzati (e sono comentati) con i dati del db originario, in quanto vi sono alcuni casi in cui dati incongruenti non rispettano il tipo

* Il database prevede delle specifiche procedure di controllo per la coerenza dei dati, tuttavia alcune di esse sono state commentate per i test

* L'help online dedicato alla generazione del file TXT con il tracciato può impiegare un paio di secondi per essere caricata a causa della generazione dinamica della tabella in javascript lenta

* La visualizzazione dei moduli di un tracciato con 100k record può richiedere minuti interi di caricamento. La query verso il DB, così come la ricezione della risposta, è istantanea, tuttavia il browser impiega un tempo eccessivo per la generazione della tabella (la pagina continua a caricare aggiungendo righe). Bisognerebbe suddividere il risultato in chunk e predisporre una tabella con più pagine.

* Lo script di importazione lega ad ogni modulo un listino di un utente di test, anziché quello corretto. Questo è necessario in assenza degli export delle anagrafiche dei produttori e dei relativi listini
