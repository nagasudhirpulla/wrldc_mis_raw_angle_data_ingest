CREATE TABLE DAILY_ANGLES_DATA (
    ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
    DATA_DATE DATE NOT NULL,
    ANGLE_PAIR VARCHAR2(250 BYTE) NOT NULL,
    ANGULAR_LIMIT NUMBER NOT NULL,
    VIOL_PERC NUMBER NOT NULL,
    MAX_VIOL NUMBER,
    MIN_VIOL NUMBER,
    DATA_TYPE VARCHAR2(10 BYTE) NOT NULL,
    UNIQUE(DATA_DATE, ANGLE_PAIR)
);