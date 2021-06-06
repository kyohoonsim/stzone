# SDE-stzone
원활한 태깅을 위한 스트라이크 존 제공 프로그램

## 설치 필요한 패키지
- pyqt5: `pip install pyqt5`
- pyinstaller: `pip install pyinstaller`

## 실행파일 생성 명령어
```
pyinstaller --onefile --noconsole --icon=icon.ico --add-data="icon.ico;." -n="STZone v1.0" stzone.py
```