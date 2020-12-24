action_for_regular_order_id = '999999226'
action_for_regular_order_uri = '/rest/v1/donationaction/' + action_for_regular_order_id + '/'

action_for_product_order_id = '387957964'
action_for_product_order_uri = '/rest/v1/donationaction/' + action_for_product_order_id + '/'
action_for_monthly_recurring_order_id = '335959703'
action_for_monthly_recurring_order_uri = '/rest/v1/donationaction/' + action_for_monthly_recurring_order_id + '/'
action_for_weekly_recurring_order_id = '303552744'
action_for_weekly_recurring_order_uri = '/rest/v1/donationaction/' + action_for_weekly_recurring_order_id + '/'

member_id = '123123'
member_uri = '/rest/v1/user/' + member_id + '/'
member_email = 'example@example.com'
member_detail_uri = '/rest/v1/orderuserdetail/' + member_id + '/'

recurring_monthly_order_id = '999114'

regular_order_id = '20878360' #order that is one-time and does not have products
regular_order_uri = '/rest/v1/order/' + regular_order_id + '/'

order_with_order_recurring_monthly_id = '21287927'
order_with_order_recurring_monthly_uri = '/rest/v1/order/' + order_with_order_recurring_monthly_id + '/'

order_with_order_recurring_weekly_id = '21287929'
order_with_order_recurring_weekly_uri = '/rest/v1/order/' + order_with_order_recurring_weekly_id + '/'

orderrecurring_monthly_id = '999114'
orderrecurring_monthly_uri = '/rest/v1/orderrecurring/' + orderrecurring_monthly_id + '/'

product_id = '33'
product_uri = '/rest/v1/product/' + product_id + '/'
product_order_detail_id = '13859761'
product_order_detail_uri = '/rest/v1/orderdetail/' + product_order_detail_id + '/'
product_order_id = '10425969' #order that is one-time and does not has products
product_order_uri = '/rest/v1/order/' + product_order_id + '/'

phone_id = '8675309'
phone_uri = '/rest/v1/phone/' + phone_id + '/' #update below, where search by url is facilitated
#objects

action_for_regular_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': '1999-10-13T17:07:00',
    'created_user': False,
    'fields': {
    },
    'id': action_for_regular_order_id,
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
    'status': 'completed',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Import',
    'updated_at': '2015-09-23T02:21:30',
    'user': member_uri
}

action_for_monthly_recurring_order_object = {
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
    'status': 'completed',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Import',
    'updated_at': '2015-09-23T02:21:30',
    'user': member_uri,
}

action_for_product_order_object = {
    'akid': '.18323492053.pOX3Jq',
    'created_at': '2019-12-04T22:21:38',
    'created_user': False,
    'fields': {   'address_validated': 'false',
                  'address_validation_notes': 'none',
                  'employer': 'None',
                  'occupation': 'Not employed',
                  'shown_save_payment_box': '1'},
    'id': action_for_product_order_id,
    'ip_address': '199.87.199.6',
    'is_forwarded': False,
    'link': None,
    'mailing': None,
    'opq_id': '',
    # 'order': product_order_object, circular definition problem
    'page': '/rest/v1/donationpage/44637/',
    'referring_mailing': None,
    'referring_user': None,
    'resource_uri': action_for_product_order_uri,
    'source': 'website',
    'status': 'completed',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Donation',
    'updated_at': '2019-12-04T22:21:40',
    'user': member_uri
}

action_for_weekly_recurring_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': '1999-10-13T17:07:00',
    'created_user': False,
    'fields': {
        'weekly': '1',
        'weekly_amount': '4.00'
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
    'status': 'completed',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Import',
    'updated_at': '2015-09-23T02:21:30',
    'user': member_uri,
}

regular_order_object = {
    'account': 'MoveOn.org Civic Action PayPal',
    'action': action_for_regular_order_uri,
    'card_num_last_four': '',
    'created_at': '2020-08-15T17:44:00',
    'currency': 'USD',
    'id': regular_order_id,
    'import_id': None,
    'orderdetails': [],
    'orderrecurrings': [],
    'payment_method': 'paypal',
    'resource_uri': regular_order_uri,
    'shipping_address': None,
    'status': 'completed',
    'total': '1.00',
    'total_converted': '1.00',
    'transactions': [
        '/rest/v1/transaction/26134025a/'
    ],
    'updated_at': '2019-05-15T17:44:01',
    'user': member_uri,
    'user_detail': member_detail_uri,
}

