CREATE UNLOGGED TABLE conversations (
    author_id int8,
    content text, 
    possibly_sensitive bool, 
    language varchar(3), 
    source text, 
    retweet_count int4,
    reply_count int4, 
    like_count int4, 
    quote_count int4, 
    created_at timestamp
)

CREATE UNLOGGED TABLE authors (
    name varchar(255), 
    username varchar(255), 
    description text, 
    followers_count int4, 
    following_count int4, 
    tweet_count int4, 
    listed_count int4
)

CREATE TABLE conversation_hashatags (
    conversation_id int8, 
    hashtag_id int8
)

CREATE TABLE hashtags (
    tag text
)

CREATE TABLE conversation_references (
    conversation_id int8, 
    parent_id, 
    type varchar(20)
)

CREATE TABLE links (
    conversation_id int8, 
    url varchar(2048),
    title text,
    description text
)

CREATE TABLE annotations (
    conversation_id int8, 
    value text, 
    type text, 
    probability numeric(4,3)
)

CREATE TABLE context_annotations (
    conversation_id int8, 
    context_domain_id int8, 
    context_entity_id int8 
)

CREATE TABLE context_domains (
    name varchar(255),
    description text
)

context_entities (
    name varchar(255),
    description text


-- ADD FK Constrains 
-- ADD ids