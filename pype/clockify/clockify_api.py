import os
import requests
import json
import datetime
import appdirs


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


class ClockifyAPI(metaclass=Singleton):
    endpoint = "https://api.clockify.me/api/"
    headers = {"X-Api-Key": None}
    app_dir = os.path.normpath(appdirs.user_data_dir('pype-app', 'pype'))
    file_name = 'clockify.json'
    fpath = os.path.join(app_dir, file_name)

    def set_api(self, api_key=None):
        if api_key is None:
            api_key = self.get_api_key()

        if api_key is not None and self.validate_api_key(api_key) is True:
            self.headers["X-Api-Key"] = api_key
            return True
        return False

    def validate_api_key(self, api_key):
        test_headers = {'X-Api-Key': api_key}
        action_url = 'workspaces/'
        response = requests.get(
            self.endpoint + action_url,
            headers=test_headers
        )
        if response.status_code != 200:
            return False
        return True

    def set_workspace(self, name=None):
        if name is None:
            self.workspace = None
            self.workspace_id = None
            return
        result = self.validate_workspace(name)
        if result is False:
            self.workspace = None
            self.workspace_id = None
            return False
        else:
            self.workspace = name
            self.workspace_id = result
            return True

    def validate_workspace(self, name):
        all_workspaces = self.get_workspaces()
        if name in all_workspaces:
            return all_workspaces[name]
        return False

    def get_api_key(self):
        api_key = None
        try:
            file = open(self.fpath, 'r')
            api_key = json.load(file).get('api_key', None)
            if api_key == '':
                api_key = None
        except Exception:
            file = open(self.fpath, 'w')
        file.close()
        return api_key

    def save_api_key(self, api_key):
        data = {'api_key': api_key}
        file = open(self.fpath, 'w')
        file.write(json.dumps(data))
        file.close()

    def get_workspaces(self):
        action_url = 'workspaces/'
        response = requests.get(
            self.endpoint + action_url,
            headers=self.headers
        )
        return {
            workspace["name"]: workspace["id"] for workspace in response.json()
        }

    def get_projects(self, workspace_name=None, workspace_id=None):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        action_url = 'workspaces/{}/projects/'.format(workspace_id)
        response = requests.get(
            self.endpoint + action_url,
            headers=self.headers
        )

        return {
            project["name"]: project["id"] for project in response.json()
        }

    def get_tags(
        self, workspace_name=None, workspace_id=None
    ):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        action_url = 'workspaces/{}/tags/'.format(workspace_id)
        response = requests.get(
            self.endpoint + action_url,
            headers=self.headers
        )

        return {
            tag["name"]: tag["id"] for tag in response.json()
        }

    def get_tasks(
        self,
        workspace_name=None, project_name=None,
        workspace_id=None, project_id=None
    ):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        project_id = self.convert_input(project_id, project_name, 'Project')
        action_url = 'workspaces/{}/projects/{}/tasks/'.format(
            workspace_id, project_id
        )
        response = requests.get(
            self.endpoint + action_url,
            headers=self.headers
        )

        return {
            task["name"]: task["id"] for task in response.json()
        }

    def get_workspace_id(self, workspace_name):
        all_workspaces = self.get_workspaces()
        if workspace_name not in all_workspaces:
            return None
        return all_workspaces[workspace_name]

    def get_project_id(
        self, project_name, workspace_name=None, workspace_id=None
    ):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        all_projects = self.get_projects(workspace_id=workspace_id)
        if project_name not in all_projects:
            return None
        return all_projects[project_name]

    def get_tag_id(self, tag_name, workspace_name=None, workspace_id=None):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        all_tasks = self.get_tags(workspace_id=workspace_id)
        if tag_name not in all_tasks:
            return None
        return all_tasks[tag_name]

    def get_task_id(
        self, task_name,
        project_name=None, workspace_name=None,
        project_id=None, workspace_id=None
    ):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        project_id = self.convert_input(project_id, project_name, 'Project')
        all_tasks = self.get_tasks(
            workspace_id=workspace_id, project_id=project_id
        )
        if task_name not in all_tasks:
            return None
        return all_tasks[task_name]

    def get_current_time(self):
        return str(datetime.datetime.utcnow().isoformat())+'Z'

    def start_time_entry(
        self, description, project_name=None, task_name=None,
        billable=True, workspace_name=None,
        project_id=None, task_id=None, workspace_id=None
    ):
        # Workspace
        workspace_id = self.convert_input(workspace_id, workspace_name)
        # Project
        project_id = self.convert_input(
            project_id, project_name, 'Project'
        )
        # Task
        task_id = self.convert_input(task_id, task_name, 'Task', project_id)

        # Check if is currently run another times and has same values
        current = self.get_in_progress(workspace_id=workspace_id)
        if current is not None:
            if (
                current.get("description", None) == description and
                current.get("projectId", None) == project_id and
                current.get("taskId", None) == task_id
            ):
                self.bool_timer_run = True
                return self.bool_timer_run
            self.finish_time_entry(workspace_id=workspace_id)

        # Convert billable to strings
        if billable:
            billable = 'true'
        else:
            billable = 'false'
        # Rest API Action
        action_url = 'workspaces/{}/timeEntries/'.format(workspace_id)
        start = self.get_current_time()
        body = {
            "start": start,
            "billable": billable,
            "description": description,
            "projectId": project_id,
            "taskId": task_id,
            "tagIds": None
        }
        response = requests.post(
            self.endpoint + action_url,
            headers=self.headers,
            json=body
        )

        success = False
        if response.status_code < 300:
            success = True
        return success

    def get_in_progress(self, workspace_name=None, workspace_id=None):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        action_url = 'workspaces/{}/timeEntries/inProgress'.format(
            workspace_id
        )
        response = requests.get(
            self.endpoint + action_url,
            headers=self.headers
        )
        try:
            output = response.json()
        except json.decoder.JSONDecodeError:
            output = None
        return output

    def finish_time_entry(self, workspace_name=None, workspace_id=None):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        current = self.get_in_progress(workspace_id=workspace_id)
        current_id = current["id"]
        action_url = 'workspaces/{}/timeEntries/{}'.format(
            workspace_id, current_id
        )
        body = {
            "start": current["timeInterval"]["start"],
            "billable": current["billable"],
            "description": current["description"],
            "projectId": current["projectId"],
            "taskId": current["taskId"],
            "tagIds": current["tagIds"],
            "end": self.get_current_time()
        }
        response = requests.put(
            self.endpoint + action_url,
            headers=self.headers,
            json=body
        )
        return response.json()

    def get_time_entries(
        self, quantity=10, workspace_name=None, workspace_id=None
    ):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        action_url = 'workspaces/{}/timeEntries/'.format(workspace_id)
        response = requests.get(
            self.endpoint + action_url,
            headers=self.headers
        )
        return response.json()[:quantity]

    def remove_time_entry(self, tid, workspace_name=None, workspace_id=None):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        action_url = 'workspaces/{}/timeEntries/{}'.format(
            workspace_id, tid
        )
        response = requests.delete(
            self.endpoint + action_url,
            headers=self.headers
        )
        return response.json()

    def add_project(self, name, workspace_name=None, workspace_id=None):
        workspace_id = self.convert_input(workspace_id, workspace_name)
        action_url = 'workspaces/{}/projects/'.format(workspace_id)
        body = {
            "name": name,
            "clientId": "",
            "isPublic": "false",
            "estimate": None,
            "color": None,
            "billable": None
        }
        response = requests.post(
            self.endpoint + action_url,
            headers=self.headers,
            json=body
        )
        return response.json()

    def add_workspace(self, name):
        action_url = 'workspaces/'
        body = {"name": name}
        response = requests.post(
            self.endpoint + action_url,
            headers=self.headers,
            json=body
        )
        return response.json()

    def convert_input(
        self, entity_id, entity_name, mode='Workspace', project_id=None
    ):
        if entity_id is None:
            error = False
            error_msg = 'Missing information "{}"'
            if mode.lower() == 'workspace':
                if entity_id is None and entity_name is None:
                    if self.workspace_id is not None:
                        entity_id = self.workspace_id
                    else:
                        error = True
                else:
                    entity_id = self.get_workspace_id(entity_name)
            else:
                if entity_id is None and entity_name is None:
                    error = True
                elif mode.lower() == 'project':
                    entity_id = self.get_project_id(entity_name)
                elif mode.lower() == 'task':
                    entity_id = self.get_task_id(
                        task_name=entity_name, project_id=project_id
                    )
                else:
                    raise TypeError('Unknown type')
            # Raise error
            if error:
                raise ValueError(error_msg.format(mode))

        return entity_id
