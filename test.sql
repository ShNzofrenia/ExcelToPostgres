--
-- PostgreSQL database dump
--

-- Dumped from database version 13.8
-- Dumped by pg_dump version 13.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: teasd; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teasd (
    row_id character varying,
    order_id character varying,
    ship_mode character varying,
    customer_id character varying,
    customer_name character varying,
    segment character varying,
    country character varying,
    city character varying,
    state character varying,
    postal_code character varying,
    region character varying,
    product_id character varying,
    category character varying,
    sub_category character varying,
    product_name character varying,
    sales character varying,
    quantity character varying,
    discount character varying,
    profit character varying
);


ALTER TABLE public.teasd OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

