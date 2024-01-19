dev:
    poetry run python3 bot.py

build:
    docker build . -t chand1012/aurora

deploy:
    fly deploy --app aurorachat-dev

deploy-prod:
    fly deploy --app aurorachat

proxy:
    fly proxy 5432:5432 -a aurora-dev-db

proxy-prod:
    fly proxy 5432:5432 -a aurora-db
