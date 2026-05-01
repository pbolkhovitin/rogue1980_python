# Agent Workflow for Rogue 1980

## Process (per task from to-do list)
1. **Receive task** – from the to-do list (stages 0-7)
2. **Write minimal code** – implement the task without over-engineering
3. **Write tests** – cover edge cases, ensure >80% coverage for new code
4. **Run quality checks**:
   ```bash
   pytest
   mypy --strict src/
   black --check src/
   isort --check src/
5. Commit – with proper format: [stage N] short description
6. Proceed – to next task

## What Agent Must NOT Do
- Add functionality not specified in assignment
- Use external libraries beyond standard
- Premature optimization
- Add bonus features (tasks 6-9) unless explicitly requested for integration
- Create circular dependencies between layers

## Handling Unclear Requirements
1. Prefer explicit behavior from original Rogue 1980 (consult documentation)
2. If still unclear – ask via comment in code with # TODO: clarify
3. Do NOT guess when it affects core mechanics (hit formulas, enemy AI)