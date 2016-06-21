venv:
	virtualenv venv	--no-site-packages --distribute --prompt=surveybot

pip:
	. venv/bin/activate ; pip install -r requirements.txt

install: venv pip
