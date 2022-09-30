# 🗂️ Django Project (Pair programming)

> 일시 : 2022-09-30
>
> 내용 : 영화 리뷰 커뮤니티 서비스의 CRUD 기능과 페이지를 구현
>
> 팀 구성 : 3인 1팀 (2-13 윤효근, 이동근, 이수경)



![220930](https://user-images.githubusercontent.com/106902415/193230301-093efd52-de39-4f27-a26d-78359cd39354.gif)



---



## ✒️ 실습 후기

- 게시글 글 번호에 DB의 pk 가 출력되게 만들면 DB가 변경될 때마다 글 번호가 갱신되지 않기 때문에,  `forloop.counter` 를 활용해서 DB가 변경되어도 오름차순 글 번호 순서가 유지될 수 있는 기능을 추가 구현했습니다
- `<select>` 와 `<option>` 태그를 활용해서 DB에 별점을 저장하고 불러올 수 있도록 추가 구현했습니다