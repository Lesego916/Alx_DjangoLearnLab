# Permissions & Groups

- **Permissions Defined**: can_view, can_create, can_edit, can_delete (in `Book` model).
- **Groups**:
  - **Viewers**: Assigned `can_view`.
  - **Editors**: Assigned `can_create` and `can_edit`.
  - **Admins**: Assigned all permissions.
- **Views**: Protected with `@permission_required`.
