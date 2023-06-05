FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

# Get the latest everything
RUN apt-get -y update && \
    apt-get -y dist-upgrade

RUN apt-get install -y \
    hydra \
    john \
    metasploit-framework \
    nmap \
    sqlmap \
    wfuzz \
    exploitdb \
    nikto \
    commix \
    hashcat \
    # Wordlists
    wordlists \ 
    cewl

# Install Other tools
RUN apt-get install -y \
    gdb

# Install utils
RUN apt-get install -y \
    netcat-traditional \
    file \
    vim \
    git

# Setup gdb-peda
RUN git clone https://github.com/longld/peda.git ~/peda && \
    echo "source ~/peda/peda.py" >> ~/.gdbinit

CMD ["/bin/bash"]
