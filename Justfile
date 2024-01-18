dev:
    poetry run python3 bot.py

build:
    docker build . -t chand1012/aurora

deploy:
    fly deploy

proxy:
    fly proxy 5432:5432 -a aurora-database
