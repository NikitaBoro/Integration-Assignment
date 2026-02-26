import argparse
from auth import register,login
from tickets import create_ticket,list_tickets,edit_ticket

parser = argparse.ArgumentParser(description="Ticket Management CLI")

subparsers = parser.add_subparsers(dest="command")

# auth commands
register_cmd = subparsers.add_parser("register")
register_cmd.add_argument("--username", required=True)
register_cmd.add_argument("--password", required=True)

login_cmd = subparsers.add_parser("login")
login_cmd.add_argument("--username", required=True)
login_cmd.add_argument("--password", required=True)

## tickets commands:
#create ticket:
create_ticket_cmd = subparsers.add_parser("create_ticket")
create_ticket_cmd.add_argument("--username", required=True)
create_ticket_cmd.add_argument("--password", required=True)
create_ticket_cmd.add_argument("--title", required=True)
create_ticket_cmd.add_argument("--description", required=False)
create_ticket_cmd.add_argument("--dependsOn", nargs="*")

#list tickets:
list_ticket_cmd = subparsers.add_parser("list_tickets")
list_ticket_cmd.add_argument("--username", required=True)
list_ticket_cmd.add_argument("--password", required=True)
list_ticket_cmd.add_argument("--limit", type=int, default=5)

#edit ticket
edit_ticket_cmd = subparsers.add_parser("edit_ticket")
edit_ticket_cmd.add_argument("--username", required=True)
edit_ticket_cmd.add_argument("--password", required=True)
edit_ticket_cmd.add_argument("--ref", required=True)
edit_ticket_cmd.add_argument("--title", required=False)
edit_ticket_cmd.add_argument("--description", required=False)
edit_ticket_cmd.add_argument("--dependsOn", nargs="*")


args = parser.parse_args()

if args.command == "register":
    result = register(args.username, args.password)
    print("Register response:", result)
elif args.command == "login":
    result = login(args.username, args.password)
    print("Login response:", result)
elif args.command == "create_ticket":
    result = create_ticket(args.username, args.password,args.title, args.description,args.dependsOn)
    print("Create ticket response:", result)
elif args.command == "list_tickets":
    result = list_tickets(args.username, args.password,args.limit)
    print("List tickets response:", result)
elif args.command == "edit_ticket":
    result = edit_ticket(args.username, args.password,args.ref,args.title, args.description,args.dependsOn)
    print("Edit ticket response:", result)