# NEP Dual Timetable Generator — Starter Project

## Overview
Generates **student** and **faculty** timetables under NEP-like flexible curricula.
Uses OR-Tools for baseline constraint solving and a simple PPO RL agent for soft optimization.
As of the NEP extension, the pipeline understands:
- course credit metadata (Major/Minor/Skill tracks, theory/practicum splits)
- group-level credit minima/maxima per track
- room capacity vs. enrolled headcount
- teaching-practice flags and optional scheduling windows
- richer JSON outputs (assignments annotated with credits, tracks, components)

## Setup
1. Create venv and activate.
2. pip install -r requirements.txt

## Run demo

### Command Line
```bash
python run_demo.py
```

### Streamlit Web Interface
```bash
streamlit run app.py
```

The Streamlit app provides:
- **Load Data**: Use default data or upload custom JSON files
- **Edit Data**: Modify data directly in the interface
- **Generate Timetable**: Generate optimized timetables with adjustable time limit
- **View Results**: See assignments, student timetables, faculty timetables, and violations
- **Download**: Download results as JSON files

The app will open at `http://localhost:8501`

## Input schema (dummy data lives under `timetable_ai/dummy_data/`)
- `slots.json`: canonical list of slot identifiers used everywhere.
- `courses.json`: each entry now includes `credit_hours`, `course_track`, `components`, `student_groups`, `possible_faculty`, and optional `teaching_practice_required`.
- `faculty.json`: availability window, expertise list, max hours, now extended to cover additional slots per NEP loads.
- `rooms.json`: capacity, type (theory/lab) used for suitability and headcount checks.
- `groups.json`: for each cohort provide majors/minors, credit requirements, and a per-track list of course choices (acts as track overrides when validating credits).
- `students.json`: individual roster per group (consumed to build per-student timetables).

To run a different scenario, swap these JSON files or point `DualTimetableManager` at another data payload with the same schema.

Outputs saved under `out/`:
- `demo_baseline_assignments.json`: slot → sessions annotated with course track, credit load, components, and assigned faculty.
- `demo_baseline_students.json`: student → slot → course code (baseline timetable).
- `demo_baseline_faculty.json`: faculty → slot → course code.
- `demo_baseline_violations.json`: validator findings (credits, capacities, conflicts, teaching-practice windows, etc.).
- `ppo_timetable_demo.zip`: PPO weights trained on the baseline timetable.

## How it works
1. `StudentScheduler` creates baseline course-slot-room assignments (student-centric).
2. `FacultyOptimizer` assigns faculties and balances loads.
3. `DualTimetableManager` orchestrates and validates outputs.
4. `rl_agent` contains a simple Gym env + PPO training loop to fine-tune assignments.

## Next steps
- Expand constraints in StudentScheduler for NEP specifics (majors/minors, cross-listed courses).
- Add explicit faculty decision variables in the CP model for stronger joint optimization.
- Replace simple RL env with richer state/action design (faculty & room encoding).
