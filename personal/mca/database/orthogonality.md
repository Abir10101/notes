# OOP Constructors: Orthogonal vs Non-Orthogonal - Complete Summary

## 1. Core Concepts

### Orthogonal Constructors
**Definition:** Constructors where parameters are completely independent of each other. Changing one parameter doesn't affect or constrain others.

**Example:**
```java
class Rectangle {
    private int width;
    private int height;
    private String color;
    
    // Orthogonal - each parameter is independent
    public Rectangle(int width, int height, String color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }
}

// Any combination is valid
Rectangle r1 = new Rectangle(10, 20, "red");
Rectangle r2 = new Rectangle(10, 30, "red");   // Only height changes
Rectangle r3 = new Rectangle(15, 20, "blue");  // Width and color change
```

**Characteristics:**
- Parameters are completely independent
- No interdependencies or constraints
- Clean separation of concerns
- Easy to understand and maintain

---

### Non-Orthogonal Constructors
**Definition:** Constructors where parameters have dependencies or constraints. Some parameters influence or restrict others.

**Example 1 - Derived Values:**
```java
class Circle {
    private double radius;
    private double diameter;
    private double circumference;
    
    // Non-orthogonal - diameter and circumference depend on radius
    public Circle(double radius) {
        this.radius = radius;
        this.diameter = 2 * radius;
        this.circumference = 2 * Math.PI * radius;
    }
}
```

**Example 2 - Parameter Constraints:**
```java
class Employee {
    private String name;
    private String role;
    private double salary;
    
    // Non-orthogonal - salary range depends on role
    public Employee(String name, String role, double salary) {
        this.name = name;
        this.role = role;
        
        // Salary is constrained by role
        if (role.equals("Intern") && salary > 30000) {
            throw new IllegalArgumentException("Intern salary too high");
        }
        if (role.equals("Manager") && salary < 80000) {
            throw new IllegalArgumentException("Manager salary too low");
        }
        this.salary = salary;
    }
}
```

**Characteristics:**
- Parameters have dependencies or constraints
- Changing one may require changing others
- Can lead to invalid states
- More complex validation logic needed

---

## 2. Making Non-Orthogonal Constructors Orthogonal

### Approach 1: Separate Validation
```java
class Employee {
    private String name;
    private String role;
    private double salary;
    
    // Orthogonal constructor
    public Employee(String name, String role, double salary) {
        this.name = name;
        this.role = role;
        this.salary = salary;
    }
    
    // Separate validation method
    public boolean isValid() {
        if (role.equals("Intern") && salary > 30000) return false;
        if (role.equals("Manager") && salary < 80000) return false;
        return true;
    }
}

// Usage
Employee emp = new Employee("John", "Intern", 35000);
if (!emp.isValid()) {
    System.out.println("Warning: Invalid configuration");
}
```

### Approach 2: Factory Methods
```java
class Employee {
    private String name;
    private String role;
    private double salary;
    
    // Private orthogonal constructor
    private Employee(String name, String role, double salary) {
        this.name = name;
        this.role = role;
        this.salary = salary;
    }
    
    // Factory methods with constraints
    public static Employee createIntern(String name, double salary) {
        if (salary > 30000) {
            throw new IllegalArgumentException("Intern salary too high");
        }
        return new Employee(name, "Intern", salary);
    }
    
    public static Employee createManager(String name, double salary) {
        if (salary < 80000) {
            throw new IllegalArgumentException("Manager salary too low");
        }
        return new Employee(name, "Manager", salary);
    }
}

// Usage
Employee intern = Employee.createIntern("John", 25000);
Employee manager = Employee.createManager("Jane", 95000);
```

### Approach 3: Builder Pattern

**Example 1: Basic Builder Pattern**

```java
class Employee {
    private String name;
    private String role;
    private double salary;
    
    private Employee(Builder builder) {
        this.name = builder.name;
        this.role = builder.role;
        this.salary = builder.salary;
    }
    
    public static class Builder {
        private String name;
        private String role;
        private double salary;
        
        public Builder setName(String name) {
            this.name = name;
            return this;
        }
        
        public Builder setRole(String role) {
            this.role = role;
            return this;
        }
        
        public Builder setSalary(double salary) {
            this.salary = salary;
            return this;
        }
        
        public Employee build() {
            // All validation in one place
            if (role.equals("Intern") && salary > 30000) {
                throw new IllegalArgumentException("Intern salary too high");
            }
            if (role.equals("Manager") && salary < 80000) {
                throw new IllegalArgumentException("Manager salary too low");
            }
            return new Employee(this);
        }
    }
}

// Usage - fluent and readable
Employee emp = new Employee.Builder()
    .setName("John Doe")
    .setRole("Intern")
    .setSalary(25000)
    .build();
```

