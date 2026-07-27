///////////////////////////////////////////////////////////////////////////
// HETIONET GRAPH DATABASE
///////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////
// CONSTRAINTS
///////////////////////////////////////////////////////////////////////////

CREATE CONSTRAINT gene_id IF NOT EXISTS
FOR (n:Gene)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT disease_id IF NOT EXISTS
FOR (n:Disease)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT compound_id IF NOT EXISTS
FOR (n:Compound)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT anatomy_id IF NOT EXISTS
FOR (n:Anatomy)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT pathway_id IF NOT EXISTS
FOR (n:Pathway)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT symptom_id IF NOT EXISTS
FOR (n:Symptom)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT sideeffect_id IF NOT EXISTS
FOR (n:`Side Effect`)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT bp_id IF NOT EXISTS
FOR (n:`Biological Process`)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT mf_id IF NOT EXISTS
FOR (n:`Molecular Function`)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT cc_id IF NOT EXISTS
FOR (n:`Cellular Component`)
REQUIRE n.id IS UNIQUE;

CREATE CONSTRAINT pc_id IF NOT EXISTS
FOR (n:`Pharmacologic Class`)
REQUIRE n.id IS UNIQUE;

///////////////////////////////////////////////////////////////////////////
// LOAD NODES
///////////////////////////////////////////////////////////////////////////

LOAD CSV WITH HEADERS FROM 'file:///Gene.csv' AS row
CREATE (:Gene {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Disease.csv' AS row
CREATE (:Disease {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Compound.csv' AS row
CREATE (:Compound {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Anatomy.csv' AS row
CREATE (:Anatomy {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Pathway.csv' AS row
CREATE (:Pathway {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Symptom.csv' AS row
CREATE (:Symptom {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Side_Effect.csv' AS row
CREATE (:`Side Effect` {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Biological_Process.csv' AS row
CREATE (:`Biological Process` {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Molecular_Function.csv' AS row
CREATE (:`Molecular Function` {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Cellular_Component.csv' AS row
CREATE (:`Cellular Component` {id:row.id,name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///Pharmacologic_Class.csv' AS row
CREATE (:`Pharmacologic Class` {id:row.id,name:row.name});

///////////////////////////////////////////////////////////////////////////
// IMPORT RELATIONSHIPS
///////////////////////////////////////////////////////////////////////////

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row

CALL {

WITH row

WHERE row.source_type='Gene' AND row.target_type='Disease'

MATCH (a:Gene{id:row.source})

MATCH (b:Disease{id:row.target})

CREATE (a)-[:RELATED_TO{type:row.relation}]->(b)

RETURN 1

UNION

WITH row

WHERE row.source_type='Disease' AND row.target_type='Gene'

MATCH (a:Disease{id:row.source})

MATCH (b:Gene{id:row.target})

CREATE (a)-[:RELATED_TO{type:row.relation}]->(b)

RETURN 1

UNION

WITH row

WHERE row.source_type='Compound' AND row.target_type='Gene'

MATCH (a:Compound{id:row.source})

MATCH (b:Gene{id:row.target})

CREATE (a)-[:RELATED_TO{type:row.relation}]->(b)

RETURN 1

UNION

WITH row

WHERE row.source_type='Gene' AND row.target_type='Biological Process'

MATCH (a:Gene{id:row.source})

MATCH (b:`Biological Process`{id:row.target})

CREATE (a)-[:RELATED_TO{type:row.relation}]->(b)

RETURN 1

UNION

WITH row

WHERE row.source_type='Gene' AND row.target_type='Pathway'

MATCH (a:Gene{id:row.source})

MATCH (b:Pathway{id:row.target})

CREATE (a)-[:RELATED_TO{type:row.relation}]->(b)

RETURN 1

}

RETURN count(*);