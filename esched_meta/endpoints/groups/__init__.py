import falcon

from esched_meta.endpoints.groups.create_group_endpoint import CreateGroupEndpoint

groups_api = falcon.API()

groups_api.add_route("/create", CreateGroupEndpoint)