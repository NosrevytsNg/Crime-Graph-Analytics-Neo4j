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
flowchart LR

A[Crime]
A -->|OCCURED_IN| B[Neighbourhood] 
A -->|ON_BEAT| C[Beat]
A -->|INVOLVED_IN| D[PropertyType]

```

#### Example Cypher Queries 

- Find crimes in a specific neighborhood
```text
MATCH (c:Crime)-[:OCCURRED_IN]->(n:Neighborhood)
WHERE n.name = "Loop"
RETURN c
LIMIT 25
```
  
- Identify neighborhoods with the highest crime counts
```text
MATCH (c:Crime)-[:OCCURRED_IN]->(n:Neighborhood)
RETURN n.name AS neighborhood, COUNT(c) AS crimeCount
ORDER BY crimeCount DESC
```
  
- Identify beats with the most crime incidents
```text
MATCH (c:Crime)-[:ON_BEAT]->(b:Beat)
RETURN b.name AS beat, COUNT(c) AS crimeCount
ORDER BY crimeCount DESC
```

- Identify property types most frequently involved in crimes
```text
MATCH (c:Crime)-[:INVOLVED_IN]->(p:PropertyType)
RETURN p.name AS propertyType, COUNT(c) AS incidents
ORDER BY incidents DESC
```

#### Advanced Graph Analytics Queries

Beyond simple data retrieval, graph databases enable analysts to explore spatial and contextual relationships within crime data.

The following queries demonstrate how graph traversal can reveal crime distribution patterns across neighborhoods, police beats, and property types.

- Identify Crime Hotspots by Neighborhood
```text
MATCH (c:Crime)-[:OCCURRED_IN]->(n:Neighborhood)
RETURN n.name AS neighborhood, COUNT(c) AS crimeCount
ORDER BY crimeCount DESC
LIMIT 10
```
This query identifies neighborhoods with the highest number of reported crimes.

Such analysis can assist law enforcement in identifying **crime hotspots** and prioritizing patrol deployment.

- Identify Police Beats with the Highest Crime Activity
```text
MATCH (c:Crime)-[:ON_BEAT]->(b:Beat)
RETURN b.name AS beat, COUNT(c) AS crimeCount
ORDER BY crimeCount DESC
```
This allows analysts to determine which patrol beats experience the most criminal activity.

- Identify Property Types Most Frequently Involved in Crimes
```text
MATCH (c:Crime)-[:INVOLVED_IN]->(p:PropertyType)
RETURN p.name AS propertyType, COUNT(c) AS incidents
ORDER BY incidents DESC
```
This analysis highlights which types of properties are most frequently targeted in crimes.

- Cross-Analysis: Property Type Distribution by Neighborhood
```text
MATCH (c:Crime)-[:OCCURRED_IN]->(n:Neighborhood),
      (c)-[:INVOLVED_IN]->(p:PropertyType)
RETURN n.name AS neighborhood,
       p.name AS propertyType,
       COUNT(c) AS incidents
ORDER BY incidents DESC
```
This query reveals which types of properties are frequently associated with crime in specific neighborhoods.

### Network Analysis: Spatial Crime Patterns

While this dataset does not model individuals or criminal networks, graph analysis can still reveal important spatial patterns.

By analysing the connections between crimes, locations, and property types, analysts can detect:

• geographic crime concentration  
• high-activity patrol beats  
• frequently targeted property categories  
• patterns of crime distribution across neighborhoods

Example: Identifying Neighborhood–Beat Relationships
```text
MATCH (c:Crime)-[:OCCURRED_IN]->(n:Neighborhood),
      (c)-[:ON_BEAT]->(b:Beat)
RETURN n.name AS neighborhood,
       b.name AS beat,
       COUNT(c) AS incidents
ORDER BY incidents DESC
```
This query helps identify which patrol beats are responsible for areas experiencing higher crime activity.

## Graph Visualization & Analytics

One of the major strengths of graph databases such as Neo4j is the ability to visually explore relationships within the data.

Using Neo4j Browser, crime incidents can be visualized alongside their associated neighborhoods, beats, and property types.

Visual exploration allows analysts to quickly identify:

• neighborhoods with dense clusters of crime  
• police beats associated with high crime activity  
• frequently targeted property types  
• patterns of crime distribution across geographic regions

### Graph Schema

The graph database models crime incidents and their contextual attributes using four node types and three relationship types.

<p align="center">
  <img width="522.5" height="385" alt="Assignment 2 - Crime Schema" src="https://github.com/user-attachments/assets/ebd6adb0-2ccc-497d-a27f-995231563a8f" />
</p>

### Node and Relationship Styling

To improve readability in Neo4j Browser, node labels and relationship types were styled using distinct colors.  
This visual configuration helps differentiate entities and relationships during graph exploration.

<p align="center">
  <img width="331.25" height="320" alt="Nodes and Relationship Colours" src="https://github.com/user-attachments/assets/3fcbf842-ba7f-42d8-b480-add99fbaa7bf" />
</p>


## 🖋️ Author

**Styverson Ng**

Bachelor of Information Technology <br>
Artificial Intelligence & Autonomous Systems <br>
Cyber Security & Cyber Forensics <br>

Murdoch University <br>
