
# 스프링 부트 1강

## 1. 프로젝트 생성

 - https://start.spring.io/ 에서 설정 후 프로젝트다운로드
 - 설정:
  ![image](./화면%20캡처%202024-09-01%20184357.png)


## 2. 프로젝트 오픈

 - 인텔리제이 -> open project-> build.gradle 을 open

## 3. 스프링 부트의 mvc 패턴

 - m: db와 상호작용하며 비즈니스 로직 수행 
 - v: 사용자에게 보여지는 화면
   - viewResolver가 controller class 가 반환한 이름을 실제 html 등의 파일과 매핑한다 
 - c: 사용자 요청에 따른 적절한 view 를 반환한다
   - @Controller 어노테이션을 단 class를 실행.
   - 웹요청을 처리하고 원하는 data값을 모델에 담아서 view에 전달하는 중간다리 역할 

## 4. 파일 build 및 서버에서 프로젝트 실행하기

 - project의 gradlew 에서 build 실행 ```./gradlew build```
 - ``` cd build/libs```  이동 
 - ```ls -arlth``` 로 만들어진 파일 이름 확인 
 - ```java -jar ${url이름.jar}``` jar 파일 실행 