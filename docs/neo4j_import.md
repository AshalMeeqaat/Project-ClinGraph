# Neo4j Import Guide

## Step 1

Copy generated CSV files into the Neo4j import directory.

Example

Disease.csv
Gene.csv
Compound.csv
Relationships.csv

---

## Step 2

Start Neo4j Desktop.

---

## Step 3

Create a fresh database.

---

## Step 4

Import nodes.

---

## Step 5

Import relationships.

---

## Step 6

Verify graph.

Example queries

MATCH (n)
RETURN count(n);

CALL db.labels();

CALL db.relationshipTypes();