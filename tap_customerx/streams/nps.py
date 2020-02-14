from tap_customerx.stream import CustomerXIterStream


class NPSStream(CustomerXIterStream):
    base_endpoint = 'net_promoter_scores'
    endpoint = 'net_promoter_scores'
    schema = 'nps'
    key_properties = ['id']
    state_field = 'date_send'
    pagination = True
    limit = 20

    def get_name(self):
        return self.schema

    def update_endpoint(self):
        self.endpoint = "{}?page={}&max_results={}".format(self.base_endpoint, self.start, self.limit)
