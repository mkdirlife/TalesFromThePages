
# Tales From The Pages 책 추천 블로그
Tales From The Pages 책 추천 블로그

* 목표
    * CRUD 기본적인 블로그 기능 구현
    * 댓글, 대댓글 구현
    * 카테고리 구현

* 사용방법
    1. https://mkdirlife.github.io/TalesFromThePages 로 접속해주세요.
    2. 회원가입을 해주세요. 글을 읽을 수 있고, 작성할 수 있습니다.
    3. 읽고 싶은 Post를 선택해서 읽고, 댓글 을 달아주세요.

* 서비스 URL 정보
    * 실행 URL: https://mkdirlife.github.io/TalesFromThePages
    * blog github repo: https://github.com/mkdirlife/TalesFromThePages

* 개발환경
   * 개발툴 : VSCode
   * 개발프로그램 : HTML, CSS, JavaScript
   * 서비스 배포 : GitHub    

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

* 폴더 구조
```
```

* 코드 컨벤션과 변수 컨벤션
   * 들여쓰기 tab(4칸)
   * 자바스크립트 카멜표기법
   * HTML class명은 '역할-태그명' 형태


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
* 구현 하고자 하는 내용 정리
   1. 댓글, 대댓글 작성 가능
   2. 댓글, 대댓글 삭제 시 삭제되었습니다. 라는 메시지 띄우고 DB에서는 삭제하지 않음.
   3. 삭제되었습니다. 상태에서 한 달 지났을때 자동 삭제
   4. 글삭제 시 에는 모든 댓글, 대댓글 삭제
   5. 글 작성 시 별점 부여 하는 방법 고려 제목에 포함되서 보이도록 할 예정.

* 시퀀스 다이어그램
```mermaid
```




* ERD
    <table>
        <tr>
           <img src="README%20img/ERD.png">
        </tr>
    </table>



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

* 애러와 애러 해결(트러블슈팅 히스토리)
    * HTML 설계

    * 유효성 검사

    * 문장길이 조절로 가독성 확보


* 참고


