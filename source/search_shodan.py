#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import shodan

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

YOUR_API_KEY = raw_input('input your API key')
SHODAN_API_KEY = YOUR_API_KEY

api = shodan.Shodan(SHODAN_API_KEY)
# Wrap the request in a try/ except block to catch errors
try:
        search_what = raw_input('Search what?')
        # Search Shodan
        results = api.search(search_what)

        # Show the results
        f = open('result' + '.txt', 'a')
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
                f.write(result['data'])
        f.close()
except shodan.APIError, e:
        print 'Error: %s' % e