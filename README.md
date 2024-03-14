
# Tales From The Pages 책 소개 블로그
Tales From The Pages 책 소개 블로그

* 목표
    * 블로그 글, 댓글 CRUD 블로그 기능 구현
    * 사이드바 구현(카테고리, tag Cloud, 검색)
    * CBV 구현
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
   * 개발프로그램 : HTML, CSS, JavaScript, DjangoFramework, 무료부트스트랩, TinyMCE

* WBS
```mermaid
gantt
    title TalesFromThePages 도서소개 블로그
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

* URL 구조
```
| URL 패턴                        | 뷰 이름                | 설명                                               
|--------------------------------|----------------------|----------------------------------------------                  
| /admin/                        | -                    | Django 관리자 페이지                                  
| /blog/                         | blog:blog_list       | 블로그 목록                                
| /blog/new/                     | blog:blog_create     | 새로운 블로그 게시물 작성                       
| /blog/<int:pk>/                | blog:blog_detail     | 블로그 게시물 상세                             
| /blog/<int:pk>/update/         | blog:blog_update     | 블로그 게시물 수정                              
| /blog/<int:pk>/delete/         | blog:blog_delete     | 블로그 게시물 삭제                             
| /blog/tag/<str:tag>/           | blog:blog_tag        | 특정 태그를 가진 블로그 게시물 목록                      
| /blog/category/<str:category>/ | blog:blog_category   | 특정 카테고리에 속한 블로그 게시물 목록                       
| /blog/author/<str:username>/   | blog:blog_author     | 특정 작성자의 블로그 게시물 목록                       
| /blog/<int:pk>/comment_create/ | blog:comment_create  | 블로그 게시물에 댓글 작성 기능                             
| /blog/<int:pk>/comment_delete/ | blog:comment_delete  | 블로그 게시물의 댓글 삭제 기능                        
| /accounts/signup/              | accounts:user_signup | 사용자 회원가입                                   
| /accounts/login/               | accounts:user_login  | 사용자 로그인                                       
| /accounts/logout/              | accounts:user_logout | 사용자 로그아웃 기능                                       
| /accounts/profile/             | accounts:profile     | 사용자 프로필                                      
| /tinymce/                      | -                    | TinyMCE 에디터 관련 URL (서드 파티 라이브러리)                   
```


* 폴더 구조
```
django_blog/
│
├── account/                     사용자 인증, 회원가입, 로그인 사용자 계정 관련 기능
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                     사용자 프로필을 업데이트 사진, 소개 메시지, email 필드를 통해 업데이트 기능
│   ├── models.py                    UserProfile class 만들어서 User 모델의 기본필드 유지하고, 추가적인 프로필 정보 정의
│   ├── tests.py
│   ├── urls.py                      view class 와 URL 패턴을 매핑
│   └── views.py                     계정관련 view class / 로그인, 로그아웃, 회원가입, 프로필 수정 등의 기능을 처리
│
├── blog/                        글작성, 삭제, 댓글작성, 삭제 등 블로그 기능 
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                     관리자 페이지에서 모델을 등록하고 관리
│   ├── apps.py
│   ├── forms.py                     블로그 관련 form class 정의, 블로그글 작성, 수정, 댓글 작성, 태그작성, 카테고리 생성
│   ├── models.py                    Blog, Comment, Tag, Category 데이터 구조 정의
│   ├── tests.py
│   ├── urls.py                      view class 와 URL 패턴을 매핑
│   └── views.py                     블로그 글 목록, 상세 페이지, 글 작성, 수정, 삭제 등의 기능을 처리
│
├── config/                     Django 프로젝트의 설정 파일 폴더
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                  프로젝트 설정 파일
│   ├── urls.py                      프로젝트 URL 정의 파일
│   └── wsgi.py
│
├── media/                     사용자 업로드 미디어 파일 저장 폴더
│
├── static/                    CSS, JavaScript 등 정적 파일 저장 폴더
│
├── templates/                 HTML 템플릿 파일 폴더
│   ├── accounts/
│   │   ├── form.html                회원가입 폼
│   │   ├── profile.html             프로필 템플릿
│   │   ├── user_login.html          로그인 템플릿
│   |   └── user_signup.html         회원가입 템플릿
│   ├── blog/
│   │   ├── _comment.html            댓글 작성자의 프로필 사진 표시, 댓글 표시
│   │   ├── blog_delete.html         블로그글 삭제
│   │   ├── blog_detail.html         블로그글 선택시 보여지는 템플릿
│   │   ├── blog_list.html           블로그글 리스트 템플릿(메인페이지)
│   │   ├── comment_delete.html      댓글 삭제
│   |   └── form.html                블로그 글 작성 폼
│   └── base.html               여러 html에 사용할 header, footer 포함한 기본 템플릿
├── db.sqlite3        Django의 기본 데이터베이스 파일
│
└── manage.py         Django 프로젝트를 관리
```

* 에러와 에러 해결(트러블슈팅 히스토리)
    1. 지속적인 model의 변경으로 인한 data 꼬임현상
    2. 유효성 검사
         *  폼 입력후 유효하지 않을 경우 입력한 값들이 사라지는 문제
         *  이미지업로드 시 파일경로 재설정 문제
    3. 이름이 맞지 않아 생기는 오류들로 시간이 많이 소요됨
    4. 부트스트랩 선정후 마음에 안드는 부분들을 미세하기 조정은 하지만 처음부터 잘 고를 필요가 있음
         *  예전스타일 코드, 앞으로 지원하지 않겠다는 오류를 잡을 수 없었음
         *  위치, 사이즈 변경 시 어울리지 않는 문제

* 참고
   1. tinyMCE django 사용방법 참고 - (https://www.tiny.cloud/docs/tinymce/latest/django-zip/)

