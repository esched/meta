import falcon


class CreateGroupEndpoint:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Group created"
