	 ______________________________________________________

		CSVTOSEPADD -- A SIMPLE CSV TO SEPA XML
			       CONVERTER

	  Michael Fiedler <dev %AT% michael-fiedler %DOT% net>
	 ______________________________________________________


Table of Contents
_________________

1 German
.. 1.1 Kurzbeschreibung
.. 1.2 Einrichtung
.. 1.3 Verwendung
.. 1.4 Lizenz
.. 1.5 Kontakt
2 English
.. 2.1 Description
.. 2.2 Setup
.. 2.3 Usage
.. 2.4 License
.. 2.5 Contact





1 German
========

1.1 Kurzbeschreibung
~~~~~~~~~~~~~~~~~~~~

  `CsvToSepaDD' erzeugt aus einer CSV-Datei eine SEPA-XML-Datei nach dem
  Standard `pain.008.003.02' für SEPA-Basislastschriften.  Die Datei
  kann dann zum Beispiel im Online-Banking deutscher Banken hochgeladen
  werden, um einen Lastschrifteinzug zu tätigen.

  Hinweis: Vor dem endgültigem Absenden der erzeugten Datei an die Bank
  sollten die Angaben darin nochmal auf Korrektheit überprüft werden, da
  das Skript auf eigene Gefahr benutzt wird.


1.2 Einrichtung
~~~~~~~~~~~~~~~

  `CsvToSepaDD' erfordert das Vorhandensein von [`PySepaDD'] im
  `PYTHONPATH':

  ,----
  | export PYTHONPATH=.:/pfad/zu/PySepaDD
  `----

  `PySepaDD' kann entweder von der Projektseite heruntergeladen werden
  oder bei Verwendung der Git-Version von `CsvToSepaDD' als
  Git-Teilmodul bezogen werden:

  ,----
  | git clone https://github.com/mfiedler/CsvToSepaDD.git
  | cd CsvToSepaDD
  | git submodule init
  | git submodule update
  | export PYTHONPATH=.:PySepaDD
  `----


  [`PySepaDD'] https://github.com/mfiedler/PySepaDD


