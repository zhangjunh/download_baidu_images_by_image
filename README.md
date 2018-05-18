# Download_Baidu_Images_by_Image

- An implement of download images which are similar to local pictures.
- Used for increase the amount of dataset.
- Search by baidu.com

## Requirements
- python 3+
- requests
- json
- re
- urllib
- hashlib
- PIL

## How to use

1. Choose some pictures in different labels, and put those photos who belonging 
to same label in a dir named with a number. Copy dirs into a dir named 
"additive", such as:
      - additive >> 99 >> 10110.jpeg...

2. Copy original dataset to dir named "train".Such as:
      - train >> 99 >> 10110.jpeg...
      - If the label number not exist in "train", pictures will be deleted after
      download.
      
3. Start to download and run follow-up processing:
      > python main.py
      - After the download is finished, those pictures will be merged with original
       datasets based on their labels. Same pictures will be deleted which are
        found by the same md5s. Followed by a convert to ".jpeg" and merge again, 
        your dataset will extend by similar images.
