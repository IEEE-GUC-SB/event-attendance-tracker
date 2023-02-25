# Members QR code Generator
A python script that generates unique QRcode encoding each member's data and accessible from a unique generated url from the sheet of attendees.

## Installation
```
$ git clone https://github.com/IEEE-GUC-SB/event-qrcode-generator.git
$ cd event-qrcode-generator
$ pip install -r requirements.txt
```
## Usage

Firstly, you must get your own API Key so you can encode your data in qrcode urls.
You can get an API Key from 
https://api.imgbb.com

- To get the full flow of the application
```
$ python main.py
```

    
Important Note: If you will edit an online google sheet of yours, Don't forget to log in and register to get your credentials file
and put it inside the event-qrcode-generator folder in your local system.

- Steps to get a credentials file:

1. Go to [Google Developers Console](https://console.cloud.google.com) and click ‘Select a project’ then create a new project. 
2. Enter a name for the project. You may leave ‘Location’ as ‘No Organization’. Press Create.
3. Click on ‘ENABLE APIS AND SERVICES’. 
4. Now enter ‘Google Sheets API’ in the search bar, click on the ‘Google Sheets API’ option, and press ‘ENABLE’.
5. Similarly, search for and enable the ‘Google Drive API’.
6. Click on ‘CREATE CREDENTIALS’.
7. Select ‘Google Sheets API’ in the ‘Select an API’ section, ‘Application Data’ and ‘No, I’m not using them’ in the following questions. Click ‘NEXT’.
8. Enter the display name and name for the service account (any name to your liking).
9. Click on ‘Select a Role’ and select ‘Editor’ under the ‘basic’ section. Press ‘CONTINUE’ then press ‘DONE’.
10. Click on the service account that was just created.
11. Go to the ‘KEYS’ section and click on ‘ADD KEY’. Select ‘Create new key’.
12. Select ‘JSON’ to download the keys in the JSON file format. Click on ‘CREATE’.
13. Now the JSON file will be downloaded to your computer and you can place it in the event-qrcode-generator directory.
14. Remember to share the spreadsheet that you want to edit with the service account you created

- To generate some random data in order to test how your results would exactly be
```
$ python randomQRGenerator
```


## Contributors
- [Abdelrahman Saleh](https://github.com/AbdoRewaished)
- [Amr Mohamed](https://github.com/IrrationalInteger)
- [Helen Mouris](https://github.com/HelenMouris)
