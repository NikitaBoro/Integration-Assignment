# Integration Assignment

A command-line interface (CLI) application that integrates with the TicketForge API.

The application allows users to:
- Register
- Create tickets
- Edit existing tickets
- List their tickets

All interactions are performed directly from the terminal.

---

## Installation

1. Clone the repository:

git clone <repository-url>
cd integration-assignment

2. Install dependencies:

pip install -r requirements.txt

---

## Usage

All commands follow this structure:

python3 app.py <command> [arguments]

---

# Commands

---

## Register

Registers a new user.

python3 app.py register --username USER --password PASS

Required arguments:
- `--username`
- `--password`

---


## Create Ticket

Creates a new ticket.

python3 app.py create_ticket --username USER --password PASS --title "Ticket title"

Required arguments:
- `--username`
- `--password`
- `--title`

Optional arguments:
- `--description "Ticket description"`
- `--dependsOn REF REF ...`

Example:

python3 app.py create_ticket --username test --password test123 --title "New Ticket" --description "Ticket description" --dependsOn TF-220 TF-221

---

## Edit Ticket

Updates an existing ticket using its reference number.

python3 app.py edit_ticket --username USER --password PASS --ref REF

Required arguments:
- `--username`
- `--password`
- `--ref`

Optional arguments:
- `--title "Updated title"`
- `--description "Updated description"`
- `--dependsOn REF REF ...`

Example:

python3 app.py edit_ticket --username test --password test123 --ref TF-220 --title "Updated title"

---

## List Tickets

Lists the user's tickets.

python3 app.py list_tickets --username USER --password PASS

Optional arguments:
- `--limit NUMBER` (default: 5)

Example:

python3 app.py list_tickets --username test --password test123 --limit 10

---

# Future Improvements

- Persist authenticated session instead of passing credentials in every command
- Improve CLI output formatting for better readability
- Add automated unit tests
- Add logging support
- Improve input validation and error formatting
