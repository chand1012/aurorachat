dev:
    overmind start

build:
    docker build . -t chand1012/aurora

deploy:
    fly deploy --app aurora-dev

deploy-prod:
    fly deploy --app aurora-prod

proxy:
    fly proxy 5432:5432 -a aurora-dev-db

proxy-prod:
    fly proxy 5432:5432 -a aurora-prod-db
