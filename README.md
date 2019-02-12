# Documents

This repository just is used when you have account of Gleim.com

## Required

The Pycharm IDE (or any Python's IDE) 

The [Web Scrapper]('webscraper.io/') on Chrome kernel (I use Vivaldi browser)

MS Excel or LibreOffice Calc or Google Sheets (I use Google Sheets)

## Usage

Firstly, we use Web Scrapper tool to auto collect each HTML's question and answer. The sitemap in file ```WebScrapper.Json```

Secondly, we've already had data which scrapped. Put them into Excel Column B.

Then, we take JSON file from /Network in ```Ctrl + Shift + I```

After that, we run ```extractFromJson.py```  and have a ```cia_explanation.txt```. Copy that and put into Excel Column D.

Run ```extractTitle.py``` and take a ```cia_title.txt```. Copy that and put into Excel Column A.

Run ```extractNumber.py``` and take a ```cia_number.txt```. Copy that and put into Excel Column C.

In Column D, we input ```=CONCATENATE(C1, " | " ,A1, "<br><br>" , B1, "<br><br>", D1)``` then scroll all of rows we have.

Finally, copy all column D and put into some text editor (I use Sublime, we can use notepad, etc.) and save as ```output1.html```

Open the ```output1.html```, we have our result expected.  

## Contact
levuminhhuy.compsci@gmail.com
