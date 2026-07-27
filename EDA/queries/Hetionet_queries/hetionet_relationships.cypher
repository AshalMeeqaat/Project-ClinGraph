
LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Gene' AND row.target_type='Biological Process'
MATCH (a:Gene {id:row.source})
MATCH (b:`Biological Process` {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Gene' AND row.target_type='Gene'
MATCH (a:Gene {id:row.source})
MATCH (b:Gene {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Compound' AND row.target_type='Compound'
MATCH (a:Compound {id:row.source})
MATCH (b:Compound {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Disease' AND row.target_type='Gene'
MATCH (a:Disease {id:row.source})
MATCH (b:Gene {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Disease' AND row.target_type='Symptom'
MATCH (a:Disease {id:row.source})
MATCH (b:Symptom {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Disease' AND row.target_type='Anatomy'
MATCH (a:Disease {id:row.source})
MATCH (b:Anatomy {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Compound' AND row.target_type='Disease'
MATCH (a:Compound {id:row.source})
MATCH (b:Disease {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Compound' AND row.target_type='Gene'
MATCH (a:Compound {id:row.source})
MATCH (b:Gene {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Disease' AND row.target_type='Disease'
MATCH (a:Disease {id:row.source})
MATCH (b:Disease {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Anatomy' AND row.target_type='Gene'
MATCH (a:Anatomy {id:row.source})
MATCH (b:Gene {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Gene' AND row.target_type='Molecular Function'
MATCH (a:Gene {id:row.source})
MATCH (b:`Molecular Function` {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Pharmacologic Class' AND row.target_type='Compound'
MATCH (a:`Pharmacologic Class` {id:row.source})
MATCH (b:Compound {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Gene' AND row.target_type='Cellular Component'
MATCH (a:Gene {id:row.source})
MATCH (b:`Cellular Component` {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Gene' AND row.target_type='Pathway'
MATCH (a:Gene {id:row.source})
MATCH (b:Pathway {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);


LOAD CSV WITH HEADERS FROM 'file:///Relationships.csv' AS row
WITH row
WHERE row.source_type='Compound' AND row.target_type='Side Effect'
MATCH (a:Compound {id:row.source})
MATCH (b:`Side Effect` {id:row.target})
CREATE (a)-[:RELATED_TO {type:row.relation}]->(b);

