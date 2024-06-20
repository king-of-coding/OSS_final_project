본 프로젝트는 레시피를 찾아주는 웹사이트 개발에 관한 것입니다.

app.py 파일에 저희의 웹에서 제공하는 기능들이 프로그래밍 되어있습니다.
대표적으로 상위 5개의 레시피를 찾아주는 함수와 검색결과를 초기화해서 다시 다른 메뉴를 검색해볼 수 있는 함수가 구현되어있습니다.
언어는 파이썬을 사용하고 있고 다음의 모듈들이 우선적으로 설치될 필요가 있습니다.
- pip install flask
- pip install requests
- pip install watress
- pip install googletrans

googletranslator api를 사용하여 영어를 한국어로 또는 한국어를 영어로 번역하였고 다음의 라이센스를 따른다.
The MIT License (MIT)

Copyright (c) 2015 SuHun Han

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

static 폴더 내에는 웹의 디자인과 관련된 css 파일과 js 파일 및 사이트에 들어가는 이미지들이 있는 폴더가 있습니다.
