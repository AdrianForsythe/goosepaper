<p align=center><img align=center src='docs/goose.svg' width=600 /></p>
<h6 align=center>a daily newsfeed delivered to your remarkable tablet</h6>

![GitHub repo size](https://img.shields.io/github/repo-size/j6k4m8/goosepaper?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/j6k4m8/goosepaper?style=for-the-badge)
![This repo is pretty dope.](https://img.shields.io/badge/pretty%20dope-%F0%9F%91%8C-blue?style=for-the-badge) ![This repo is licensed under Apache 2.0](https://img.shields.io/github/license/j6k4m8/goosepaper?style=for-the-badge)

## what's up

goosepaper is a utility that delivers a daily newspaper to your remarkable tablet. that's cute!

you can include RSS feeds, Twitter feeds, news articles, wikipedia articles-of-the-day, weather, and more. I read it when I wake up so that I can feel anxious without having to get my phone out.

## installation

### dependencies:

this tool uses `weasyprint` to generate PDFs. You can install everything you need with `pip3 install -r ./requirements.txt` from this repo, but you may need these prerequisites before starting.

more details [here](https://weasyprint.readthedocs.io/en/latest/install.html).

#### mac:

```shell
brew install cairo pango gdk-pixbuf libffi
```

#### ubuntu-flavored:

```shell
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

#### windows:

[Follow these instructions carefully](https://weasyprint.readthedocs.io/en/latest/install.html#windows).

## and then:

```shell
pip3 install -r ./requirements.txt
```

Check out `main.py` for an example usage!

## usage

execute easily using [frof](https://github.com/j6k4m8/frof):

```shell
frof remarkable.frof
```

You can add this to a crontab to run daily in the morning.

### slightly more annoying, without frof:

```shell
mkdir -p temp
python3 main.py > temp/test.html
wkhtmltopdf temp/test.html temp/test.pdf
open temp/test.pdf
```

### p2r

You'll need a [`p2r` of some variety](https://github.com/GjjvdBurg/paper2remarkable) installed; this tool syncs documents to your tablet. (You can also use this without p2r, and sync the PDF yourself.) I'd recommend cloning the p2r repo and building with docker:

```shell
git clone https://github.com/GjjvdBurg/paper2remarkable
cd paper2remarkable
docker build -t p2r .
```

## yes but pardon me — i haven't a remarkable tablet

Do you have another kind of tablet? You may generate a print-ready PDF which you can use on another kind of robot as well!

```shell
frof frofs/pdf-only.frof
```

## thank you, but i prefer not to install `frof`!

that is ok! you can still use this like a Python library, and move the resulting HTML or PDF onto your device of choice.

# More Questions, Infrequently Asked

## very nice! may i have it in comic sans?

yes! you may do anything that you find to be fun and welcoming :)

Check out the `styles.Styles` enum in the goosepaper library. You will find there what you seek.

## do all dogs' names start with the letter "B"?

I do not think so, but it is a good question!

## may i use this to browse twitter?

yes you may! you can add a list of usernames to the feed generator and it will make a print-ready version of twitter. this is helpful for when you are on twitter on your laptop but wish you had Other Twitter as well, in print form.

# You May Also Like...

-   [remailable](https://github.com/j6k4m8/remailable): Email PDF documents to your reMarkable tablet
