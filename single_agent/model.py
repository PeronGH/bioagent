from typing import List
from pydantic import BaseModel, Field


class GOTerm(BaseModel):
    go_id: str = Field(alias="GO_ID", description="Example: 'GO:0005829'")
    evidence_code: str = Field(description="Example: 'IDA', 'IMP'")


class Gene(BaseModel):
    veupathdb_id: str = Field(
        alias="VEuPAthDB_ID", description="Example: 'PF3D7_0618500'"
    )
    shorthand_name: str = Field(description="Example: 'MDH'")
    full_name: str = Field(description="Example: 'malate dehydrogenase'")
    go_terms: List[GOTerm] = Field(alias="GO_terms")


class Species(BaseModel):
    name: str = Field(description="Example: 'P.falciparum'")
    strain: str = Field(description="Example: '3D7'")
    taxon_id: str = Field(description="Example: '36329'")
    genes: List[Gene]


class Output(BaseModel):
    pmid: str = Field(
        alias="PMID",
        description="PubMed Identifier.",
    )
    species: List[Species]
