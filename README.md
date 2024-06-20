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
최종 수정본인 silverchef 폴더를 다운받아 사용하시면 됩니다.

실행을 위한 파일의 구조는 다음과 같습니다.

![image](https://github.com/king-of-coding/OSS_final_project/assets/144990670/f64a1c77-153b-445a-abad-6b6390101727)





1. python이 설치되어있는지 먼저 확인 후에
2. 가상환경을 생성하고 활성화합니다. ex) anaconda
3. app.py의 실행을 위해서 필요한 다음의 패키지들을 설치합니다.
- pip install flask
- pip install googletrans==3.1.0a0 (에러가 나지 않는 버전)
- pip install requests
- pip install waitress
4. API 사용을 위한 app id와 app key는 홈페이지에서 부여받을 수 있습니다.
https://www.edamam.com/
5. app.py가 flask 어플리케이션 파일이므로 가상환경에서 app.py 실행 후에
http://127.0.0.1:5000 의 주소로 가면 웹 페이지에 접속할 수 있습니다.
6. app.py 최초 실행 시에 보안 관련 팝업에 대해서 허용을 해줘야 웹에 접속이 가능합니다.


프로젝트에 사용된 이미지의 출처
-------------------------
- banner1.png (독거노인종합지원센터) : https://edu.1661-2129.or.kr/html/images/main/logo_m1200.jpg
- background.jpg(배경화면 음식 사진 freepik) : https://img.freepik.com/free-photo/top-view-table-full-food_23-2149209265.jpg?t=st=1718881640~exp=1718885240~hmac=095ecff47c28b2cfdbe26195a958f348336faa9c80e48ab8e14e52c719e7e559&w=996
- banner2.png (한국노인종합복지관협회) : https://lh6.googleusercontent.com/proxy/iGbJiYOb2irnntgnHsGbxVIlRDM_wabzvXMjbTZaPtimdcqg7a2m8U1Xki23vU0k0Rz3cZubI7QMYNuO9n3pWS9MfrwKPsxCKg
