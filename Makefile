destroy-cluster:
	k3d cluster delete valor-stats

create-cluster:
	k3d cluster create valor-stats --api-port 127.0.0.1:6443 \
		-p 80:80@loadbalancer \
		-p 443:443@loadbalancer \
		--registry-create valor-stats-registry
	k3d kubeconfig get valor-stats >> ~/k3d/kubeconfig
	export KUBECONFIG=/tmp/kubeconfig

apply-deployments:
	kubectl apply -f kubernetes/deployments/valor-stats.yaml

reapply-deployments:
	kubectl rollout restart deployment valor-stats-development

push-image-to-local-registry:
	k3d image import valor-stats -c valor-stats

build:
	docker build . -f./Dockerfile.dev -t valor-stats --no-cache