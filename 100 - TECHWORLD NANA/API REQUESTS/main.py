import requests
response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
# I did a request with the "get" command
my_projects = response.json()
# i save the response in the "my_projects" variable

# print the whole objects list
print(my_projects)
print(type(my_projects))

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")

#Information: google search "gitlab api documentation"

