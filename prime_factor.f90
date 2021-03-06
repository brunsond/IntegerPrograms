PROGRAM PRIME_FACTOR

IMPLICIT NONE

INTEGER(KIND=8) :: D,NUM,ST

READ(*,*) NUM

ST = FLOOR(NUM**0.5)

OPEN(1, FILE = 'prime_list.txt')

D = 0
DO WHILE (NUM > 1 .AND. D .LE. ST)
    READ(1,*) D
    DO WHILE (MOD(NUM,D)==0)
        NUM = NUM / D
        PRINT *,D
    END DO
END DO

IF (NUM > 1) THEN
    PRINT *,NUM
END IF


END PROGRAM PRIME_FACTOR
