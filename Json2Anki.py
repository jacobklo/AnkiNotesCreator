from __future__ import annotations
from typing import List
import json
import hashlib
import genanki


def convertSpanishWordsJson2Anki(filename: str):
  f = open(filename+'.json', 'r')
  words_dict = json.load(f)
  f.close()

  my_model = MyModel(filename+' Model', fields=[{'name': 'Question'}, {'name': 'Answer'}],
   front_html=QUESTION, back_html=ANSWER, css=STYLE)

  my_deck = genanki.Deck(deck_id=abs(hash(filename)) % (10 ** 10), name=filename)

  for word, html in words_dict.items():
    newNotes = genanki.Note(model=my_model, fields=[word, html], tags=[filename])
    my_deck.add_note(newNotes)

  anki_output = genanki.Package(my_deck)
  anki_output.write_to_file(filename+'.apkg')



class MyModel(genanki.Model):

  def __init__(self, name: str, fields: List, front_html: str, back_html: str, css: str):
    hash_object = hashlib.sha1(name.encode('utf-8'))
    hex_dig = int(hash_object.hexdigest(), 16) % (10 ** 10)
    
    templates = [
      {
        'name': 'Card 1',
        'qfmt': front_html,
        'afmt': back_html,
      }
    ]
    super(MyModel, self).__init__(model_id=hex_dig, name=name, fields=fields, templates=templates, css=css)



QUESTION = '''
<div class="front">{{Question}}</div>
'''


ANSWER = '''
<div class="back">
{{Answer}}
</div>
'''


STYLE = '''
.card {
 font-family: 'DejaVu Sans Mono';
 text-align: left;
 color: white;
 background-color: rgba(42, 129, 151,1);
 text-shadow: 0px 4px 3px rgba(0,0,0,0.4),
             0px 8px 13px rgba(0,0,0,0.1),
             0px 18px 23px rgba(0,0,0,0.1);
}

.front {
	font-size: 14px;
}

.back {
	font-size: 14px;

}

div.o9Q4V2vd {
  margin-bottom: 50px;
}


@font-face { font-family: DejaVu Sans Mono; src: url('_DejaVuSansMono.ttf'); }
'''


convertSpanishWordsJson2Anki('spanishHTML')
