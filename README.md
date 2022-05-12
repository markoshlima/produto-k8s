# produto-k8s

**Pre-Requisites** <br />
Python 3.7.10 <br />
Flask 2.0.3 <br />
pip 20.2.2 <br />
Docker 20.10.7

**Install** <br />
pip install pipenv <br />
pipenv --three <br />
pipenv install flask <br />
pipenv install marshmallow

**RUN** <br />
./bootstrap.sh
    
**Build docker container** <br />
docker build . -t markoshlima/produto-k8s<br />
docker build . -t markoshlima/produto-k8s --platform linux/amd64 //EKS

**Start docker container** <br />
docker run -it -p 5002:8080 -d markoshlima/produto-k8s

**Logs docker container** <br />
docker logs [img]

**Inspect docker image** <br />
docker inspect [img] <br />
docker exec -it [img] /bin/bash

**Stop docker container** <br />
docker stop [img]