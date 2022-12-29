## This simple program is written to help convert Words in Duolingo into Anki Notes.

#### The spanishWords2Json.js is designed to run in Browser.
#### The Json2Anki.py can be ran in python


### Step 0 (Optional): See bottom.

### Step 1: Update the spanish words you want to download its definition
Go to change the variable `ajaxRequestData` in `SpanishWords2Json.js`

### Step 2: Open a new tab in Chrome or Firefox, and go to https://www.spanishdict.com

### Step 3: Open Developer Console

### Step 4: Copy all the code in `SpanishWords2Json.js` and run in the console.

### Step 5: Wait til finish ( the last spanish words shows in console )

### Step 6: type allProcessedData in console and press enter:
```
allProcessedData
```

### Step 7: Right click and Press 'Copy Object' on the results of allProcessedData

### Step 8: Paste the results into a new Text editor. This becomes a JSON file stores definitions in HTML format for each spanish words. And combine as a JSON dictionary.

### Step 9: Open Json2Anki.py in text editor. Edit the main function input to your Json (default: spanishHTML.json)

### Step 10: Run Json2Anki.py


### Step 0 (Optional): Download list of spanish words from https://www.duolingo.com/words
#### Step 0.1: Save the webpage into *.html file and store locally
#### Step 0.2: Open new Excel file, go to Data -> From Web. The URL gives the full local path to your downloaded HTML file.
```
C:\Users\username\Desktop\spanish.html
```
#### Step 0.3: save as .CSV file
#### Step 0.4: Open that CSV file in Visual Studio Code, use the multiple line feature to change format to fit Javascript
