# tap-customerx

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
- Pulls raw data from CustomerX's [REST API](https://doc.api.customerx.com.br/?version=latest)
- Extracts the following resources from CustomerX
  - [Clientes](https://doc.api.customerx.com.br/?version=latest#a0803301-389b-45d5-a77b-43d413e7534b)
  - [NPS](https://doc.api.customerx.com.br/?version=latest#4655df85-aae7-47c8-a7d4-4def0494c956)
  - [Tasks](https://doc.api.customerx.com.br/?version=latest#a5412030-4ace-4ded-8e90-95ccc4f1725b)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## setup

1. Install the tap
`pip install -e .`

2. Install the target
`pip install target-stitch`

3. Create and edit the tap config file (tap_config.json)
```
{
    "api_token": "YOUR_API_TOKEN",
    "start_date": "2017-01-01T00:00:00Z"
}
```

4. Create and edit the target config file (target_config.json)
```
{
    "client_id" : YOUR_CLIENT_ID,
    "token" : "YOUR_TOKEN",
    "small_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "big_batch_url": "https://api.stitchdata.com/v2/import/batch",
    "batch_size_preferences": {}
}
```

5. Generate the catalog.json file
`tap-customerx --config tap_config.json --discover > catalog.json`


## Run
`tap-customerx --config tap_config.json --catalog catalog.json | target-stitch --config target_config.json >> state.json`



---

Copyright &copy; 2019 Jusi
