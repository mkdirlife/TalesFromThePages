
# Tales From The Pages 책 소개 블로그
Tales From The Pages 책 소개 블로그

* 목표
    * CRUD 기본적인 블로그 기능 구현
    * 사이드바 구현(카테고리, tag Cloud, 검색)
    * 페이징, 댓글, 대댓글 구현

* 사용방법
    1. https://mkdirlife.github.io/TalesFromThePages 로 접속해주세요.
    2. 회원가입을 해주세요. 글을 읽을 수 있고, 작성할 수 있습니다.
    3. 읽고 싶은 Post를 선택해서 읽고, 댓글 을 달아주세요.

* 서비스 URL 정보
    * 실행 URL: https://mkdirlife.github.io/TalesFromThePages
    * blog github repo: https://github.com/mkdirlife/TalesFromThePages

* 개발환경
   * 개발툴 : VSCode
   * 개발프로그램 : HTML, CSS, JavaScript, Django

* WBS
```mermaid
gantt
    title TalesFromThePages 도서추천 블로그
    dateFormat  YYYY-MM-DD
    section 계획
    프로젝트 범위 정의        :    des1, 2024-03-07, 1d
    section 설계
    와이어프레임 작성         :    des2, 2024-03-08, 1d
    section 개발
    기능 개발                :     dev1, after des1, 3d
    디자인                :        dev2, 2024-03-10, 2d
    section 테스트
    테스트                  :     tes1, 2024-03-09, 3d
    최종테스트              :     tes2, 2024-03-12, 12h
    section 배포
    배포 준비               :     dep1, after tes2, 12h
```

* 화면 정의서
    <table>
        <tr>
            <th>메인화면</th>
            <th>설명</th>
        </tr>
        <tr>
            <td width="70%">
               <img src="README%20img/[Blog 프로젝트]blog_list.jpg">
            </td>     
            <td>
                <ul>
                    <li>로그인, 로그아웃 구현</li>
                    <li>검색 기능 구현</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td width="70%">
               <img src="README%20img/[Blog 프로젝트]blog_detail.jpg">
            </td>              
            <td>
                <ul>
                    <li>카테고리 구현</li>
                    <li>댓글, 대댓글 구현</li>
                    <li>tag 조회 구현</li>                   
                </ul>
            </td>
        </tr>       
    </table>

* 흐름도
```mermaid
graph LR
    A[사용자] --> B{회원 로그인}
    B --> |Yes| C[블로그 기능]
    C --> D[글 작성/삭제]
    C --> E[댓글 작성/삭제]
    C --> F[검색 기능]
    F --> G[텍스트/태그/카테고리/ID 검색]
    C --> H[사이드바]
    H --> I[최근 블로그 글]
    H --> J[태그 클라우드]
    D --> K[데이터베이스]
    E --> K[데이터베이스]
    G --> K[데이터베이스]
    I --> K[데이터베이스]
    J --> K[데이터베이스]
    B --> |No| L[로그인 필요 알림/글목록만 조회]
    A --> M[회원가입]
    M --> K[데이터베이스]
```

* ERD
    <table>
        <tr>
           <img src="README%20img/ERD.png">
        </tr>
    </table>

* 폴더 구조
```
django_blog/
│
├── account/   사용자 인증, 회원가입, 로그인 사용자 계정 관련 기능
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── blog/      글작성, 삭제, 댓글작성, 삭제 등 블로그 기능 
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── config/   Django 프로젝트의 설정 파일 폴더
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/   사용자 업로드 미디어 파일 저장 폴더
│
├── static/   CSS, JavaScript 등 정적 파일 저장 폴더
│
├── templates/   HTML 템플릿 파일 폴더
│
├── db.sqlite3   Django의 기본 데이터베이스 파일
│
└── manage.py   Django 프로젝트를 관리
```

* 에러와 에러 해결(트러블슈팅 히스토리)
    1. 지속적인 model의 변경으로 인한 data 꼬임현상
    2. 유효성 검사(폼 입력후 유효하지 않을 경우 입력한 값들이 사라지는 문제, 특히 이미지업로드 시 파일경로 재설정 문제)
    3. 이름이 맞지 않아 생기는 수 많은 오류들(긴 시간을 헤메게 하는 원인이었음)
    4. 부트스트랩 선정후 마음에 안드는 부분들을 미세하기 조정은 하지만 처음부터 잘 골라야 한다고 생각이 듬.(예전스타일 코드, 위치, 사이즈 변경 시 어울리지 않는 문제)
    


* 참고


