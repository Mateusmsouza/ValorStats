create-cluster:
	k3d cluster create valor-stats

deploy-cluster:
	kubectl apply -f kubernetes/deployments/valor-stats.yaml

build:
	docker build . -f./Dockerfile.dev -t valor-stats-local --no-cache