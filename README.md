# python-youtube-downloader
![python-version](https://img.shields.io/badge/python-v3.9-blue)<br>
Python tool for automating YouTube videos converting to mp3 and downloading.
## Arguments
- **-h/--help** - Get help with using the tool
- **-u/--url** - URL for the video to be converted and downloaded
- **-f/--csv-file** - Path to csv file containing the urls to be converted and downloaded
- **-b/--bin-location** - Path to chrome .exe file
- **-c/--chrome-driver** - Path to chrome driver
- **-d/--download_path** - Path to files to be downloaded to locally
## Run Example
```bash
git clone https://github.com/galbirk/python-youtube-downloader.git
cd python-youtube-downloader
python -m pip install -r requirements.txt
python yt_downloader.py -f "/path/to/csv"
```
**Notice!** The chrome driver in this repositry is for chrome version 87<br>
### Example for csv file
## ![csv](images/csv.png)

## Author Information

<b>Gal Birkman, DevOps Engineer.</b><br>
<b>Email:</b> galbirkman@gmail.com<br>
<b>GitHub:</b> https://github.com/galbirk