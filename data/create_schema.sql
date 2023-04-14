-- Name: comments; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE comments (
    comment_id         INTEGER NOT NULL,
    commentator        CHARACTER VARYING(100) DEFAULT NULL::CHARACTER VARYING,
    comment_detail     TEXT NOT NULL,
    comment_time_stamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    update_date        DATE NOT NULL
);

