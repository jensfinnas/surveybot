venv:
	virtualenv venv	--no-site-packages --distribute --prompt=surveybot

pip:
	. venv/bin/activate ; pip install -r requirements.txt

install: venv pip

run:
	. venv/bin/activate ; python example.py

docker-build:
	docker build -t surveybot .

docker-run:
	docker run -it surveybot

deploy:
	git push https://git.heroku.com/askchartbot.git
