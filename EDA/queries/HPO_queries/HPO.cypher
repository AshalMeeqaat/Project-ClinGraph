///////////////////////////////////////////////////////////////////////////
// HPO KNOWLEDGE GRAPH
///////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////
// CONSTRAINTS
///////////////////////////////////////////////////////////////////////////

CREATE CONSTRAINT disease_id IF NOT EXISTS
FOR (d:Disease)
REQUIRE d.id IS UNIQUE;

CREATE CONSTRAINT phenotype_id IF NOT EXISTS
FOR (p:Phenotype)
REQUIRE p.id IS UNIQUE;

///////////////////////////////////////////////////////////////////////////
// LOAD DISEASE NODES
///////////////////////////////////////////////////////////////////////////

LOAD CSV WITH HEADERS
FROM 'file:///Disease.csv' AS row

CREATE (:Disease{
    id: row.id,
    name: row.name
});

///////////////////////////////////////////////////////////////////////////
// LOAD PHENOTYPE NODES
///////////////////////////////////////////////////////////////////////////

LOAD CSV WITH HEADERS
FROM 'file:///Phenotype.csv' AS row

CREATE (:Phenotype{
    id: row.id,
    name: row.name
});

///////////////////////////////////////////////////////////////////////////
// LOAD RELATIONSHIPS
///////////////////////////////////////////////////////////////////////////

LOAD CSV WITH HEADERS
FROM 'file:///HAS_PHENOTYPE.csv' AS row

MATCH (d:Disease {id: row.source})
MATCH (p:Phenotype {id: row.target})

CREATE (d)-[:HAS_PHENOTYPE]->(p);

///////////////////////////////////////////////////////////////////////////
// VERIFY IMPORT
///////////////////////////////////////////////////////////////////////////

MATCH (n)
RETURN labels(n)[0] AS NodeType,
count(*) AS Count
ORDER BY Count DESC;

MATCH ()-[r]->()
RETURN type(r) AS Relationship,
count(*) AS Count;

///////////////////////////////////////////////////////////////////////////
// DASHBOARD QUERIES
///////////////////////////////////////////////////////////////////////////

//
// Total Nodes
//

MATCH (n)
RETURN count(n) AS TotalNodes;

//
// Total Relationships
//

MATCH ()-[r]->()
RETURN count(r) AS TotalRelationships;

//
// Diseases
//

MATCH (d:Disease)
RETURN count(d) AS Diseases;

//
// Phenotypes
//

MATCH (p:Phenotype)
RETURN count(p) AS Phenotypes;

//
// Diseases with Most Phenotypes
//

MATCH (d:Disease)-[:HAS_PHENOTYPE]->(p:Phenotype)

RETURN
d.name AS Disease,
count(p) AS PhenotypeCount

ORDER BY PhenotypeCount DESC
LIMIT 20;

//
// Sample Graph
//

MATCH p=(d:Disease)-[:HAS_PHENOTYPE]->(p:Phenotype)

RETURN p
LIMIT 100;

//
// Top Connected Diseases
//

MATCH (d:Disease)

RETURN
d.name,
size((d)-[:HAS_PHENOTYPE]->()) AS Phenotypes

ORDER BY Phenotypes DESC
LIMIT 20;

//
// Graph Exploration
//

MATCH p=(a)-[*1..2]-(b)

RETURN p
LIMIT 100;