**Example 2: Advanced Builder with Multiple Constraints**

```java
class FlightBooking {
    private String classType;
    private int baggage;
    private boolean mealIncluded;
    private boolean priorityBoarding;
    
    private FlightBooking(Builder builder) {
        this.classType = builder.classType;
        this.baggage = builder.baggage;
        this.mealIncluded = builder.mealIncluded;
        this.priorityBoarding = builder.priorityBoarding;
    }
    
    public static class Builder {
        private String classType;
        private int baggage = 0;
        private boolean mealIncluded = false;
        private boolean priorityBoarding = false;
        
        public Builder(String classType) {
            this.classType = classType;
        }
        
        public Builder baggage(int count) {
            this.baggage = count;
            return this;
        }
        
        public Builder withMeal() {
            this.mealIncluded = true;
            return this;
        }
        
        public Builder withPriorityBoarding() {
            this.priorityBoarding = true;
            return this;
        }
        
        public FlightBooking build() {
            // Centralized validation
            if (classType.equals("Economy") && baggage > 1) {
                throw new IllegalArgumentException("Economy allows max 1 bag");
            }
            if (classType.equals("First") && !mealIncluded) {
                this.mealIncluded = true; // Auto-correct
            }
            if (priorityBoarding && classType.equals("Economy")) {
                throw new IllegalArgumentException("No priority for Economy");
            }
            return new FlightBooking(this);
        }
    }
}

// Usage examples
FlightBooking economy = new FlightBooking.Builder("Economy")
    .baggage(1)
    .build();

FlightBooking business = new FlightBooking.Builder("Business")
    .baggage(2)
    .withMeal()
    .withPriorityBoarding()
    .build();
```

---

## 3. Challenges of Non-Orthogonal Constructors

### Challenge 1: Increased Complexity
```java
class VideoSettings {
    private int width;
    private int height;
    private String aspectRatio;
    
    public VideoSettings(int width, int height, String aspectRatio) {
        if (aspectRatio.equals("16:9") && (width * 9 != height * 16)) {
            throw new IllegalArgumentException("Dimensions don't match");
        }
    }
}

// Developer must calculate correct combinations every time
VideoSettings v = new VideoSettings(1920, 1080, "16:9"); // Valid
VideoSettings v2 = new VideoSettings(1920, 1200, "16:9"); // Error!
```

### Challenge 2: Difficult Testing
```java
// Need to test all valid AND invalid combinations
@Test public void testSavingsAccount() { ... }
@Test public void testPremiumAccount() { ... }
@Test public void testInvalidSavingsRate() { ... }
@Test public void testInvalidPremiumBalance() { ... }
// Many more test cases needed!
```

### Challenge 3: Maintenance Nightmares
```java
// If business rules change (Economy now allows 2 bags),
// must find and update all constraint checks
if (classType.equals("Economy") && baggage > 1) { // Must change to > 2
    throw new IllegalArgumentException("...");
}
```

### Challenge 4: Poor Extensibility
```java
// Adding new tier requires understanding ALL existing constraints
class SubscriptionPlan {
    public SubscriptionPlan(String tier, int maxUsers, boolean support) {
        if (tier.equals("Basic") && maxUsers > 5) { ... }
        if (tier.equals("Enterprise") && !support) { ... }
        // Adding "Professional" tier - where do we add checks?
    }
}
```

### Challenge 5: Hidden Dependencies
```java
class NetworkConnection {
    public NetworkConnection(String protocol, int port, boolean encrypted) {
        if (protocol.equals("HTTPS") && !encrypted) {
            this.encrypted = true; // Silently overrides user input!
        }
    }
}

// Surprising behavior
NetworkConnection conn = new NetworkConnection("HTTPS", 443, false);
// encrypted is true, not false as specified!
```

---

## 6. Key Takeaways

| Aspect | Orthogonal | Non-Orthogonal | Builder Pattern |
|--------|-----------|----------------|-----------------|
| **Complexity** | Low | High | Medium |
| **Flexibility** | High | Limited | Very High |
| **Validation** | None/Simple | Complex/Scattered | Centralized |
| **Readability** | Good | Poor | Excellent |
| **Maintenance** | Easy | Difficult | Easy |
| **Extensibility** | Easy | Hard | Very Easy |

**Best Practices:**
1. Prefer orthogonal constructors for simple objects
2. Use Builder pattern for complex objects with constraints
3. Use Factory methods for specific constrained scenarios
4. Centralize validation logic
5. Make code self-documenting and readable

**When to Use What:**
- **Orthogonal Constructor**: Simple objects, no dependencies (Rectangle, Point)
- **Factory Methods**: Few specialized variations (createIntern, createManager)
- **Builder Pattern**: Complex objects, many optional parameters, multiple constraints (FlightBooking, DatabaseConnection)
