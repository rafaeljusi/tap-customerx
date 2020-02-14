from tap_customerx.stream import CustomerXIterStream


class TasksStream(CustomerXIterStream):
    base_endpoint = 'tasks'
    endpoint = 'tasks'
    schema = 'tasks'
    key_properties = ['id']
    state_field = 'updated_at'
    pagination = True
    limit = 20

    def get_name(self):
        return self.schema

    def update_endpoint(self):
        self.endpoint = "{}?created_at={}&updated_at={}&page={}&max_results={}".format(self.base_endpoint, self.initial_state.strftime('%Y-%m-%d'), self.earliest_state.strftime('%Y-%m-%d'), self.start, self.limit)
