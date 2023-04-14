-- drop the old database completely
DROP DATABASE IF EXISTS "ITIS";

-- PostgreSQL database dump
SET statement_timeout = 0;
SET client_encoding = 'LATIN1';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

-- Name: ITIS; Type: DATABASE; Schema: -; Owner: -
CREATE DATABASE "ITIS" WITH TEMPLATE = template0 ENCODING = 'LATIN1' LC_COLLATE = 'en_US.ISO8859-1' LC_CTYPE = 'en_US.ISO8859-1';

\connect "ITIS"

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';

SET search_path = public, pg_catalog;
SET default_tablespace = '';
SET default_with_oids = false;
