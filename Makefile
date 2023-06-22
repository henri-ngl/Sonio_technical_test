init:
	docker-compose up -d;
	pip install -r requirements.txt;

run:
	python main.py