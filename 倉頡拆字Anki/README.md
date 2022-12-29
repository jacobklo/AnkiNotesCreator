# 倉頡拆字 Anki Creator

## features
1. 18638 Tranditonal Chinese characters
2. 7951 圖解倉頡拆字 ( Pictures Sources: https://www.hkcards.com/ )
3. Different tags for each keys
4. Custom Fonts embedded in Anki package that support Chinese ( Font Source: https://www.freechinesefont.com/ )

# Steps

## Crawl all 倉頡拆字 Data
By using crawlChangJie.js from ActiveTabWebpageCrawlerSynchronous.git\
You will get the following json data

```json
{
    "一": [
        "一",
        "https://www.hkcards.com/img/cj/一.png"
    ],
    "七": [
        "十山",
        "https://www.hkcards.com/img/cj/七.png"
    ],
    "丄": [
        "中一",
        ""
    ],
    ...
}
```

## Download all pictures
using downloadFromUrlArray.py

## Rename Urls
the Json file from step 1, change all Urls to filename only.

```json
{
    "一": [
        "一",
        "一.png"
    ],
    "七": [
        "十山",
        "七.png"
    ],
    "丄": [
        "中一",
        ""
    ],
    ...
}
```

## Creat Anki from Json file
changJieTson2Anki.py
