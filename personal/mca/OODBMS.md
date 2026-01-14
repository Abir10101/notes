# Object-Oriented Database Management Systems (OODBMS)

## Key Characteristics

### 1. Direct Object Persistence
OODBMS allows storing class objects directly without transformation. Complex objects with nested relationships can be persisted in their natural form.

**Example:**
```java
class Person {
  int id;
  String name;
}

class Student {
  int id;
  Person person;
}
```

In OODBMS, the `person` attribute within the `Student` object is stored as-is, maintaining the object reference and structure.

**Contrast with RDBMS:**
In relational databases, you would need to:
- Create separate tables for `Student` and `Person`
- Define a foreign key in the `Student` table referencing the `Person` table
- Manually manage the relationship through join operations

### 2. Object-Oriented Programming Support
OODBMS natively supports OOP concepts, including:

- **Encapsulation:** Objects maintain their data and methods together
- **Inheritance:** Class hierarchies are preserved in the database
- **Polymorphism:** Objects can be stored and retrieved with their behavioral characteristics intact
- **Abstraction:** Complex data types and relationships are handled naturally

This eliminates the **object-relational impedance mismatch** that occurs when mapping object-oriented code to relational database schemas.
