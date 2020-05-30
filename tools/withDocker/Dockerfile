FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y tzdata
RUN apt-get install -y vim
RUN apt-get install -y file 
RUN apt-get install -y binutils
RUN apt-get install -y build-essential 
RUN apt-get install -y cmake clang libssl-dev bsdmainutils 
RUN apt-get install -y foremost binwalk socat wget gdb
RUN apt-get install -y strace ltrace curl
RUN apt-get install -y python3.6
RUN apt-get install -y python3.6-dev
RUN apt-get install -y python3.6-venv
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN ln -s /usr/bin/python3.6 /usr/local/bin/python3
#install python
RUN pip3 install opencv-python requests pwntools 

#install java
RUN apt-get update
RUN apt-get install -y openjdk-8-jre
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y git zip unzip exiftool

RUN mkdir /root/tools

#length extension attack
WORKDIR /root/tools
RUN git clone https://github.com/bwall/HashPump.git
RUN apt-get install g++ libssl-dev
WORKDIR /root/tools/HashPump
RUN make && make install


#install dex2jar()
WORKDIR /root/tools
RUN wget  https://sourceforge.net/projects/dex2jar/files/latest/download
RUN unzip download 
RUN rm download
RUN chmod +x dex2jar-2.0/*

#install jadx (java decompiler)
WORKDIR /root/tools
RUN git clone https://github.com/skylot/jadx.git
WORKDIR /root/tools/jadx
RUN ./gradlew dist

#install checksec
WORKDIR /root/tools
RUN wget https://github.com/slimm609/checksec.sh/archive/1.6.tar.gz
RUN tar zxvf 1.6.tar.gz
RUN cp checksec.sh-1.6/checksec /bin/checksec.sh

RUN apt-get install -y python-dev libffi-dev build-essential virtualenvwrapper
RUN pip3 install virtualenvwrapper

RUN echo "if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then" >> /root/.bashrc
RUN echo "    export WORKON_HOME=$HOME/.virtualenvs"           >> /root/.bashrc
RUN echo "    source /usr/local/bin/virtualenvwrapper.sh"      >> /root/.bashrc
RUN echo "fi">>/root/.bashrc

RUN bash -c "source /root/.bashrc && source /usr/local/bin/virtualenvwrapper.sh  &&  mkvirtualenv --python=$(which python3) angr && pip install angr"

CMD ["/bin/bash"]
