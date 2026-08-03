// =====================================
// Clear ClinGraph Database
// =====================================

MATCH (n)
DETACH DELETE n;

// Drop indexes

DROP INDEX disease_id IF EXISTS;
DROP INDEX gene_id IF EXISTS;
DROP INDEX compound_id IF EXISTS;
DROP INDEX anatomy_id IF EXISTS;
DROP INDEX pathway_id IF EXISTS;
DROP INDEX symptom_id IF EXISTS;
DROP INDEX sideeffect_id IF EXISTS;
DROP INDEX bp_id IF EXISTS;
DROP INDEX mf_id IF EXISTS;
DROP INDEX cc_id IF EXISTS;
DROP INDEX pc_id IF EXISTS;