---
description: "Task list for console todo application implementation"
---

# Tasks: Console Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are based on the user stories from spec.md and implementation plan from plan.md.

  The tasks are organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  Each user story implementation includes models, services, and CLI components needed for that specific functionality.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 [P] Create src/models/ directory for data models
- [x] T003 [P] Create src/services/ directory for business logic
- [x] T004 [P] Create src/cli/ directory for command-line interface
- [x] T005 [P] Create src/lib/ directory for utility functions
- [x] T006 Create tests/unit/ directory for unit tests
- [x] T007 Create tests/integration/ directory for integration tests
- [x] T008 Create pyproject.toml with Python 3.13+ requirement
- [x] T009 Create README.md with usage instructions

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T010 [P] Create TodoItem model in src/models/todo_item.py with id, description, status, created_at properties
- [x] T011 [P] Create TodoList service in src/services/todo_service.py with basic data structure (dictionary)
- [x] T012 Create main application loop in src/cli/main.py with basic input/output
- [x] T013 Create command parser in src/lib/utils.py for splitting and validating commands
- [x] T014 Create error handling utilities in src/lib/utils.py for user-friendly messages
- [x] T015 Implement auto-incrementing ID counter in TodoList service
- [x] T016 Create TodoItem constructor with validation

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo Items (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list through the console interface

**Independent Test**: Can be fully tested by running the application, entering an "add" command with a task description, and verifying the task appears in the list when viewed

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [ ] T017 [P] [US1] Create unit test for TodoItem creation in tests/unit/test_todo_item.py
- [ ] T018 [P] [US1] Create unit test for add_item method in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [x] T019 [P] [US1] Implement add_item method in TodoList service in src/services/todo_service.py
- [x] T020 [P] [US1] Implement 'add' command handling in main.py in src/cli/main.py
- [x] T021 [US1] Add input validation for 'add' command in src/lib/utils.py
- [x] T022 [US1] Add success message formatting for added tasks in src/lib/utils.py
- [x] T023 [US1] Connect 'add' command to TodoList service in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View Todo Items (Priority: P1)

**Goal**: Enable users to see all their current todo items in a clear, readable format through the console interface

**Independent Test**: Can be fully tested by adding some tasks and then running the "view" or "list" command to display all tasks

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T024 [P] [US2] Create unit test for get_all_items method in tests/unit/test_todo_service.py
- [ ] T025 [P] [US2] Create unit test for display formatting in tests/unit/test_todo_service.py

### Implementation for User Story 2

- [x] T026 [P] [US2] Implement get_all_items method in TodoList service in src/services/todo_service.py
- [x] T027 [P] [US2] Implement get_pending_items method in TodoList service in src/services/todo_service.py
- [x] T028 [P] [US2] Implement get_completed_items method in TodoList service in src/services/todo_service.py
- [x] T029 [US2] Implement 'list' and 'view' command handling in main.py in src/cli/main.py
- [x] T030 [US2] Add display formatting for todo items in src/lib/utils.py (with [ ] for pending, [x] for completed)
- [x] T031 [US2] Connect 'list' command to TodoList service in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Complete Todo Items (Priority: P2)

**Goal**: Enable users to mark specific todo items as completed to track their progress through the console interface

**Independent Test**: Can be tested by adding tasks, marking one as complete, and verifying it shows as completed when viewing the list

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T032 [P] [US3] Create unit test for complete_item method in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [x] T033 [P] [US3] Implement complete_item method in TodoList service in src/services/todo_service.py
- [x] T034 [US3] Implement 'complete' command handling in main.py in src/cli/main.py
- [x] T035 [US3] Add input validation for 'complete' command (valid ID) in src/lib/utils.py
- [x] T036 [US3] Add success message formatting for completed tasks in src/lib/utils.py
- [x] T037 [US3] Connect 'complete' command to TodoList service in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---
## Phase 6: User Story 4 - Update Todo Items (Priority: P3)

**Goal**: Enable users to modify the description of existing todo items through the console interface

**Independent Test**: Can be tested by adding a task, updating its description, and verifying the change appears when viewing the list

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T038 [P] [US4] Create unit test for update_item method in tests/unit/test_todo_service.py

### Implementation for User Story 4

- [x] T039 [P] [US4] Implement update_item method in TodoList service in src/services/todo_service.py
- [x] T040 [US4] Implement 'update' command handling in main.py in src/cli/main.py
- [x] T041 [US4] Add input validation for 'update' command (valid ID and new description) in src/lib/utils.py
- [x] T042 [US4] Add success message formatting for updated tasks in src/lib/utils.py
- [x] T043 [US4] Connect 'update' command to TodoList service in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---
## Phase 7: User Story 5 - Delete Todo Items (Priority: P3)

**Goal**: Enable users to remove todo items they no longer need from their list through the console interface

**Independent Test**: Can be tested by adding tasks, deleting one, and verifying it no longer appears when viewing the list

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T044 [P] [US5] Create unit test for delete_item method in tests/unit/test_todo_service.py

### Implementation for User Story 5

- [x] T045 [P] [US5] Implement delete_item method in TodoList service in src/services/todo_service.py
- [x] T046 [US5] Implement 'delete' command handling in main.py in src/cli/main.py
- [x] T047 [US5] Add input validation for 'delete' command (valid ID) in src/lib/utils.py
- [x] T048 [US5] Add success message formatting for deleted tasks in src/lib/utils.py
- [x] T049 [US5] Connect 'delete' command to TodoList service in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Edge Cases & Error Handling (Cross-Story)

**Goal**: Implement comprehensive error handling for all edge cases identified in the specification

**Independent Test**: Each error case should be testable independently

### Tests for Error Handling (OPTIONAL - only if tests requested) ⚠️

- [ ] T050 [P] Create integration tests for edge cases in tests/integration/test_cli_flow.py

### Implementation for Error Handling

- [x] T051 [P] Implement validation for non-existent IDs in all commands in src/services/todo_service.py
- [x] T052 [P] Implement validation for empty input in command parser in src/lib/utils.py
- [x] T053 Implement handling for invalid commands in main.py in src/cli/main.py
- [x] T054 Add error messages for empty list scenarios in src/lib/utils.py
- [x] T055 Add support for special characters in todo descriptions in src/models/todo_item.py

**Checkpoint**: All error cases should be handled gracefully

---
## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T056 [P] Add 'help' command to display available commands in src/cli/main.py
- [x] T057 [P] Add 'quit' or 'exit' command to exit application in src/cli/main.py
- [x] T058 [P] Add type hints to all functions in src/models/todo_item.py, src/services/todo_service.py, src/cli/main.py, src/lib/utils.py
- [x] T059 [P] Add docstrings to all classes and functions in src/models/todo_item.py, src/services/todo_service.py, src/cli/main.py, src/lib/utils.py
- [x] T060 Add comprehensive error handling with user-friendly messages throughout the application
- [x] T061 [P] Create integration tests for complete user flows in tests/integration/test_cli_flow.py
- [x] T062 Update README.md with complete usage instructions from quickstart.md
- [x] T063 Run quickstart.md validation to ensure sample session works as expected

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Edge Cases (Phase 8)**: Depends on all user stories being implemented
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May depend on US1 for data
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May depend on US1 for data
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May depend on US1 for data

### Within Each User Story

- Models before services
- Services before endpoints/cli
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Create unit test for TodoItem creation in tests/unit/test_todo_item.py"
Task: "Create unit test for add_item method in tests/unit/test_todo_service.py"

# Launch all models for User Story 1 together:
Task: "Implement add_item method in TodoList service in src/services/todo_service.py"
Task: "Implement 'add' command handling in main.py in src/cli/main.py"
```

---
## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add functionality)
4. Complete Phase 4: User Story 2 (View functionality)
5. **STOP and VALIDATE**: Test adding and viewing tasks independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Add feature!)
3. Add User Story 2 → Test independently → Deploy/Demo (View feature!)
4. Add User Story 3 → Test independently → Deploy/Demo (Complete feature!)
5. Add User Story 4 → Test independently → Deploy/Demo (Update feature!)
6. Add User Story 5 → Test independently → Deploy/Demo (Delete feature!)
7. Add error handling → Test edge cases → Deploy/Demo
8. Add polish → Final validation → Complete application

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Add)
   - Developer B: User Story 2 (View)
   - Developer C: User Story 3 (Complete)
   - Developer D: User Stories 4 & 5 (Update & Delete)
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence