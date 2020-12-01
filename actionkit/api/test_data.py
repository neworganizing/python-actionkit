TEST_DATA = {
    'actions': {
        '/rest/v1/donationaction/999999226/': { #fake action_url
            'res': 200,
             #some fields removed for brevity.
             # add them back if you need them for testing
            'action': {
                'akid': '.401.-9Mop1',
                'created_at': '1999-10-13T17:07:00',
                'created_user': False,
                'fields': {

                },
                'id': 1,
                'ip_address': None,
                'is_forwarded': False,
                'link': None,
                'mailing': None,
                'opq_id': '',
                'page': '/rest/v1/importpage/12/',
                'referring_mailing': None,
                'referring_user': None,
                'resource_uri': '/rest/v1/importaction/1/',
                'source': 'initial_ak_import',
                'status': 'complete',
                'subscribed_user': False,
                'taf_emails_sent': None,
                'type': 'Import',
                'updated_at': '2015-09-23T02:21:30',
                'user': '/rest/v1/user/401/'
            }
        },
    },
    'orders_recurring': {
        "get_orderrecurring_detail": {
            'res': None,
            "account": "Test Account",
            "action":"/rest/v1/donationaction/999999226/",
            "amount":"1.12",
            "amount_converted":"1.12",
            "card_num":"1111",
            "created_at":"2020-04-23T20:42:55",
            "currency":"USD",
            "exp_date":"0822",
            "id":999114,
            "order":{
                "account":"MoveOn.org Political Action",
                "action":"/rest/v1/donationaction/999999226/",
                "card_num_last_four":"3676",
                "created_at":"2020-04-23T20:42:55",
                "currency":"USD",
                "id":99999527,
                "import_id":"None",
                "orderdetails":[

                ],
                "orderrecurrings":[
                    "/rest/v1/orderrecurring/999114/"
                ],
                "payment_method":"cc",
                "resource_uri":"/rest/v1/order/99999527/",
                "reverse":"/rest/v1/order/99999527/reverse/",
                "shipping_address":"None",
                "status":"completed",
                "total":"1.12",
                "total_converted":"1.12",
                "transactions":[
                    "/rest/v1/transaction/99999745/",
                    "/rest/v1/transaction/99999746/",
                    "/rest/v1/transaction/99999830/"
                ],
                "updated_at":"2020-04-23T20:42:59",
                "user":"/rest/v1/user/99999835/",
                "user_detail":"/rest/v1/orderuserdetail/99999000/"
            },
            "period":"months",
            "recurring_id":"z9zzzz",
            "resource_uri":"/rest/v1/orderrecurring/999114/",
            "start":"2020-05-23",
            "status":"canceled_by_admin",
            "updated_at":"2020-04-23T23:02:39",
            "user":"/rest/v1/user/99999835/",
            "user_detail":{
                "address1":"123 Main St",
                "address2":"",
                "city":"Any City",
                "country":"United States",
                "created_at":"2020-04-23T20:42:55",
                "email":"test@example.com",
                "first_name":"Testy",
                "id":99999000,
                "last_name":"Test",
                "middle_name":"",
                "orders":[
                    "/rest/v1/order/99999527/"
                ],
                "plus4":"4052",
                "postal":"99999-4052",
                "prefix":"",
                "region":"AZ",
                "resource_uri":"/rest/v1/orderuserdetail/99999000/",
                "source":"",
                "state":"AZ",
                "suffix":"",
                "updated_at":"2020-04-23T20:42:55",
                "zip":"99999"
            }
        },
        "123123": {
            "res": None,
            "orders_recurring":[
                {
                    "account":"Test Account",
                    "action":"/rest/v1/donationaction/999999226/",
                    "amount":"1.12",
                    "amount_converted":"1.12",
                    "card_num":"1111",
                    "created_at":"2020-04-23T20:42:55",
                    "currency":"USD",
                    "exp_date":"0822",
                    "id":999114,
                    "order":"/rest/v1/order/99999527/",
                    "period":"months",
                    "recurring_id":"z9zzzz",
                    "resource_uri":"/rest/v1/orderrecurring/999114/",
                    "start":"2020-05-23",
                    "status":"canceled_by_admin",
                    "updated_at":"2020-04-23T23:02:39",
                    "user":"/rest/v1/user/99999835/"
                },
                  {
                    'account': 'MoveOn.org Civic Action PayPal',
                    'action': '/rest/v1/donationaction/303552744/',
                    'amount': '1.00',
                    'amount_converted': '1.00',
                    'card_num': '',
                    'created_at': '2019-05-15T18:09:00',
                    'currency': 'USD',
                    'exp_date': '',
                    'id': 269681,
                    'order': '/rest/v1/order/20878367/',
                    'period': 'months',
                    'recurring_id': None,
                    'resource_uri': '/rest/v1/orderrecurring/269681/',
                    'start': '2019-06-15',
                    'status': 'active',
                    'updated_at': '2019-05-15T18:09:02',
                    'user': '/rest/v1/user/18715613/'
                  },
                  {
                    'account': 'MoveOn.org Political Action',
                    'action': '/rest/v1/donationaction/304419112/',
                    'amount': '1.00',
                    'amount_converted': '1.00',
                    'card_num': '5644',
                    'created_at': '2019-05-21T13:50:54',
                    'currency': 'USD',
                    'exp_date': '0922',
                    'id': 270123,
                    'order': '/rest/v1/order/20893040/',
                    'period': 'months',
                    'recurring_id': 'jm3m26',
                    'resource_uri': '/rest/v1/orderrecurring/270123/',
                    'start': '2019-06-21',
                    'status': 'canceled_by_user',
                    'updated_at': '2019-05-21T13:55:55',
                    'user': '/rest/v1/user/18715613/',
                  }
            ]
        },
        "update_orderrecurring_status": {
            'res': None,
            'success': True
        }
    },
    'phones': {
        'fake_id': '8675309', #update below, where search by id is facilitated
        'fake_url': '/rest/v1/phone/8675309/', #update below, where search by url is facilitated
        '/rest/v1/phone/8675309/': { #phone url
            'res': None,
            'phone': {
                "created_at": "2015-11-24T21:07:58",
                "id": "8675309",
                "normalized_phone": "5558675309",
                "phone": "5558675309",
                "resource_uri": "/rest/v1/phone/8675309/",
                "source": "user",
                "type": "home",
                "updated_at": "2016-03-29T16:41:10",
                "user": "/rest/v1/user/123123/"
            }
        },
        '8675309': { #phone id
            'res': 200,
            'phone': {
                "created_at": "2015-11-24T21:07:58",
                "id": "8675309",
                "normalized_phone": "5558675309",
                "phone": "5558675309",
                "resource_uri": "/rest/v1/phone/8675309/",
                "source": "user",
                "type": "home",
                "updated_at": "2016-03-29T16:41:10",
                "user": "/rest/v1/user/123123/"
            }
        },
    },
    'users': {
        'fake_id': '123123', #update below, where search by id is facilitated
        'fake_email': 'example@example.com', #update below, where search by email is facilitated
        'create_user': {
            'res': None,
            'id': "123123",
        },
        'example@example.com': { #user email address
            'res': None,
            'id': "123123",
        },
        '123123': { #userid
            'res': 200,
             #some fields removed for brevity.
             # add them back if you need them for testing
            'user': {
                "address1": "123 Main St.",
                "address2": "",
                "city": "Cleveland",
                "country": "United States",
                "created_at": "2015-11-18T16:22:31",
                "do_not_call": "True",
                "email": "example@example.com",
                "employer": "Ringling Bros",
                "fields": {},
                "first_name": "Joey",
                "last_name": "AndMe",
                "middle_name": "Annabelle",
                "id": "123123",
                "occupation": "balloon artist",
                'orders': [
                    {
                        'account': 'MoveOn.org Civic Action PayPal',
                        'action': '/rest/v1/donationaction/303552367/',
                        'card_num_last_four': '',
                        'created_at': '2019-05-15T17:44:00',
                        'currency': 'USD',
                        'id': '20878360',
                        'import_id': None,
                        'orderdetails': [],
                        'orderrecurrings': [],
                        'payment_method': 'paypal',
                        'resource_uri': '/rest/v1/order/20878360/',
                        'shipping_address': None,
                        'status': 'incomplete',
                        'total': '1.00',
                        'total_converted': '1.00',
                        'transactions': [
                            '/rest/v1/transaction/26134025a/'
                        ],
                        'updated_at': '2019-05-15T17:44:01',
                        'user': '/rest/v1/user/123123/',
                        'user_detail': '/rest/v1/orderuserdetail/20878741/'
                    },
                    {
                        'account': 'MoveOn.org Civic Action PayPal',
                        'action': '/rest/v1/donationaction/303552368/',
                        'card_num_last_four': '',
                        'created_at': '2020-12-30T17:44:01', #most recent order
                        'currency': 'USD',
                        'id': '20878361',
                        'import_id': None,
                        'orderdetails': [],
                        'orderrecurrings': [],
                        'payment_method': 'paypal',
                        'resource_uri': '/rest/v1/order/20878361/',
                        'shipping_address': None,
                        'status': 'incomplete',
                        'total': '1.00',
                        'total_converted': '1.00',
                        'transactions': [
                            '/rest/v1/transaction/26134026/'
                        ],
                        'updated_at': '2019-05-15T17:44:02',
                        'user': '/rest/v1/user/123123/',
                        'user_detail': '/rest/v1/orderuserdetail/20878742a/'
                    },
                    {
                        'account': 'MoveOn.org Civic Action',
                        'action': '/rest/v1/donationaction/335959703/',
                        'card_num_last_four': '5644',
                        'created_at': '2020-01-15T22:29:15',
                        'currency': 'USD',
                        'id': '21287927',
                        'import_id': None,
                        'orderdetails': [],
                        'orderrecurrings': [
                            '/rest/v1/orderrecurring/297709/'
                        ],
                        'payment_method': 'cc',
                        'resource_uri': '/rest/v1/order/21287927/',
                        'shipping_address': None,
                        'status': 'reversed',
                        'total': '1.00',
                        'total_converted': '1.00',
                        'transactions': [
                            '/rest/v1/transaction/27394242/',
                            '/rest/v1/transaction/27394244/',
                            '/rest/v1/transaction/27394256/'
                        ],
                        'updated_at': '2020-01-17T21:19:25',
                        'user': '/rest/v1/user/123123/',
                        'user_detail': '/rest/v1/orderuserdetail/21288358/'
                    }
                ],
                "phones": [
                    "/rest/v1/phone/8675309/"
                ],
                "postal": "44123",
                "region": "OH",
                "sms_subscribed": "False",
                "state": "OH",
                "subscription_status": "monthly",
                "updated_at": "2016-07-11T18:19:26",
                "zip": "44123",
            }
        },
    },
}
