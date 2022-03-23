# Julie-Data
# Remake of Julie-Julie with underlying sqlite3 database

# This is the start of a whole new architecture that is intended to be a kind of command shell with memory.  The idea is to make the computer more useful by saving actions and parameters for future use.  I'm starting off with sqlite 3 as my database, but I may switch to a graph database at some point.  So I will try to make this as database independant (or flexible) as possible.

# Initial setup:
# I use miniconda for virtual environments. You will need this for pyaudio as pip can't install it. Anaconda also works.
# Here's the 64 bit Linux installer you need. It will download automatically: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh Here's the link to miniconda documentation: https://docs.conda.io/en/latest/miniconda.html

# You don't need to know much about this to run the commands in my instructions, but you should understand that you are segregating python packages for this application by creating a virtual environment -- then activating it.

# Let's start by setting up a new base directory and conda environment:
# If the ~/Code directory doesn't exist, create it.
# I create all my projects off the Code directory.
mkdir -p ~/Code
cd !$
git clone git@github.com:MikeyBeez/Julie-Data.git
cd Julie-Data
git status
git pull
conda create --name Julie-Data python=3.6.2
# either do this:
conda activate Julie-Data
# or do this:
# I always setup direnv to automatically switch to the correct environment when in the project directory.  I have a video showing this on my YouTube channel:
https://www.youtube.com/watch?v=mkqAILBSp1U&t=707s
# The following two lines only work after direnv is installed and configured:
echo 'layout anaconda Julie-Data' > .envrc
direnv allow
# You may need to update conda's base:
conda update -n base -c defaults conda
# This should be done occassionally as a security patch to get most recent versions of base packages.
conda install pyaudio
pip3 install --user --force-reinstall --ignore-installed --no-binary :all: gTTS
# Test the installation of gtts:
gtts-cli 'hello' --output hello.mp3 |mpg123 hello.mp3
# You may need the full path to gtts-cli ~/.local/bin/gtts-cli
# You should hear your computer say "hello."
# If it doesn't check your sound settings.
# Get git up to date:
git status
vim .git ignore
# add the file hello.mp3 to .git ignore then add .gitignore to the repository
git add .gitignore
git commit -a
# add a commit message
git push
git status

# Next is speech to text (STT):

# Install the alphacep's vosk-api software from github. The command is 
cd ~/Code
git clone https://github.com/alphacep/vosk-api

# I always clone this package so I have the example files handy. cd to where you store code. I use ~/Code.  If you don't have it, make it.

mkdir ~/Code cd ~/Code

# for SSH use:

git clone git@github.com:alphacep/vosk-api.git

# Or for HTTPS use:

git clone https://github.com/alphacep/vosk-api.git

# Documentation for vosk is on their website: https://alphacephei.com/vosk/ Always read the documentation when installing a package. Things change, and they may have updated their proceedures whil I may not have updated mine.

pip3 install vosk==0.3.10

pip list

# Now get and install the kaldi model used by vosk. You can find it at https://alphacephei.com/vosk/models Download the vosk-model-en-us-0.22.  This is the English model with the lowest error rates.  Check the error rates.  There may be a new better model.  This is a large file.  It may take quite a while to download.  On my system downloads go into ~/downloads/

cd ~/Downloads 
unzip vosk-model-en-us-0.22 
mv ~/Downloads/vosk-model-en-us-0.22 ~/Code/Julie-Data/
cd ~/Code/Julie-Data
mv vosk-model-en-us-0.22 model-en/
# Let's test our vosk installation:
python ../vosk-api/python/example/test_microphone.py
# Start speaking.  You should see your words appear as text.  Make sure your microphone is turned on in settings sound.