1.3 Verwendung
~~~~~~~~~~~~~~

  Als Eingabedaten wird eine CSV-Datei verwendet.  In ihrer ersten Zeile
  muss sie die Feldnamen enthalten, ab der zweiten Zeile folgen die
  eigentlichen Nutzdaten.  Erforderliche Feldnamen sind:

  - `first_name' und `last_name' für den Vor- und Nachnamen des Inhabers
    des zu belastenden Kontos

  - `IBAN' und `BIC' als Angabe des zu belastenden Kontos

  - `amount' als abzubuchender Betrag in Euro (erlaubte Formate: `42',
    `42.0', `42.00', `42,0', `42,00')

  - `type' als Angabe, ob es sich bei der Lastschrift um eine erstmalige
    (Wert `FRST'), eine nachfolgende (`RCUR') oder letztmalige (`FNAL')
    innerhalb einer ganzen Reihe von wiederkehrenden Lastschriften oder
    aber um eine einmalige (`OOFF') Lastschrift handelt.  Bei `OOFF' ist
    das Mandat nur für die eine Abbuchung gültig.

  - `collection_date' als Datum der Belastung (erlaubte Formate:
    `2014-12-27', `27.12.2014', `27.12.14')

  - `mandate_id' und `mandate_date' als Mandatsreferenz und Datum der
    Ausstellung des Mandats (Datumsformat wie bei `collection_date')

  - `description' als Verwendungszweck

  Zusätzlich vorhandene Felder in der CSV-Datei werden ignoriert.

  Zum Aufruf des Skripts wird zunächst eine Konfigurationsdatei mit den
  Informationen zum Einziehenden erstellt.  Hierbei werden der Name des
  Gläubigers sowie seine IBAN, BIC und Gläubiger-ID abgefragt.  Außerdem
  wird das Format der CSV-Datei mit den Eingabedaten benötigt
  (z. B. `calc-default' für das von LibreOffice/OpenOffice mit den
  Standardeinstellungen erzeugte Format).  Für Details zu möglichen
  Formaten hilft ein Blick in die Datei `CsvToSepaDD.py' weiter, wo am
  Anfang die CSV-Dialekte registriert werden.  Analog kann auch ein
  eigener hier eingetragen werden, vgl. dazu die [Python-Dokumentation
  zu CSV-Dialekten].  Die Konfigurationsdatei kann bei Bedarf
  nachträglich mit einem Texteditor verändert werden.

  ,----
  | ./CsvToSepaDD.py genconfig config.py
  `----

  Unter Angabe der Konfigurationsdatei werden dann die Eingabedateien in
  eine SEPA-XML-Datei umgewandelt:

  ,----
  | ./CsvToSepaDD.py convert input.csv output.xml
  `----


  [Python-Dokumentation zu CSV-Dialekten]
  https://docs.python.org/2/library/csv.html#dialects-and-formatting-parameters


1.4 Lizenz
~~~~~~~~~~

  (C) 2014 Michael Fiedler <dev %AT% michael-fiedler %DOT% net>

  Diese Software darf unter den Bedingungen der geänderten BSD-Lizenz
  verwendet werden.  Der vollständige Lizenztext ist in der Datei
  `LICENCE.BSD' zu finden.


1.5 Kontakt
~~~~~~~~~~~

  Siehe die [Projektseite] für das System zum Einreichen von
  Fehlermeldungen und weitere Kontaktinformationen.


  [Projektseite] https://github.com/mfiedler/CsvToSepaDD


2 English
=========

2.1 Description
~~~~~~~~~~~~~~~

  `CsvToSepaDD' is a very simple converter from CSV to SEPA XML: It
  takes CSV input data representing SEPA Core Direct Debit instructions
  and creates a SEPA XML file conforming to `pain.008.003.02' standard.
  That XML file can then be uploaded to the online banking application
  of German banks in order to carry out the transactions.

  Notice: Before sending the generated file to your bank, verify it for
  correctness once again, as use is at your own risk.


2.2 Setup
~~~~~~~~~

  `CsvToSepaDD' depends on a version of [`PySepaDD'] in `PYTHONPATH':

  ,----
  | export PYTHONPATH=.:/path/to/PySepaDD
  `----

  `PySepaDD' can either be downloaded from its project page or, if
  `CsvToSepaDD' is used from the Git repository, be obtained as a Git
  submodule:

  ,----
  | git clone https://github.com/mfiedler/CsvToSepaDD.git
  | cd CsvToSepaDD
  | git submodule init
  | git submodule update
  | export PYTHONPATH=.:PySepaDD
  `----


  [`PySepaDD'] https://github.com/mfiedler/PySepaDD


2.3 Usage
~~~~~~~~~

  The `CsvToSepaDD.py' script uses a CSV file for input data.  The first
  row must contain the available fields, the second and further rows
  represent the actual data.  The following fields are required:

  - `first_name' and `last_name' as first and last name of the debtor

  - `IBAN' and `BIC' of the debtor's bank account

  - `amount' in Euro to be transfered (valid formats: `42', `42.0',
    `42.00', `42,0', `42,00')

  - `type' of the direct debit: `FRST' for the first transaction, `RCUR'
    a follow-up or `FNAL' as the last one in a sequence of transactions;
    or `OOFF' for a only-once transaction (the mandate is only valid for
    that transaction)

  - `collection_date' as the debit's transaction date (valid formats:
    `2014-12-27', `27.12.2014', `27.12.14')

  - `mandate_id' and `mandate_date' as the identifier for the mandate
    and the date the mandate was signed (date format as above)

  - `description' of the transaction

  Additional fields in the CSV file are ignored.

  When using the script, you first need to create a configuration file
  containing the creditor's data.  These are the creditor's name, his
  account's IBAN and BIC and his creditor identifier.  Moreover, the
  format of the input CSV data must be specified (e. g. `calc-default'
  for the default export settings of LibreOffice/OpenOffice Calc).  See
  `CsvToSepaDD.py' source for details of the available formats.  If you
  need another format than already there, just specify you own one in
  that file; see [Python's documentation on CSV dialects] for more
  information.  You can change the configuration file after creating it
  using a texteditor of your choice.

  ,----
  | ./CsvToSepaDD.py genconfig config.py
  `----

  Now convert the input data to SEPA XML, referring to the created
  configuration file:

  ,----
  | ./CsvToSepaDD.py convert input.csv output.xml
  `----


  [Python's documentation on CSV dialects]
  https://docs.python.org/2/library/csv.html#dialects-and-formatting-parameters


2.4 License
~~~~~~~~~~~

  (C) 2014 Michael Fiedler <dev %AT% michael-fiedler %DOT% net>

  You can use this project under the terms of the modified BSD license,
  see the file `LICENSE.BSD' for the full license text.


2.5 Contact
~~~~~~~~~~~

  See the [project page] for an issue tracker and further contact
  information.


  [project page] https://github.com/mfiedler/CsvToSepaDD
