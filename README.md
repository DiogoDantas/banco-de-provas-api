# banco-de-provas-api

### Instalando Docker no Linux

`
$ sudo wget -qO- https://get.docker.com/ | sh
`

### Configuração pós-instalação no Linux

`
$ sudo usermod -aG docker $USER
`

> Provavelmente você deverar reiniciar a máquina após o uso desse comando

### Instalando o docker compose

`
$ pip install docker-compose
`

### Buildando

`
$ docker-compose build
`

### Subindo os containers

`
$ docker-compose up
`