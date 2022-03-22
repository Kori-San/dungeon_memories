#!/bin/bash

# [ Check Python Packages with '$ dpkg' ]
pycheck_pkg(){
    #  ↪ 1: Check if ${arg} is installed
    if dpkg -s "${1}" 1> /dev/null ; then
        #  ↪ 2: Skip ${arg} install
        echo "'$ ${1}' found, skipping install..."
    else
        #  ↪ 2Bis: Install ${arg}
        echo "'$ ${1}' not found, installing ${1}..."
        sudo apt install -q -y "${1}" 1> /dev/null
    fi
}

# [ Check Python Packages with '$ pip list' ]
pycheck(){
    #  ↪ 1: Check if ${arg} is installed
    if pip3 list | grep "${1}" 1> /dev/null ; then
        #  ↪ 2: Skip ${arg} install
        echo "'$ pip3 ${1}' found, skipping install..."
    else
        #  ↪ 2Bis: Install ${arg}
        echo "'$ pip3 ${1}' not found, installing ${1}..."
        pip3 install "${1}"
    fi
}

# > Begin Script
#   ↪ 1: Check if pip3 is installed
if command -v "pip3" 1> /dev/null ; then
    echo "'$ pip3' found, skipping install..."
else
    #  ↪ 1Bis: Install pip3 if not installed
    echo "'$ pip3' not found, installing pip..."
    sudo apt install -q -y pip3 1> /dev/null
fi

#   ↪ 2: Check Dependencies
pycheck "PyYAML"
pycheck_pkg "python3-tk"

#   ↪ 3: Ask if user want to run DuMe
echo "All dependencies were checked, do you want to run the script ? (y/n)"
read -r answer
if [ "${answer,,}" == "n" ] || [ "${answer,,}" == "no" ]; then
    exit 0;
fi

exec ./dume.py
