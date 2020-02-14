#!/usr/bin/env python3

import singer
import json
import sys
from tap_customerx.tap import CustomerXTap


logger = singer.get_logger()


def main_impl():
    args = singer.utils.parse_args(['api_token', 'start_date'])

    customerx_tap = CustomerXTap(args.config, args.state)

    if args.discover:
        catalog = customerx_tap.do_discover()
        json.dump(catalog.to_dict(), sys.stdout, indent=2)
        logger.info('Finished discover')
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = customerx_tap.do_discover()
        customerx_tap.do_sync(catalog)


def main():
    try:
        main_impl()
    except Exception as e:
        logger.critical(e)
        raise e


if __name__ == '__main__':
    main()
