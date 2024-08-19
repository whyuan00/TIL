
발상
 - 순회를 최소화하기 위해 team 기준으로 병사들을 묶어 저장하기
구현

 - hire: 5개의 team에 따른 dict 5개 생성, 각 dict에 dict_1[id] = Score 로 저장
  
 - dict 5개 순회해서 fire: dict_n[id] = 0

 - updateS: dict 5개 순회해서 dict_n[id] = score
  
 - updateT: 해당 팀의 dict 에서 score 변경

 - updateS: 해당 팀의 dict에서 value, key 기준으로 정렬해서 첫번째 인덱스 key 반환 