# Julie-Data
# Remake of Julie-Julie with underlying sqlite3 database

# This is the start of a whole new architecture that is intended to be a kind of command shell with memory.  The idea is to make the computer more useful by saving actions and parameters for future use.  I'm starting off with sqlite 3 as my database, but I may switch to a graph database at some point.  So I will try to make this as database independant (or flexible) as possible.

# Initial setup:
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





