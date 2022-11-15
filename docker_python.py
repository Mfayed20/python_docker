import time
import docker

client = docker.from_env()

# Get the image
# image = client.images.pull('python:3.7')

# Create a container
# client.containers.run("bulletinboard:1.0")

# list all containers
# for container in client.containers.list():
#     print(container.id)

# list all running containers
# for container in client.containers.list(all):
#     print(container.id)

# list all images
# for image in client.images.list():
#     print(image.id)

# list all volumes
# for volume in client.volumes.list():
#     print(volume.name)

# create a container with a public port and name
# container = client.containers.run("nginx", name="nginx", ports={
#                                   '80/tcp': 80}, detach=True)

# create a container with a public port and name and a volume
# container = client.containers.run("httpd", name="fayed", ports={
#                                   '80/tcp': 8889}, volumes={'C:\httpd-v': {'bind': '/usr/local/apache2/htdocs/', 'mode': 'rw'}}, detach=True)

# wait for 10 seconds
# time.sleep(10)

# close the container
# container.stop()

# remove the container
# container.remove()

# remove the image
# client.images.remove('nginx')

# remove the volume
# client.volumes.remove('nginx')

# remove all containers
# for container in client.containers.list():
#     container.remove()

# remove all images
# for image in client.images.list():
#     client.images.remove(image.id)

# remove all volumes
# for volume in client.volumes.list():
#     client.volumes.remove(volume.name)

# run dockerfile and build an image
# client.images.build(path="C:\Users\mohamed.fayed\Documents\GitHub\docker\dockerfile", tag="bulletinboard:1.0")

# tag an image
# client.images.get('bulletinboard:1.0').tag('mfayed20/bulletinboard:2.0')

# push an image to docker hub
# client.images.push('mfayed20/bulletinboard:2.0')

# run docker swarm
# client.swarm.init()

# list all services
# for service in client.services.list():
#     print(service.name)

# create a service
# client.services.create("nginx", name="nginx", replicas=2)

# remove a service
# client.services.get('nginx').remove()

# remove all services
# for service in client.services.list():
#     service.remove()
