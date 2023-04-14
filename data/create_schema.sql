-- Name: geographic_div; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE geographic_div (
    tsn integer NOT NULL,
    geographic_value character varying(45) NOT NULL,
    update_date date NOT NULL
);

-- Name: hierarchy; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE hierarchy (
    hierarchy_string character varying(300) NOT NULL,
    tsn integer NOT NULL,
    parent_tsn integer,
    level integer NOT NULL,
    childrencount integer NOT NULL
);

-- Name: jurisdiction; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE jurisdiction (
    tsn integer NOT NULL,
    jurisdiction_value character varying(30) NOT NULL,
    origin character varying(19) NOT NULL,
    update_date date NOT NULL
);

-- Name: kingdoms; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE kingdoms (
    kingdom_id integer NOT NULL,
    kingdom_name character(10) NOT NULL,
    update_date date NOT NULL
);

-- Name: longnames; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE longnames (
    tsn integer NOT NULL,
    completename character varying(300) NOT NULL
);

-- Name: other_sources; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE other_sources (
    source_id_prefix character(3) NOT NULL,
    source_id integer NOT NULL,
    source_type character(10) NOT NULL,
    source character varying(64) NOT NULL,
    version character(10) NOT NULL,
    acquisition_date date NOT NULL,
    source_comment character varying(500) DEFAULT NULL::character varying,
    update_date date NOT NULL
);

-- Name: nodc_ids; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE nodc_ids (
    nodc_id character(12) NOT NULL,
    update_date date NOT NULL,
    tsn integer NOT NULL
);

-- Name: publications; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE publications (
    pub_id_prefix character(3) NOT NULL,
    publication_id integer NOT NULL,
    reference_author character varying(100) NOT NULL,
    title character varying(255) DEFAULT NULL::character varying,
    publication_name character varying(255) NOT NULL,
    listed_pub_date date,
    actual_pub_date date NOT NULL,
    publisher character varying(80) DEFAULT NULL::character varying,
    pub_place character varying(40) DEFAULT NULL::character varying,
    isbn character varying(16) DEFAULT NULL::character varying,
    issn character varying(16) DEFAULT NULL::character varying,
    pages character varying(15) DEFAULT NULL::character varying,
    pub_comment character varying(500) DEFAULT NULL::character varying,
    update_date date NOT NULL
);

-- Name: reference_links; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE reference_links (
    tsn integer NOT NULL,
    doc_id_prefix character(3) NOT NULL,
    documentation_id integer NOT NULL,
    original_desc_ind character(1) DEFAULT NULL::bpchar,
    init_itis_desc_ind character(1) DEFAULT NULL::bpchar,
    change_track_id integer,
    vernacular_name character varying(80) DEFAULT NULL::character varying,
    update_date date NOT NULL
);

-- Name: strippedauthor; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE strippedauthor (
    taxon_author_id integer NOT NULL,
    shortauthor character varying(100) NOT NULL
);

-- Name: synonym_links; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE synonym_links (
    tsn integer NOT NULL,
    tsn_accepted integer NOT NULL,
    update_date date NOT NULL
);

-- Name: taxon_authors_lkp; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE taxon_authors_lkp (
    taxon_author_id integer NOT NULL,
    taxon_author character varying(100) NOT NULL,
    update_date date NOT NULL,
    kingdom_id smallint NOT NULL,
    short_author text
);

-- Name: taxon_unit_types; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE taxon_unit_types (
    kingdom_id integer NOT NULL,
    rank_id smallint NOT NULL,
    rank_name character(15) NOT NULL,
    dir_parent_rank_id smallint NOT NULL,
    req_parent_rank_id smallint NOT NULL,
    update_date date NOT NULL
);

-- Name: taxonomic_units; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE taxonomic_units (
    tsn integer NOT NULL,
    unit_ind1 character(1) DEFAULT NULL::bpchar,
    unit_name1 character(35) NOT NULL,
    unit_ind2 character(1) DEFAULT NULL::bpchar,
    unit_name2 character varying(35) DEFAULT NULL::character varying,
    unit_ind3 character varying(7) DEFAULT NULL::character varying,
    unit_name3 character varying(35) DEFAULT NULL::character varying,
    unit_ind4 character varying(7) DEFAULT NULL::character varying,
    unit_name4 character varying(35) DEFAULT NULL::character varying,
    unnamed_taxon_ind character(1) DEFAULT NULL::bpchar,
    name_usage character varying(12) NOT NULL,
    unaccept_reason character varying(50) DEFAULT NULL::character varying,
    credibility_rtng character varying(40) NOT NULL,
    completeness_rtng character(10) DEFAULT NULL::bpchar,
    currency_rating character(7) DEFAULT NULL::bpchar,
    phylo_sort_seq smallint,
    initial_time_stamp timestamp without time zone NOT NULL,
    parent_tsn integer,
    taxon_author_id integer,
    hybrid_author_id integer,
    kingdom_id smallint NOT NULL,
    rank_id smallint NOT NULL,
    update_date date NOT NULL,
    uncertain_prnt_ind character(3) DEFAULT NULL::bpchar,
    n_usage text,
    complete_name character varying(255) NOT NULL
);

-- Name: tu_comments_links; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE tu_comments_links (
    tsn integer NOT NULL,
    comment_id integer NOT NULL,
    update_date date NOT NULL
);

-- Name: vern_ref_links; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE vern_ref_links (
    tsn integer NOT NULL,
    doc_id_prefix character(3) NOT NULL,
    documentation_id integer NOT NULL,
    update_date date NOT NULL,
    vern_id integer NOT NULL
);

-- Name: vernaculars; Type: TABLE; Schema: public; Owner: -; Tablespace: 
CREATE TABLE vernaculars (
    tsn integer NOT NULL,
    vernacular_name character varying(80) NOT NULL,
    language character varying(15) NOT NULL,
    approved_ind character(1) DEFAULT NULL::bpchar,
    update_date date NOT NULL,
    vern_id integer NOT NULL
);