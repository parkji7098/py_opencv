# opencv 환경설정
## 설치

//우분투, 터미널에 입력
//전역에서 사용되는 pip를 미리 업그레이드
$ sudo -H pip3 install --upgrade --ignore-installed pip setuptools

//만약 pip3이 설치되어 있지 않으면 아래 명령으로 설치
$ sudo apt install python3-pip

// matplotlib 에 대비하여 tk 모듈 설치
$ sudo apt-get update
$ sudo apt-get install python3-tk

//가상환경 설정
$ python -m venv venv
//pip 업그레이드
$ pip install –upgrade pip

//윈도우 활성화
$ .\venv\Scripts\Activate.ps1

//우분투 활성화
$ source ./venv/bin/activate

//버전 및 설치 확인 (pip의 경로가 가상환경 경로와 일치해야함)
$ pip -V

// 이하 가상환경 안에서
// opencv 설치 (파이썬 3.10 이상)
$ pip install opencv-contrib-python

// 파이썬 3.6 이하
$ pip install opencv-contrib-python==3.4.1.15

// matplotlib 설치
$ pip install matplotlib
