docker-build:
	bash shell/docker-build.sh

docker-push:
	bash shell/docker-build.sh push

# delete:
# 	-kubectl delete -f deployment/k8s/template-matching-summary.yml
# 	-kubectl delete -f deployment/k8s/template-matching-summary-server.yml

run:
	# client run, not server
	bash shell/run.sh microservice-watch
