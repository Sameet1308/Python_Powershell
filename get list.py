from mstrio.connection import Connection
from mstrio.project import list_projects

# Connect to the MicroStrategy server
conn = Connection(base_url="http://your-microstrategy-server/MicroStrategyLibrary/api",
                  username="your_username",
                  password="your_password",
                  login_mode=1)  # Adjust the login_mode if necessary
conn.connect()

# Fetch and list projects
projects = list_projects(connection=conn)
for project in projects:
    print(f"Project Name: {project.name}, ID: {project.id}")

# Disconnect
conn.close()