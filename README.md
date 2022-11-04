# opencv 환경설정
## 설치

#설치

//우분투
$ sudo apt-get update

//만약 pip3이 설치되어 있지 않으면 아래 명령으로 설치
$ sudo apt install python3-pip

// matplotlib 에 대비하여 tk 모듈 설치
$ sudo apt-get install python3-tk

//우분투, 터미널에 입력
//전역에서 사용되는 pip를 미리 업그레이드
$ sudo -H pip3 install --upgrade --ignore-installed pip setuptools

//$ sudo pip3 install --upgrade pip

$ python3 -m venv venv
$ source ./venv/bin/activate

//버전 및 설치 확인 (pip의 경로가 가상환경 경로와 일치해야함)
(가상환경) $ pip -V
(가상환경) $ pip install –upgrade pip

//파이썬 버전 3.10으로 설치

//apt 업데이트 및 업그레이드
$ sudo apt update
$ sudo apt upgrade
$ sudo apt dist-upgrade

//새 저장소 추가
$ sudo apt install software-properties-common -y
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

$ sudo add-apt-repository ppa:deadsnakes/ppa

//파이썬 3.10 설치
$ sudo apt install python3.10
$ sudo apt-get install python3.10-venv
//$ sudo apt install python3-pip

$ sudo apt-get install python3.10-tk


//설치확인
$ python3.10 -V
$ pip3 -V
//$ pip3.10 -V

//가상환경 생성
$ python3.10 -m venv venv

//메모장으로 .bashrc 파일을 열어 가장 아래에 내용 추가
$ sudo gedit ~/.bashrc
// 추가할 내용 (저장)
alias python3=’python3.10’

//커널에 적용
$ source ~/.bashrc
//확인
$ python3 -V




//윈도우

//가상환경 설정
$ python -m venv venv
//활성화
$ .\venv\Scripts\Activate.ps1

//pip 업그레이드
(가상환경) $ pip install –upgrade pip

//버전 및 설치 확인 (pip의 경로가 가상환경 경로와 일치해야함)
(가상환경) $ pip -V


//opencv 및 관련 패키지 설치

// 이하 가상환경 안에서
// opencv 설치 (파이썬 3.10 이상)
$ pip install opencv-contrib-python

// 파이썬 3.6 이하
$ pip install opencv-contrib-python==3.4.1.15



// matplotlib 설치
$ pip install matplotlib

//matplotlib이 동작안할때 (에러메시지에 xcb 어쩌구..)
(가상환경) $ pip install opencv-python-headless


// pafy, youtube-dl 설치
$ pip install pafy youtube-dl