order_with_order_recurring_monthly_object = {
    'account': 'MoveOn.org Civic Action',
    'action': action_for_monthly_recurring_order_uri,
    'amount': '5.00',
    'amount_converted': '5.00',
    'card_num': '5644',
    'created_at': '2019-01-18T22:29:15',
    'currency': 'USD',
    'id': order_with_order_recurring_monthly_id,
    'import_id': None,
    'orderdetails': [],
    'orderrecurrings': [
        orderrecurring_monthly_uri
    ],
    'payment_method': 'cc',
    'resource_uri': order_with_order_recurring_monthly_uri,
    'shipping_address': None,
    'start': '2020-01-18',
    'status': 'reversed',
    'transactions': [
        '/rest/v1/transaction/27394242/',
        '/rest/v1/transaction/27394244/',
        '/rest/v1/transaction/27394256/'
    ],
    'updated_at': '2020-01-17T21:19:25',
    'user': member_uri,
    'user_detail': member_detail_uri,
}

order_with_order_recurring_weekly_object = {
    'account': 'MoveOn.org Civic Action',
    'action': action_for_weekly_recurring_order_uri,
    'amount': '5.00',
    'amount_converted': '5.00',
    'card_num': '5644',
    'created_at': '2019-01-15T22:29:15',
    'currency': 'USD',
    'id': order_with_order_recurring_monthly_id,
    'import_id': None,
    'orderdetails': [],
    'orderrecurrings': [
        '/rest/v1/orderrecurring/297709/'
    ],
    'payment_method': 'cc',
    'resource_uri': action_for_weekly_recurring_order_uri,
    'shipping_address': None,
    'start': '2020-01-15',
    'status': 'reversed',
    'transactions': [
        '/rest/v1/transaction/27394242/',
        '/rest/v1/transaction/27394244/',
        '/rest/v1/transaction/27394256/'
    ],
    'updated_at': '2020-01-17T21:19:25',
    'user': member_uri,
    'user_detail': member_detail_uri,
}

product_order_detail_object = {
    'amount': '20.20',
    'amount_converted': '20.20',
    'candidate': None,
    'created_at': '2020-12-04T22:21:39',
    'currency': 'USD',
    'id': product_order_detail_id,
    'order': product_order_uri,
    'product': product_uri,
    'quantity': 1,
    'resource_uri': product_order_detail_uri,
    'status': 'completed',
    'updated_at': '2019-12-04T22:21:39'
}

product_order_object = {
    'account': 'MoveOn.org Political Action',
    'action': action_for_product_order_uri,
    'card_num_last_four': '2314',
    'created_at': '2019-12-04T22:21:39',
    'currency': 'USD',
    'id': product_order_id,
    'import_id': None,
    'orderdetails': [product_order_detail_uri], #tk make order details object
    'orderrecurrings': [],
    'payment_method': 'cc',
    'resource_uri': product_order_uri,
    # 'shipping_address': /rest/v1/ordershippingaddress/79142/, #tk make shipping address object
    'status': 'completed',
    'total': '20.20',
    'total_converted': '20.20',
    # 'transactions': [/rest/v1/transaction/30617340/], #tk make transaction object
    'updated_at': '2019-12-04T22:21:40',
    'user': member_uri,
    # 'user_detail': /rest/v1/orderuserdetail/22712348/ #tk user detail object
}

product_order_detail_object = {
   'amount': '20.20',
    'amount_converted': '20.20',
    'candidate': None,
    'created_at': '2020-12-04T22:21:39',
    'currency': 'USD',
    'id': product_order_detail_id,
    'order': product_order_uri,
    'product': product_uri,
    'quantity': 1,
    'resource_uri': product_order_detail_uri,
    'status': 'completed',
    'updated_at': '2020-12-04T22:21:39'
}

product_object = {
    'admin_name': 'thismasksaveslives_mask',
    'created_at': '2020-12-04T19:09:23',
    'currency': 'USD',
    'description': '<img \'src=\"https://s3.amazonaws.com/s3.moveon.org/images/editor-2020-12-04.jpg\" \'\r\n>/>\r\n<em>Please note: Delivery not guaranteed before 12/25. \'\'</em>',
    'hidden': False,
    'id': product_id,
    'maximum_order': 100,
    'name': '"This Mask Saves Lives" face mask',
    'orderdetails': [ product_order_detail_uri ],
    'price': '20.20',
    'resource_uri': product_uri,
    'shippable': True,
    'status': 'active',
    'tags': [],
    'updated_at': '2020-12-04T19:59:59'
}

