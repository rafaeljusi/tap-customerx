# tap-customerx

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
- Pulls raw data from CustomerX's [REST API](https://doc.api.customerx.com.br/?version=latest)
- Extracts the following resources from CustomerX
  - [Clientes](https://doc.api.customerx.com.br/?version=latest#a0803301-389b-45d5-a77b-43d413e7534b)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state


---

Copyright &copy; 2019 Jusi
