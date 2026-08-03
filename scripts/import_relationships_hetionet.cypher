:auto

// ==========================================================
// ClinGraph - Hetionet Relationship Import
// Human-readable relationship names
// ==========================================================


// ----------------------------------------------------------
// Compound -> Disease
// CtD = Compound treats Disease
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'CtD'
CALL {
    WITH row
    MATCH (c:Compound {id: row.source})
    MATCH (d:Disease {id: row.target})
    MERGE (c)-[:TREATS]->(d)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Disease -> Symptom
// DpS = Disease presents Symptom
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'DpS'
CALL {
    WITH row
    MATCH (d:Disease {id: row.source})
    MATCH (s:Symptom {id: row.target})
    MERGE (d)-[:HAS_SYMPTOM]->(s)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Disease -> Gene
// DaG = Disease associates Gene
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'DaG'
CALL {
    WITH row
    MATCH (d:Disease {id: row.source})
    MATCH (g:Gene {id: row.target})
    MERGE (d)-[:ASSOCIATED_WITH_GENE]->(g)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Disease -> Anatomy
// DlA = Disease localizes Anatomy
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'DlA'
CALL {
    WITH row
    MATCH (d:Disease {id: row.source})
    MATCH (a:Anatomy {id: row.target})
    MERGE (d)-[:AFFECTS_ANATOMY]->(a)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Disease -> Disease
// DrD
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'DrD'
CALL {
    WITH row
    MATCH (d1:Disease {id: row.source})
    MATCH (d2:Disease {id: row.target})
    MERGE (d1)-[:RESEMBLES_DISEASE]->(d2)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Compound -> Gene
// CbG = Compound binds Gene
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'CbG'
CALL {
    WITH row
    MATCH (c:Compound {id: row.source})
    MATCH (g:Gene {id: row.target})
    MERGE (c)-[:TARGETS_GENE]->(g)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Compound -> Compound
// CrC
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'CrC'
CALL {
    WITH row
    MATCH (c1:Compound {id: row.source})
    MATCH (c2:Compound {id: row.target})
    MERGE (c1)-[:RESEMBLES_COMPOUND]->(c2)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Compound -> Side Effect
// CcSE
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'CcSE'
CALL {
    WITH row
    MATCH (c:Compound {id: row.source})
    MATCH (s:`Side Effect` {id: row.target})
    MERGE (c)-[:CAUSES_SIDE_EFFECT]->(s)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Pharmacologic Class -> Compound
// PCiC
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'PCiC'
CALL {
    WITH row
    MATCH (pc:`Pharmacologic Class` {id: row.source})
    MATCH (c:Compound {id: row.target})
    MERGE (pc)-[:INCLUDES_COMPOUND]->(c)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Gene -> Biological Process
// GpBP
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'GpBP'
CALL {
    WITH row
    MATCH (g:Gene {id: row.source})
    MATCH (bp:`Biological Process` {id: row.target})
    MERGE (g)-[:INVOLVED_IN_BIOLOGICAL_PROCESS]->(bp)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Gene -> Molecular Function
// GpMF
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'GpMF'
CALL {
    WITH row
    MATCH (g:Gene {id: row.source})
    MATCH (mf:`Molecular Function` {id: row.target})
    MERGE (g)-[:HAS_MOLECULAR_FUNCTION]->(mf)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Gene -> Cellular Component
// GpCC
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'GpCC'
CALL {
    WITH row
    MATCH (g:Gene {id: row.source})
    MATCH (cc:`Cellular Component` {id: row.target})
    MERGE (g)-[:LOCATED_IN_CELLULAR_COMPONENT]->(cc)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Gene -> Pathway
// GpPW
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'GpPW'
CALL {
    WITH row
    MATCH (g:Gene {id: row.source})
    MATCH (p:Pathway {id: row.target})
    MERGE (g)-[:PARTICIPATES_IN_PATHWAY]->(p)
} IN TRANSACTIONS OF 10000 ROWS;


// ----------------------------------------------------------
// Gene -> Gene
// GiG
// ----------------------------------------------------------

LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row WHERE row.relation = 'GiG'
CALL {
    WITH row
    MATCH (g1:Gene {id: row.source})
    MATCH (g2:Gene {id: row.target})
    MERGE (g1)-[:INTERACTS_WITH]->(g2)
} IN TRANSACTIONS OF 10000 ROWS;



Current Hetionet Import Scope

ClinGraph currently imports the 14 most clinically relevant 
Hetionet relationship categories using descriptive relationship 
names rather than Hetionet abbreviations.

Examples:

TREATS
HAS_SYMPTOM
ASSOCIATED_WITH_GENE
TARGETS_GENE
CAUSES_SIDE_EFFECT
INTERACTS_WITH
INVOLVED_IN_BIOLOGICAL_PROCESS
HAS_MOLECULAR_FUNCTION
LOCATED_IN_CELLULAR_COMPONENT
PARTICIPATES_IN_PATHWAY
AFFECTS_ANATOMY

The remaining Hetionet metaedges (AdG, AeG, AuG, CdG, CpD, CuG, DdG, DuG, GcG, GrG) are 
intentionally excluded from the first implementation because they are not required for 
the current clinical reasoning, retrieval, and question-answering workflow. They can be 
incorporated in future versions if more advanced biomedical reasoning is needed.