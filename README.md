# "너는" 웹서비스

## 세팅 방법

- MacOS 기준
- python 3.5 이상
- pyenv 설치 권장

```
# 프로젝트 클론
cd ~/projects
git clone git@gitlab.com:youareapp/service.git
# 해당 프로젝트 폴더로 이동
cd ~/projects/service

# python 설정
brew install pyenv pyenv-virtualenv  # 설치시 안내에 따라 .bash_profile에 init 설정을 추가해야함
pyenv install 3.5.2  # 파이썬 인스톨
pyenv virtualenv 3.5.2 3.5.2-ur-service  # 가상환경 만들기
pyenv local 3.5.2-ur-service  # 해당 폴더로 접근시 자동으로 가상환경 활성화
pip install setuptools pip --upgrade
pip install -r app/requirements.txt

# 개발 중 프로젝트 업데이트 사항 따라가기
pip install -r requirements.txt --upgrade
python manage.py migrate

# Local 서버 실행
python manage.py runserver
```