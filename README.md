# Neo4j Crime Graph Analytics

Graph-based crime investigation and network analysis using Neo4j and Cypher.

This project demonstrates how graph databases can uncover hidden relationships within criminal networks, enabling investigators to identify key suspects, collaboration patterns, and crime hotspots that may not be visible using traditional relational databases.

By modelling crime data as a network of people, crimes, and locations, investigators can perform relationship-driven analysis to understand criminal behaviour and network structures.

Typical investigative questions this graph can answer include:

- Which suspects collaborated on criminal activities?
- Which suspects are central figures within the network?
- Which locations appear most frequently in crime records?
- Which individuals are connected through indirect criminal associations?

Graph databases are widely used in:

- law enforcement investigations
- fraud detection
- intelligence analysis
- cybercrime network mapping

## Project Overview

Traditional relational databases store information in tables, making it difficult to analyse complex relationships between entities.

Graph databases such as Neo4j represent data as:

- Nodes → entities (people, crimes, locations)
- Relationships → connections between entities
- Properties → attributes of nodes and relationships

This project constructs a crime investigation network where suspects, crimes, and locations are connected through relationships that can be explored using Cypher queries.

Investigators can then identify patterns such as:

- suspects committing multiple crimes
- criminal collaboration networks
- frequently targeted locations
- central figures within criminal organisations

### Technology Used
| Technology | Purpose |
| ----- | ----- |
| Neo4j | Graph database engine |
| Cypher | Graph query language |
| Neo4j Browser | Interactive graph visualization |
| Graph Data Modelling | Relationship-driven data representation |
| Graph Algorithm | Network analysis and pattern detection |


### Graph Data Model

The dataset models **crime incidents and their associated contextual information** using Neo4j.

Instead of analysing suspect relationships, the graph focuses on **where crimes occur and the type of crime involved**.

#### Nodes
| Node | Description |
| ----- | ----- |
| Crime | Individual crime incident |
| Beat | Police patrol beat where the crime occurred |
| Neighborhood | Neighborhood where the crime took place |
| PropertyType | Type of property involved in the crime 


#### Relationship Types
| Relationship | Description |
| ----- | ----- |
| OCCURRED_IN | Crime occurred within a specific neighborhood |
| ON_BEAT | Crime took place within a police beat |
| INVOLVED_IN | Crime involved a particular property type |

#### Graph Schema
```mermaid
A[Crime]
A -->|OCCURED_IN| B[Neighbourhood] 
A -->|ON_BEAT| C[Beat]
A -->|INVOLVED_IN| D[PropertyType]

```














## 🖋️ Author

**Styverson Ng**

Bachelor of Information Technology <br>
Artificial Intelligence & Autonomous Systems <br>
Cyber Security & Cyber Forensics <br>

Murdoch University <br>
