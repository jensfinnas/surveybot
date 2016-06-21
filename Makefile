venv:
	virtualenv venv	--no-site-packages --distribute --prompt=surveybot

pip:
	. venv/bin/activate ; pip install -r requirements.txt

install: venv pip

docker-build:
	docker build -t surveybot .

docker-run:
	docker run -it surveybot

deploy:
	heroku container:push worker -a askchartbot
