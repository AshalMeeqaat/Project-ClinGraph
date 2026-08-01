// ==========================================
// ClinGraph - Hetionet Import
// ==========================================

// ---------- Indexes ----------

CREATE INDEX disease_id IF NOT EXISTS
FOR (n:Disease)
ON (n.id);

CREATE INDEX gene_id IF NOT EXISTS
FOR (n:Gene)
ON (n.id);

CREATE INDEX compound_id IF NOT EXISTS
FOR (n:Compound)
ON (n.id);

CREATE INDEX anatomy_id IF NOT EXISTS
FOR (n:Anatomy)
ON (n.id);

CREATE INDEX pathway_id IF NOT EXISTS
FOR (n:Pathway)
ON (n.id);

CREATE INDEX symptom_id IF NOT EXISTS
FOR (n:Symptom)
ON (n.id);

CREATE INDEX sideeffect_id IF NOT EXISTS
FOR (n:`Side Effect`)
ON (n.id);

CREATE INDEX bp_id IF NOT EXISTS
FOR (n:`Biological Process`)
ON (n.id);

CREATE INDEX mf_id IF NOT EXISTS
FOR (n:`Molecular Function`)
ON (n.id);

CREATE INDEX cc_id IF NOT EXISTS
FOR (n:`Cellular Component`)
ON (n.id);

CREATE INDEX pc_id IF NOT EXISTS
FOR (n:`Pharmacologic Class`)
ON (n.id);

// ==========================================
// NOTE
//
// CSV Import commands will be added after
// finalizing the Neo4j bulk import pipeline.
//
// ==========================================