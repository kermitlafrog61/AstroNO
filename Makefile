up:
	docker compose -f docker/docker-compose.yml up -d
bash: 
	docker compose -f docker/docker-compose.yml exec -it $(CON) bash
