from __future__ import annotations
from typing import List
import json
import hashlib
import genanki


def convertChangJieJson2Anki(filename: str):
  f = open(filename+'.json', 'r')
  changjie = json.load(f)
  f.close()

  my_model = MyModel('倉頡拆字模型', front_html=QUESTION, back_html=ANSWER
   , fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Image'}], css=STYLE)

  # hash for Anki to know when the same Deck is changed
  my_deck = genanki.Deck(deck_id=abs(hash('倉頡拆字')) % (10 ** 10), name='倉頡拆字')

  # use to import images, but also the custom fonts too
  media_files = ['_DroidSansFallback.ttf']
  
  for character, v in changjie.items():
    changjieKeys = v[0]
    imgName = v[1]
    # add tags, for easy search for custom study
    tags = []

    if imgName:
      media_files += ['images/'+imgName]
      tags += ['有圖']
    
    # tags map to each changJie 26 Keys
    for i in range(len(changjieKeys)):
      # just the keys
      tags += [changjieKeys[i]]
      # Also that key and position
      tags += [changjieKeys[i]+str(i)]

    # add tags for 標點符號
    if changjieKeys[:2] == 'z難':
      tags += ['標點符號']

    # In Anki, Images needs to direct references using HTML, without folders
    # https://docs.ankiweb.net/importing.html#importing-media
    img_html = '<img src="'+imgName+'">'
    newNotes = genanki.Note(model=my_model, fields=[character, changjieKeys, img_html], tags=tags)
    my_deck.add_note(newNotes)

  anki_output = genanki.Package(my_deck)
  anki_output.media_files = media_files
  anki_output.write_to_file('倉頡拆字.apkg')


class MyModel(genanki.Model):

  def __init__(self, name: str, fields: List, front_html: str, back_html: str, css: str):
    hash_object = hashlib.sha1(name.encode('utf-8'))
    hex_dig = int(hash_object.hexdigest(), 16) % (10 ** 10)
    
    templates = [
      {
        'name': '倉頡卡',
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
{{Question}}
<br>
{{Image}}
<br>
{{Answer}}
</div>
<footer>
  <p>Source: hkcards.com</p>
</footer>
'''


STYLE = '''
div {
}

.card {
}

.front {
  background-color: rgba(0, 0, 0,1);
  font-size: xx-large;
  font-family: "myfont";
  text-align: center;
  color: white;
  text-shadow: 1px 1px 1px rgba(0,128,255,0.7),
             5px 5px 5px rgba(0,128,255,0.4),
             10px 10px 10px rgba(0,128,255,0.1);
}

.back {
    background-color: rgba(0, 0, 0,1);
  font-size: xx-large;
  font-family: "myfont";
  text-align: center;
  color: white;
  text-shadow: 1px 1px 1px rgba(0,128,255,0.7),
             5px 5px 5px rgba(0,128,255,0.4),
             10px 10px 10px rgba(0,128,255,0.1);
}


@font-face { 
  font-family: myfont; 
  src: url('_DroidSansFallback.ttf'); 
}
'''

if __name__ == "__main__":
  convertChangJieJson2Anki('changjie18638')
