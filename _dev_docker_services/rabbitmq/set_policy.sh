#!/bin/bash

docker-compose exec -T rabbitmq sh -c "rabbitmqctl set_policy queue-length \".*\" '{\"max-length\":50}' --apply-to queues"