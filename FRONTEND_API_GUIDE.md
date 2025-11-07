# Frontend API Integration Guide

Complete guide for frontend developers to integrate with the NEP Timetable Generator API.

## Base URL

**Production:** `https://your-app.onrender.com`  
**Local:** `http://localhost:5000`

---

## API Endpoints

### 1. Health Check
**GET** `/health`

Check if the API is running.

**Request:**
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "NEP Timetable Generator API",
  "timestamp": "2024-11-07T19:30:00"
}
```

---

### 2. API Information
**GET** `/api/info`

Get detailed API documentation and schema.

**Request:**
```http
GET /api/info
```

**Response:**
```json
{
  "service": "NEP Timetable Generator API",
  "version": "1.0.0",
  "endpoints": {...},
  "input_schema": {...},
  "output_schema": {...}
}
```

---

### 3. Validate Input
**POST** `/api/validate`

Validate input JSON structure without generating timetable.

**Request:**
```http
POST /api/validate
Content-Type: application/json

{
  "time_slots": [...],
  "courses": [...],
  "faculty": [...],
  "rooms": [...],
  "student_groups": [...]
}
```

**Response (Valid):**
```json
{
  "valid": true,
  "message": "Input structure is valid",
  "timestamp": "2024-11-07T19:30:00"
}
```

**Response (Invalid):**
```json
{
  "valid": false,
  "errors": ["Missing required fields: courses"],
  "timestamp": "2024-11-07T19:30:00"
}
```

---

### 4. Generate Timetable ⭐ (Main Endpoint)
**POST** `/api/generate`

Generate timetable from JSON input.

**Request:**
```http
POST /api/generate
Content-Type: application/json

