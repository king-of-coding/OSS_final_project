프로젝트명
----------
실버셰프의 '그리운 그맛 그맛' 프로젝트는

레시피를 찾아주는 웹사이트 개발에 관한 것입니다.

프로젝트 설명
-------------
app.py 파일에 저희의 웹에서 제공하는 기능들이 프로그래밍 되어있습니다.
py 파일의 구현은 Edamam의 Recipe Search API를 활용했으며,
대표적으로 상위 5개의 레시피를 찾아주는 함수와 검색결과를 초기화해서 다시 다른 메뉴를 검색해볼 수 있는 함수가 구현되어있습니다.
googletranslator api를 사용하여 영어를 한국어로 또는 한국어를 영어로 번역하였고,
이들에 대한 라이센스가 고지되어 있습니다.
static 폴더 내에는 웹의 디자인과 관련된 css 파일과 js 파일 및 사이트에 들어가는 이미지들이 있는 폴더가 있습니다.
이후에 번역의 정확도를 개선하고 레시피의 영양성분에 대한 정보를 제공해주는 기능을 추가해보고 싶습니다.

프로젝트 실행 방법
------------------
파일의 구조는 다음과 같습니다.

![image](https://github.com/king-of-coding/OSS_final_project/assets/144990670/f64a1c77-153b-445a-abad-6b6390101727)





app.py의 실행을 위해서는 다음의 모듈들이 우선적으로 설치될 필요가 있습니다.
- pip install flask
- pip install googletrans==3.1.0a0 (에러가 나지 않는 버전)
- pip install requests
- pip install waitress

API 사용을 위한 app id와 app key는 홈페이지에서 부여받을 수 있습니다.
https://www.edamam.com/

app.py가 flask 어플리케이션 파일이므로 가상환경에서 app.py 실행 후에
http://127.0.0.1:5000 의 주소로 가면 웹 페이지에 접속할 수 있습니다.
