-- ANIMAL_INS 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. 
-- ANIMAL_INS 테이블 구조는 다음과 같으며, 
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

-- NAME	TYPE	NULLABLE
-- ANIMAL_ID	VARCHAR(N)	FALSE
-- ANIMAL_TYPE	VARCHAR(N)	FALSE
-- DATETIME	DATETIME	FALSE
-- INTAKE_CONDITION	VARCHAR(N)	FALSE
-- NAME	VARCHAR(N)	TRUE
-- SEX_UPON_INTAKE	VARCHAR(N)	FALSE

-- 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.

SELECT * from ANIMAL_INS order by ANIMAL_ID
-- 역순 정렬 원할 시 order by ANIMAL_ID desc
-- 여러 attribute에 대해서도 동시에 가능