{
  "time_slots": [...],
  "courses": [...],
  "faculty": [...],
  "rooms": [...],
  "student_groups": [...],
  "time_limit": 10  // optional
}
```

**Response (Success):**
```json
{
  "success": true,
  "assignments": {...},
  "student_timetables": {...},
  "faculty_timetables": {...},
  "violations": [],
  "metadata": {
    "time_slots_used": 14,
    "students_scheduled": 4,
    "faculty_assigned": 5,
    "violations_count": 0,
    "time_limit_used": 10
  },
  "message": "Timetable generated successfully",
  "timestamp": "2024-11-07T19:30:00"
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Error message",
  "message": "Human-readable message",
  "timestamp": "2024-11-07T19:30:00"
}
```

---

## Complete Input Schema

### Required Fields

#### 1. `time_slots` (Array of Strings)
List of all available time slots.

```json
"time_slots": [
  "Mon_09", "Mon_10", "Mon_11", "Mon_12",
  "Tue_09", "Tue_10", "Tue_11", "Tue_12",
  "Wed_09", "Wed_10", "Wed_11", "Wed_12",
  "Thu_09", "Thu_10", "Thu_11", "Thu_12",
  "Fri_09", "Fri_10", "Fri_11", "Fri_12"
]
```

**Format:** `Day_Hour` (e.g., "Mon_09" = Monday 9 AM)

---

#### 2. `courses` (Array of Objects)
List of all courses to be scheduled.

```json
"courses": [
  {
    "course_code": "DSA",                    // Required: Unique course identifier
    "name": "Data Structures & Algorithms",  // Optional: Full course name
    "credit_hours": 4,                       // Required: Total credit hours
    "course_track": "Major",                 // Required: "Major" | "Minor" | "Skill" | "Elective"
    "components": {                          // Required: Breakdown of hours
      "theory": 3,
      "lab": 1
    },
    "student_groups": ["G1"],                // Required: Which groups take this course
    "possible_faculty": ["F001", "F004"],    // Optional: Preferred faculty IDs
    "lab_required": true,                    // Optional: If true, needs lab room
    "teaching_practice_required": false      // Optional: For B.Ed programs
  }
]
```

**Required Fields:**
- `course_code` (string)
- `credit_hours` (integer)
- `course_track` (string)
- `components` (object)
- `student_groups` (array)

**Optional Fields:**
- `name` (string)
- `possible_faculty` (array of strings)
- `lab_required` (boolean)
- `teaching_practice_required` (boolean)

---

#### 3. `faculty` (Array of Objects)
List of all faculty members.

```json
"faculty": [
  {
    "faculty_id": "F001",                    // Required: Unique faculty identifier
    "name": "Dr. Alpha",                     // Optional: Faculty name
    "expertise": ["DSA", "SSP"],             // Required: Courses they can teach
    "available_slots": [                     // Required: When they're available
      "Mon_09", "Mon_10", "Tue_09", 
      "Wed_09", "Thu_09"
    ],
    "max_hours_per_week": 10                 // Required: Maximum teaching hours
  }
]
```

**Required Fields:**
- `faculty_id` (string)
- `expertise` (array of course codes)
- `available_slots` (array of slot strings)
- `max_hours_per_week` (integer)

**Optional Fields:**
- `name` (string)

---

#### 4. `rooms` (Array of Objects)
List of all available rooms.

```json
"rooms": [
  {
    "room_id": "R101",                       // Required: Unique room identifier
    "type": "theory",                        // Required: "theory" | "lab"
    "capacity": 60,                          // Required: Maximum students
    "available_slots": [                     // Required: When room is available
      "Mon_09", "Mon_10", "Mon_11", "Mon_12",
      "Tue_09", "Tue_10", "Tue_11", "Tue_12"
    ]
  },
  {
    "room_id": "LAB1",
    "type": "lab",
    "capacity": 32,
    "available_slots": [
      "Mon_11", "Mon_12", "Tue_11", "Tue_12"
    ]
  }
]
```

**Required Fields:**
- `room_id` (string)
- `type` (string: "theory" or "lab")
- `capacity` (integer)
- `available_slots` (array of slot strings)

---

#### 5. `student_groups` (Array of Objects)
List of student groups/cohorts.

```json
"student_groups": [
  {
    "group_id": "G1",                        // Required: Unique group identifier
    "program": "B.Tech CS",                  // Optional: Program name
    "semester": 3,                           // Optional: Semester number
    "major": "Computer Science",             // Optional: Major subject
    "minor": "Artificial Intelligence",      // Optional: Minor subject
    "credit_requirements": {                 // Optional: Credit constraints
      "min": 11,
      "max": 20,
      "major_min": 7,
      "minor_min": 3,
      "skill_min": 1
    },
    "students": ["S001", "S002", "S003"],   // Required: List of student IDs
    "course_choices": {                      // Required: Courses they can take
      "major": ["DSA", "OS", "CN"],
      "minor": ["ML"],
      "skill": ["SSP"]
    }
  }
]
```

**Required Fields:**
- `group_id` (string)
- `students` (array of student IDs)
- `course_choices` (object with track arrays)

**Optional Fields:**
- `program` (string)
- `semester` (integer)
- `major` (string)
- `minor` (string)
- `credit_requirements` (object)

---

#### 6. `time_limit` (Integer, Optional)
Solver time limit in seconds. Default: 10

```json
"time_limit": 10
```

---

## Complete Example Request

```json
{
  "time_slots": [
    "Mon_09", "Mon_10", "Mon_11", "Mon_12",
    "Tue_09", "Tue_10", "Tue_11", "Tue_12",
    "Wed_09", "Wed_10", "Wed_11", "Wed_12",
    "Thu_09", "Thu_10", "Thu_11", "Thu_12",
    "Fri_09", "Fri_10", "Fri_11", "Fri_12"
  ],
  "courses": [
    {
      "course_code": "DSA",
      "name": "Data Structures & Algorithms",
      "credit_hours": 4,
      "course_track": "Major",
      "components": {"theory": 3, "lab": 1},
      "student_groups": ["G1"],
      "possible_faculty": ["F001", "F004"],
      "lab_required": true
    },
    {
      "course_code": "OS",
      "name": "Operating Systems",
      "credit_hours": 3,
      "course_track": "Major",
      "components": {"theory": 3},
      "student_groups": ["G1"],
      "possible_faculty": ["F002", "F005"]
    }
  ],
  "faculty": [
    {
      "faculty_id": "F001",
      "name": "Dr. Alpha",
      "expertise": ["DSA", "SSP"],
      "available_slots": ["Mon_09", "Mon_10", "Tue_09", "Wed_09", "Thu_09"],
      "max_hours_per_week": 10
    },
    {
      "faculty_id": "F002",
      "name": "Dr. Beta",
      "expertise": ["OS", "ML"],
      "available_slots": ["Mon_11", "Mon_12", "Tue_11", "Tue_12", "Wed_10", "Wed_11"],
      "max_hours_per_week": 12
    }
  ],
  "rooms": [
    {
      "room_id": "R101",
      "type": "theory",
      "capacity": 60,
      "available_slots": ["Mon_09", "Mon_10", "Mon_11", "Mon_12", "Tue_09", "Tue_10"]
    },
    {
      "room_id": "LAB1",
      "type": "lab",
      "capacity": 32,
      "available_slots": ["Mon_11", "Mon_12", "Tue_11", "Tue_12", "Wed_11", "Wed_12"]
    }
  ],
  "student_groups": [
    {
      "group_id": "G1",
      "program": "B.Tech CS",
      "semester": 3,
      "major": "Computer Science",
      "minor": "Artificial Intelligence",
      "credit_requirements": {
        "min": 11,
        "max": 20,
        "major_min": 7,
        "minor_min": 3,
        "skill_min": 1
      },
      "students": ["S001", "S002", "S003", "S004"],
      "course_choices": {
        "major": ["DSA", "OS", "CN"],
        "minor": ["ML"],
        "skill": ["SSP"]
      }
    }
  ],
  "time_limit": 10
}
```

---

## Frontend Integration Examples

### JavaScript (Fetch API)

```javascript
// Generate Timetable
async function generateTimetable(inputData) {
  try {
    const response = await fetch('https://your-app.onrender.com/api/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(inputData)
    });
    
    const result = await response.json();
    
    if (result.success) {
      console.log('Timetable generated!');
      console.log('Assignments:', result.assignments);
      console.log('Student Timetables:', result.student_timetables);
      console.log('Violations:', result.violations);
      return result;
    } else {
      console.error('Error:', result.error);
      return null;
    }
  } catch (error) {
    console.error('Network error:', error);
    return null;
  }
}

