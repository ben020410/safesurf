<p align="center">
  <p align="center">
    <img src="https://github.com/user-attachments/assets/d7a2fc93-04e8-4a27-a995-9140fcd738cd" width="300">
  </p>
  <h1 align="center">🏄 Safesurf: 악성 URL 진단 서비스 ✅</h1>
  <p align="center">
    <h3 align="center">2024-2 서울대학교 AI빅데이터기초/빅데이터개론I 기말 프로젝트</h3>
  </p>
  <p align="center">
    <a> 김준휘, 나세민, 문희주, 박하연, 방준혁, 서예린, 윤정원, 이상은(팀장), 이정균, 이정원 </a>
  </p>
</p>
<br>

## :sparkles: 소개
사용자가 URL을 입력하면, 사전 학습된 AI 분류 모델을 통해 악성 URL 여부를 판단해 알려주는 서비스입니다. <br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/261ea884-6e4c-49f3-9550-91b773dc5010" width="800"/>
</p>
<br>

## :hammer_and_wrench: 설치
`python` 및 `pip`가 설치되어 있지 않다면 설치 후 진행합니다([설치 방법](https://heytech.tistory.com/318)).

### 1. git을 처음 접하는 경우(사용해본 적이 있다면 다음 단계로)
터미널에서 다음 명령을 실행합니다. <br>
```bash
git --version
```
결과로 버전 정보가 출력되면, git이 이미 설치된 것입니다(예시: `git version 2.34.1`). <br>
설치되지 않은 경우 [git 공식 사이트](https://git-scm.com/)에서 다운로드하여 설치합니다. <br>
<br>

### 2. 저장소 복제
**복제할 폴더**에서 터미널을 실행합니다. (예를 들어, Windows를 사용하는 경우 복제할 폴더에서 우클릭 후 '명령 프롬프트' 열기) <br>
또는 임의의 경로에서 터미널을 실행한 후 다음 명령을 입력해도 됩니다. <br>
```bash
cd <복제할 폴더의 경로>
```
이제 터미널에서 다음 명령을 실행합니다. <br>
```bash
git clone https://github.com/ben020410/safesurf.git
```
이 명령은 `safesurf` 레포지토리를 복사하여 현재 경로에 `safesurf` 폴더를 생성합니다. <br>
<br>

### 3. 가상 환경 생성 및 활성화
2.에서 복제한 `safesurf` 폴더에서 터미널을 열고, 다음 명령을 입력합니다.
**(주의할 점: `safesurf` 폴더에서 명령어를 실행하지 않는다면 추후 오류가 발생할 수 있습니다.)** <br>
```bash
python -m venv venv
```
위 명령은 `safesurf` 폴더 내에 `venv`라는 이름의 가상 환경 폴더를 생성합니다. <br>
<br>

그 다음, 가상 환경을 활성화합니다(Windows와 Linux/Mac의 명령어가 다름에 주의). <br>

- Windows - [만약 오류가 발생한다면?](https://github.com/ben020410/safesurf/issues/1)
```bash
venv\Scripts\activate
```
- Linux/Mac
```bash
source venv/bin/activate
```
활성화되면, 터미널 프롬프트가 `(venv)`로 시작하게 됩니다. <br>
<br>

### 4. 필요한 패키지 설치
프로젝트에서 필요한 라이브러리를 설치합니다. <br>
`safesurf` 폴더에서 터미널을 열고, 다음 명령을 입력합니다(마찬가지로, 다른 폴더에서 명령어를 실행하면 오류가 발생할 수 있습니다). <br>
```bash
pip install -r requirements.txt
```
(참고로, 가상 환경을 실행한 후 패키지를 설치하기 때문에 이 프로젝트를 진행할 때만 패키지가 사용되고, 로컬 환경의 다른 패키지와의 충돌이 발생하지 않습니다.) <br>
<br>

### 5. 가상 환경 비활성화
이제 설치가 모두 끝났습니다. 터미널에서 실행했던 가상 환경을 비활성화합니다. <br>
```
deactivate
```
<br>

## :arrow_forward: 로컬에서 실행
위 설치 단계를 마쳤다면, 로컬 환경에서 서비스를 실행할 수 있습니다. <br> <br>
우선 가상 환경을 활성화합니다.
- Windows
```bash
venv\Scripts\activate
```
- Linux/Mac
```bash
source venv/bin/activate
```
<br>

이제 `project` 폴더의 `app.py` 파일을 실행하면 Flask 서버가 가동되며 html 페이지로 연결됩니다. 서버를 중지하고 싶다면 `Ctrl`+`C` 키를 터미널에 입력합니다. <br>
<br>
테스트 후에는 반드시 가상 환경을 비활성화하여 마무리합니다.
```bash
deactivate
```
