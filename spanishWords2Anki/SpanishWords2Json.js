var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);

// output to allProcessedData
var allProcessedData = {};

var ajaxRequestData = ['a',
  'a él',
  'a menudo',
  'a mí',
  'a nosotros'];

const spanishdictURL = 'https://www.spanishdict.com/translate/';


var getSpanishWordDefinitionHTML = (word, html) => {
  console.log('Downloading : ', word);
  let $devDiv = $(html).find('#dictionary-neodict-es').children('div')
  let $searchedWord = $devDiv.find('span').first().text()
  allProcessedData[$searchedWord] = $devDiv.html()
}


// For each data in ajaxRequestData, we will get the html webpage code, and call helper function()
// Each ajax request is waited, and only go to next ajax request if this succeed.
var promiseRecursive = (index) => {
  if (index >= ajaxRequestData.length) {
    return;
  }
  setTimeout(() => { 
    $.ajax({
      url: spanishdictURL + ajaxRequestData[index]
      , success: (response) => {
        getSpanishWordDefinitionHTML(ajaxRequestData[index], response);
        promiseRecursive(index + 1);
      }
    });
  }, 5000);
}

// This is how to start stock crawler
promiseRecursive(0)