member_object = {
    "address1": "123 Main St.",
    "address2": "",
    "city": "Cleveland",
    "country": "United States",
    "created_at": "2015-11-18T16:22:31",
    "do_not_call": "True",
    "email": member_email,
    "employer": "Ringling Bros",
    "fields": {},
    "first_name": "Joey",
    "last_name": "AndMe",
    "middle_name": "Annabelle",
    "id": member_id,
    "occupation": "balloon artist",
    'orders': [
        regular_order_object,
        order_with_order_recurring_weekly_object,
        order_with_order_recurring_monthly_object,
        product_order_object,
    ],
    "phones": [
        phone_uri,
    ],
    "postal": "44123",
    "region": "OH",
    "sms_subscribed": "False",
    "state": "OH",
    "subscription_status": "monthly",
    "updated_at": "2016-07-11T18:19:26",
    "zip": "44123",
}

member_object_detail_with_recurring_order = {
    "address1":"123 Main St",
    "address2":"",
    "city":"Any City",
    "country":"United States",
    "created_at":"2020-04-23T20:42:55",
    "email": member_email,
    "first_name":"Testy",
    "id": member_id,
    "last_name":"Test",
    "middle_name":"",
    "orders": [
        order_with_order_recurring_monthly_uri
    ],
    "plus4":"4052",
    "postal":"99999-4052",
    "prefix":"",
    "region":"AZ",
    "source":"",
    "state":"AZ",
    "suffix":"",
    "updated_at":"2020-04-23T20:42:55",
    "zip":"99999"
}

phone_object = {
    "created_at": "2015-11-24T21:07:58",
    "id": "8675309",
    "normalized_phone": "5558675309",
    "phone": "5558675309",
    "resource_uri": phone_uri,
    "source": "user",
    "type": "home",
    "updated_at": "2016-03-29T16:41:10",
    "user": member_uri
}

TEST_DATA = {
    'actions': {
        action_for_regular_order_uri: { #fake action_url
            'res': 200,
             #some fields removed for brevity.
             # add them back if you need them for testing
            'action': action_for_regular_order_object,
        },
        action_for_weekly_recurring_order_uri: { #fake action_url with weekly recurring
            'res': 200,
            'action': action_for_weekly_recurring_order_object,
        },
        action_for_monthly_recurring_order_uri: {
            'res': 200,
            'action': action_for_monthly_recurring_order_object,
        }
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
            "id": orderrecurring_monthly_id,
            "order": order_with_order_recurring_monthly_object,
            "period":"months",
            "recurring_id":"z9zzzz",
            "resource_uri": orderrecurring_monthly_uri,
            "start":"2020-05-23",
            "status":"canceled_by_admin",
            "updated_at":"2020-04-23T23:02:39",
            "user": member_uri,
            "user_detail": member_object_detail_with_recurring_order,
        },
        member_id: {
            "res": None,
            "orders_recurring": [
                order_with_order_recurring_monthly_object,
                order_with_order_recurring_weekly_object,
            ]
        },
        "update_orderrecurring_status": {
            'res': None,
            'success': True
        }
    },
    'phones': {

        phone_uri: { #phone url
            'res': None,
            'phone': phone_object,
        },
        phone_id: { #phone id
            'res': 200,
            'phone': phone_object,
        },
    },
    'orders':
        {
            regular_order_id: regular_order_object,
            order_with_order_recurring_weekly_id: order_with_order_recurring_weekly_object,
            order_with_order_recurring_monthly_id: order_with_order_recurring_monthly_object,
            product_order_id: product_order_object,
        },
    'order_details': {
        product_order_detail_uri: product_order_detail_object,
    },
    'products': {
        product_id: product_object,
    },
    'users': {
        'create_user': {
            'res': None,
            'id': member_id,
        },
        member_email: {
            'res': None,
            'id': member_id,
        },
        member_id: { #userid
            'res': 200,
             #some fields removed for brevity.
             # add them back if you need them for testing
            'user': member_object,
        },
    },
}