// Validate Input
async function validateInput(inputData) {
  const response = await fetch('https://your-app.onrender.com/api/validate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(inputData)
  });
  
  return await response.json();
}

// Health Check
async function checkHealth() {
  const response = await fetch('https://your-app.onrender.com/api/health');
  return await response.json();
}
```

### React Example

```jsx
import { useState } from 'react';

function TimetableGenerator() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const generateTimetable = async (inputData) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('https://your-app.onrender.com/api/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(inputData)
      });
      
      const data = await response.json();
      
      if (data.success) {
        setResult(data);
      } else {
        setError(data.error || data.message);
      }
    } catch (err) {
      setError('Network error: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button 
        onClick={() => generateTimetable(yourInputData)}
        disabled={loading}
      >
        {loading ? 'Generating...' : 'Generate Timetable'}
      </button>
      
      {error && <div className="error">{error}</div>}
      
      {result && (
        <div>
          <h3>Generated Timetable</h3>
          <p>Time Slots Used: {result.metadata.time_slots_used}</p>
          <p>Violations: {result.metadata.violations_count}</p>
          {/* Display assignments, timetables, etc. */}
        </div>
      )}
    </div>
  );
}
```

### Python (requests)

```python
import requests

def generate_timetable(input_data):
    url = "https://your-app.onrender.com/api/generate"
    response = requests.post(url, json=input_data)
    
    if response.status_code == 200:
        result = response.json()
        if result['success']:
            return result
        else:
            print(f"Error: {result['error']}")
            return None
    else:
        print(f"HTTP Error: {response.status_code}")
        return None
```

---

## Response Structure

### Success Response

```json
{
  "success": true,
  "assignments": {
    "Mon_09": [
      {
        "course_code": "DSA",
        "course_name": "Data Structures & Algorithms",
        "room_id": "R101",
        "faculty_id": "F001",
        "course_track": "Major",
        "credit_hours": 4,
        "components": {"theory": 3, "lab": 1}
      }
    ]
  },
  "student_timetables": {
    "S001": {
      "Mon_09": "DSA",
      "Tue_10": "OS"
    }
  },
  "faculty_timetables": {
    "F001": {
      "Mon_09": "DSA"
    }
  },
  "violations": [],
  "metadata": {
    "time_slots_used": 14,
    "students_scheduled": 4,
    "faculty_assigned": 5,
    "violations_count": 0,
    "time_limit_used": 10
  },
  "message": "Timetable generated successfully",
  "timestamp": "2024-11-07T19:30:00"
}
```

---

## Error Handling

### HTTP Status Codes

- `200` - Success
- `400` - Bad Request (invalid input, missing fields)
- `404` - Not Found (invalid endpoint)
- `405` - Method Not Allowed
- `500` - Internal Server Error

### Error Response Format

```json
{
  "success": false,
  "error": "Error type",
  "message": "Human-readable error message",
  "timestamp": "2024-11-07T19:30:00"
}
```

---

## Important Notes

1. **Content-Type**: Always set `Content-Type: application/json` header
2. **CORS**: API has CORS enabled, so frontend can call from any domain
3. **Timeout**: Generation may take 10-60 seconds depending on complexity
4. **Violations**: Check `violations` array - empty means no conflicts
5. **Time Limit**: Increase `time_limit` for complex schedules (more courses/faculty)

---

## Quick Reference

| Endpoint | Method | Purpose | Input Required |
|----------|--------|---------|----------------|
| `/` | GET | API info | None |
| `/health` | GET | Health check | None |
| `/api/info` | GET | API documentation | None |
| `/api/validate` | POST | Validate input | Full input JSON |
| `/api/generate` | POST | Generate timetable | Full input JSON |

---

For more details, see `README_FLASK.md` or call `/api/info` endpoint.

