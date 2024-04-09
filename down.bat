curl -s -L -o setup.py https://gitlab.com/chamod12/iperius_win-10_github_rdp/-/raw/main/setup.py
curl -s -L -o iperius.exe "https://www.iperiusremote.com/dsir.aspx?file=IperiusRemote_Setup.exe&v=4&a=64"
curl -s -L -o show.bat https://gitlab.com/chamod12/iperius_win-10_github_rdp/-/raw/main/show.bat
start "" "iperius.exe"
python setup.py
