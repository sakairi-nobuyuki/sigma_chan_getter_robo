FROM ubuntu:20.04

### add a non-root user
RUN apt update && apt install sudo
ARG USERNAME=sigma_chan && GROUPNAME=user && UID=1000 && GID=1000 
ARG PASSWD=$USERNAME && HOME=/home/$USERNAME

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID -G sudo $USERNAME && \
    echo $USERNAME:$PASSWD | chpasswd && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USERNAME
WORKDIR $HOME


### install python
RUN sudo apt install --no-install-recommends -y python3.8 python3-pip python3.8-dev default-libmysqlclient-dev build-essential

### install poetry
RUN sudo apt install --no-install-recommends -y curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
ENV PATH $HOME/.poetry/bin:$PATH


### install python modules
#EXPOSE 80

COPY . $HOME
#RUN poetry config virtualenvs.create false && \
#    poetry install --no-interaction --no-ansi
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

ENV PATH $HOME/.local/bin:$PATH

