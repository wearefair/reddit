.PHONY: image

docker-image:
	docker build -t skurtinc/reddit/backend:latest .
docker-run:
	docker run -d -p 5000:5000 --name reddit-backend skurtinc/reddit/backend
docker-stop:
	docker kill reddit-backend
test:
	env ENV=test python -m pytest tests/
