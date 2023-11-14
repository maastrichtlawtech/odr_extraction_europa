# odr_extraction_europa
Converting ODR list from pdf to dataframe


Requirements
- python 3.9+ with pip installed


How to execute the code?
1. Copy the project onto your computer, open in your favourite IDE or enter it in CMD.
2. Run ```pip install --user virtualenv``` in the terminal.
3. Run ```virtualenv .venv' in the terminal``` to create a virtual environment.
4. Run ```source .venv/bin/activate``` on Mac/Linux or ```.\.venv\Scripts\activate``` on Windows in your terminal.
5. Run ```pip install -r requirements.txt``` in the terminal.
6. Run the 'separating.py' file - it will create a csv file called data.csv with the final dataframe in the same folder.

In this project we already included an html file which was acquired through downloading all of the cases from [Dispute resolution bodies](https://ec.europa.eu/consumers/odr/main/?event=main.adr.show2).
If you would like to use your own html file, make sure to put it in the same folder. You will also have to edit the 'separating.py' file.
Change the value of the 'HTML_FILE_PATH' variable which can be found at the top of the file to the name of your new html file, then run the file as normal.
