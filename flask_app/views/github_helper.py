from ghapi.all import *

class Sanity:
    def __init__(self, token=None):
        self.token = token

    def get_notifications(self, org):
        """Gets all notifications corresponding to Pull Requests and Issues."""
        return (GhApi(token=self.token).activity
                .list_notifications_for_authenticated_user(per_page=100))

    def get_comments(self, org, repo, issue_num):
        """Get the main comment body and a list of all subsequent comments"""
        g = GhApi(owner=org, repo=repo, token=self.token)
        return ' '.join(g.issues.list_comments(issue_num).map(lambda x: x.body) + [g.issues.get(issue_num).body])

    def get_threads(self, org):
        "Get a list of threads and their comments corresponding to notifications."
        return [{'comments': self.get_comments(org=n.repository.owner.login,
                                               repo=n.repository.name,
                                               issue_num=int(n.subject.url.split('/')[-1])),
                 'thread': int(n.url.split('/')[-1])} for n in self.get_notifications(org=org)]