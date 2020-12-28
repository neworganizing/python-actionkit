from datetime import datetime, timedelta

today = datetime.now()

act_blue_order_id = '2039345'
action_for_act_blue_order_id = '682001'
action_for_act_blue_order_uri = '/rest/v1/donationaction/' + action_for_act_blue_order_id + '/'
act_blue_order_uri = '/rest/v1/order/' + act_blue_order_id + '/'
action_for_failed_order_id = '9996'
action_for_failed_order_uri = '/rest/v1/donationaction/' + action_for_failed_order_id + '/'
action_for_monthly_recurring_order_id = '335959703'
action_for_monthly_recurring_order_uri = '/rest/v1/donationaction/' + action_for_monthly_recurring_order_id + '/'
action_for_product_order_id = '387957964'
action_for_product_order_uri = '/rest/v1/donationaction/' + action_for_product_order_id + '/'
action_for_recent_product_order_id = '38717964'
action_for_recent_product_order_uri = '/rest/v1/donationaction/' + action_for_product_order_id + '/'
action_for_regular_order_id = '999999226'
action_for_regular_order_uri = '/rest/v1/donationaction/' + action_for_regular_order_id + '/'
action_for_weekly_recurring_order_id = '303552744'
action_for_weekly_recurring_order_uri = '/rest/v1/donationaction/' + action_for_weekly_recurring_order_id + '/'
failed_order_id = '28360' #order that is one-time and does not have products
failed_order_uri = '/rest/v1/order/' + failed_order_id + '/'
first_transaction_id = '392051'
first_transaction_uri = '/rest/v1/transaction/' + first_transaction_id + '/'
card_num_last_four = '1234'
member_id = '123123'
member_uri = '/rest/v1/user/' + member_id + '/'
member_email = 'example@example.com'
member_detail_uri = '/rest/v1/orderuserdetail/' + member_id + '/'
order_date = datetime.strptime('2017-10-23T02:21:30', "%Y-%m-%dT%H:%M:%S")
order_recurring_monthly_id = '6901'
order_recurring_monthly_uri = '/rest/v1/orderrecurring/' + order_recurring_monthly_id + '/'
order_recurring_weekly_id = '6992401'
order_recurring_weekly_uri = '/rest/v1/orderrecurring/' + order_recurring_weekly_id + '/'
order_with_order_recurring_monthly_id = '21287927'
order_with_order_recurring_monthly_uri = '/rest/v1/order/' + order_with_order_recurring_monthly_id + '/'
order_with_order_recurring_weekly_id = '21287929'
order_with_order_recurring_weekly_uri = '/rest/v1/order/' + order_with_order_recurring_weekly_id + '/'
phone_id = '8675309'
phone_uri = '/rest/v1/phone/' + phone_id + '/' #update below, where search by url is facilitated
product_id = '33'
product_order_id = '10425969' #order that is one-time and has products. order is > 2 weeks ago
product_order_uri = '/rest/v1/order/' + product_order_id + '/'
product_order_detail_id = '13859761'
product_order_detail_uri = '/rest/v1/orderdetail/' + product_order_detail_id + '/'
product_uri = '/rest/v1/product/' + product_id + '/'
recent_product_order_id = '1042514356' #order that is one-time, has products, and is recent.
recent_product_order_uri = '/rest/v1/order/' + recent_product_order_id + '/'
recent_product_order_detail_id = '1385324'
recent_product_order_detail_uri = '/rest/v1/orderdetail/' + recent_product_order_detail_id + '/'
regular_order_id = '20878360' #order that is one-time and does not have products
regular_order_uri = '/rest/v1/order/' + regular_order_id + '/'
second_product_id = '333'
second_product_uri = '/rest/v1/product/' + second_product_id + '/'
second_product_order_detail_id = '138597631'
second_product_order_detail_uri = '/rest/v1/orderdetail/' + second_product_order_detail_id + '/'
second_transaction_id = '92011'
second_transaction_uri = '/rest/v1/transaction/' + second_transaction_id + '/'


#objects

action_for_act_blue_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': order_date,
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
    'updated_at': order_date,
    'user': member_uri
}

action_for_failed_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': order_date,
    'created_user': False,
    'fields': {
    },
    'id': action_for_failed_order_id,
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
    'status': 'failed',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Import',
    'updated_at': order_date,
    'user': member_uri
}

action_for_regular_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': order_date,
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
    'updated_at': order_date,
    'user': member_uri
}

action_for_monthly_recurring_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': order_date,
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
    'status': 'active',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Import',
    'updated_at': order_date,
    'user': member_uri,
}

action_for_product_order_object = {
    'akid': '.18323492053.pOX3Jq',
    'created_at': order_date,
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
    'updated_at': order_date,
    'user': member_uri
}

action_for_recent_product_order_object = {
    'akid': '.18323492053.pOX3Jq',
    'created_at': order_date,
    'created_user': False,
    'fields': {   'address_validated': 'false',
                  'address_validation_notes': 'none',
                  'employer': 'None',
                  'occupation': 'Not employed',
                  'shown_save_payment_box': '1'},
    'id': action_for_recent_product_order_id,
    'ip_address': '199.87.199.6',
    'is_forwarded': False,
    'link': None,
    'mailing': None,
    'opq_id': '',
    # 'order': product_order_object, circular definition problem
    'page': '/rest/v1/donationpage/44637/',
    'referring_mailing': None,
    'referring_user': None,
    'resource_uri': action_for_recent_product_order_uri,
    'source': 'website',
    'status': 'completed',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Donation',
    'updated_at': order_date,
    'user': member_uri
}

action_for_weekly_recurring_order_object = {
    'akid': '.401.-9Mop1',
    'created_at': order_date,
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
    'status': 'active',
    'subscribed_user': False,
    'taf_emails_sent': None,
    'type': 'Import',
    'updated_at': order_date,
    'user': member_uri,
}

act_blue_order_object = {
    'account': 'MoveOn.org Civic Action PayPal',
    'action': action_for_act_blue_order_uri,
    'card_num_last_four': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'id': act_blue_order_id,
    'import_id': 'AB39502', #act blue orders have 'AB' at the beginning of the import id
    'orderdetails': [],
    'orderrecurrings': [],
    'payment_method': 'paypal',
    'resource_uri': act_blue_order_uri,
    'shipping_address': None,
    'status': 'completed',
    'total': '1.00',
    'total_converted': '1.00',
    'transactions': [
        first_transaction_uri
    ],
    'updated_at': order_date,
    'user': member_uri,
    'user_detail': member_detail_uri,
}


regular_order_object = {
    'account': 'MoveOn.org Civic Action PayPal',
    'action': action_for_regular_order_uri,
    'card_num_last_four': card_num_last_four,
    'created_at': order_date,
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
        first_transaction_uri
    ],
    'updated_at': order_date,
    'user': member_uri,
    'user_detail': member_detail_uri,
}

failed_order_object = {
    'account': 'MoveOn.org Civic Action PayPal',
    'action': action_for_failed_order_uri,
    'card_num_last_four': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'id': failed_order_id,
    'import_id': None,
    'orderdetails': [],
    'orderrecurrings': [],
    'payment_method': 'paypal',
    'resource_uri': failed_order_uri,
    'shipping_address': None,
    'status': 'failed',
    'total': '1.00',
    'total_converted': '1.00',
    'transactions': [
        first_transaction_uri
    ],
    'updated_at': order_date,
    'user': member_uri,
    'user_detail': member_detail_uri,
}

order_with_order_recurring_monthly_object = {
    'account': 'MoveOn.org Civic Action',
    'action': action_for_monthly_recurring_order_uri,
    'amount': '5.00',
    'amount_converted': '5.00',
    'card_num_last_four': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'id': order_with_order_recurring_monthly_id,
    'import_id': None,
    'orderdetails': [],
    'orderrecurrings': [
        order_recurring_monthly_uri
    ],
    'payment_method': 'cc',
    'resource_uri': order_with_order_recurring_monthly_uri,
    'shipping_address': None,
    'start': '2020-01-18',
    'status': 'active',
    'transactions': [
        first_transaction_uri,
        second_transaction_uri
    ],
    'updated_at': order_date,
    'user': member_uri,
    'user_detail': member_detail_uri,
}

order_with_order_recurring_weekly_object = {
    'account': 'MoveOn.org Civic Action',
    'action': action_for_weekly_recurring_order_uri,
    'amount': '5.00',
    'amount_converted': '5.00',
    'card_num_last_four': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'id': order_with_order_recurring_monthly_id,
    'import_id': None,
    'orderdetails': [],
    'orderrecurrings': [
        order_recurring_weekly_uri
    ],
    'payment_method': 'cc',
    'resource_uri': action_for_weekly_recurring_order_uri,
    'shipping_address': None,
    'start': '2020-01-15',
    'status': 'active',
    'transactions': [
        first_transaction_uri,
        second_transaction_uri,
    ],
    'updated_at': order_date,
    'user': member_uri,
    'user_detail': member_detail_uri,
}

order_recurring_monthly_object = {
    'account': 'MoveOn.org Political Action',
    'action': action_for_monthly_recurring_order_uri,
    'amount': '5.00',
    'amount_converted': '5.00',
    'cancel': order_recurring_monthly_uri + 'cancel/',
    'card_num': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'exp_date': '0223',
    'id': order_recurring_monthly_id,
    'order': order_with_order_recurring_monthly_uri,
    'period': 'months',
    'recurring_id': '349295', #not sure what this number isf or
    'resource_uri': order_recurring_monthly_uri,
    'start': '2013-11-03',
    'status': 'active',
    'updated_at': order_date,
    'user': member_uri
    }

order_recurring_weekly_object = {
    'account': 'MoveOn.org Political Action',
    'action': action_for_weekly_recurring_order_uri,
    'amount': '5.00',
    'amount_converted': '5.00',
    'cancel': order_recurring_weekly_uri + 'cancel/',
    'card_num': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'exp_date': '0223',
    'id': order_recurring_weekly_id,
    'order': order_with_order_recurring_weekly_uri,
    'period': 'months',
    'recurring_id': '349295', #not sure what this number isf or
    'resource_uri': order_recurring_weekly_uri,
    'start': '2013-11-03',
    'status': 'active',
    'updated_at': order_date,
    'user': member_uri
    }

product_order_object = {
    'account': 'MoveOn.org Political Action',
    'action': action_for_product_order_uri,
    'card_num_last_four': card_num_last_four,
    'created_at': order_date,
    'currency': 'USD',
    'id': product_order_id,
    'import_id': None,
    'orderdetails': [product_order_detail_uri, second_product_order_detail_uri],
    'orderrecurrings': [],
    'payment_method': 'cc',
    'resource_uri': product_order_uri,
    # 'shipping_address': /rest/v1/ordershippingaddress/79142/, #tk make shipping address object
    'status': 'completed',
    'total': '20.20',
    'total_converted': '20.20',
    # 'transactions': [/rest/v1/transaction/30617340/], #tk make transaction object
    'updated_at': order_date,
    'user': member_uri,
    # 'user_detail': /rest/v1/orderuserdetail/22712348/ #tk user detail object
}

product_order_detail_object = {
   'amount': '20.20',
    'amount_converted': '20.20',
    'candidate': None,
    'created_at': order_date,
    'currency': 'USD',
    'id': product_order_detail_id,
    'order': product_order_uri,
    'product': product_uri,
    'quantity': 1,
    'resource_uri': product_order_detail_uri,
    'status': 'completed',
    'updated_at': order_date
}

recent_product_order_detail_object = {
   'amount': '20.20',
    'amount_converted': '20.20',
    'candidate': None,
    'created_at': today - timedelta(days=7),
    'currency': 'USD',
    'id': recent_product_order_detail_id,
    'order': recent_product_order_uri,
    'product': product_uri,
    'quantity': 1,
    'resource_uri': product_order_detail_uri,
    'status': 'completed',
    'updated_at': today - timedelta(days=7),
}

recent_product_order_object = {
    'account': 'MoveOn.org Political Action',
    'action': action_for_recent_product_order_uri,
    'card_num_last_four': card_num_last_four,
    'created_at': today - timedelta(days=7),
    'currency': 'USD',
    'id': recent_product_order_id,
    'import_id': None,
    'orderdetails': [recent_product_order_detail_uri],
    'orderrecurrings': [],
    'payment_method': 'cc',
    'resource_uri': recent_product_order_uri,
    # 'shipping_address': /rest/v1/ordershippingaddress/79142/, #tk make shipping address object
    'status': 'completed',
    'total': '20.20',
    'total_converted': '20.20',
    # 'transactions': [/rest/v1/transaction/30617340/], #tk make transaction object
    'updated_at': today - timedelta(days=7),
    'user': member_uri,
    # 'user_detail': /rest/v1/orderuserdetail/22712348/ #tk user detail object
}

recent_product_order_detail_object = {
   'amount': '20.20',
    'amount_converted': '20.20',
    'candidate': None,
    'created_at': order_date,
    'currency': 'USD',
    'id': recent_product_order_detail_id,
    'order': recent_product_order_uri,
    'product': product_uri,
    'quantity': 1,
    'resource_uri': recent_product_order_detail_uri,
    'status': 'completed',
    'updated_at': order_date
}

product_object = {
    'admin_name': 'thismasksaveslives_mask',
    'created_at': order_date,
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
    'updated_at': order_date
}

second_product_order_detail_object = {
   'amount': '2.50',
    'amount_converted': '2.50',
    'candidate': None,
    'created_at': order_date,
    'currency': 'USD',
    'id': second_product_order_detail_id,
    'order': product_order_uri,
    'product': second_product_uri,
    'quantity': 2,
    'resource_uri': second_product_order_detail_uri,
    'status': 'completed',
    'updated_at': order_date
}

second_product_object = {
    'admin_name': 'savethepostoffice_sticker',
    'created_at': order_date,
    'currency': 'USD',
    'description': '',
    'hidden': False,
    'id': second_product_id,
    'maximum_order': 100,
    'name': 'Save the Post Office sticker',
    'orderdetails': [ second_product_order_detail_uri ],
    'price': '2.50',
    'resource_uri': second_product_uri,
    'shippable': True,
    'status': 'active',
    'tags': [],
    'updated_at': order_date
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
        recent_product_order_object,
        failed_order_object,
        act_blue_order_object,
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

first_transaction_object = {
    'account': 'Default Import Stub',
    'amount': '5.00',
    'amount_converted': '5.00',
    'created_at': order_date,
    'currency': 'USD',
    'failure_code': None,
    'failure_description': '',
    'failure_message': '',
    'id': first_transaction_id,
    'order': regular_order_uri,
    'resource_uri': first_transaction_uri,
    'status': 'completed',
    'success': False,
    'test_mode': False,
    'trans_id': None,
    'type': 'sale',
    'updated_at': order_date
}

second_transaction_object = {
    'account': 'Default Import Stub',
    'amount': '5.00',
    'amount_converted': '5.00',
    'created_at': order_date + timedelta(days=30),
    'currency': 'USD',
    'failure_code': None,
    'failure_description': '',
    'failure_message': '',
    'id': second_transaction_id,
    'order': regular_order_uri,
    'resource_uri': second_transaction_uri,
    'status': 'completed',
    'success': False,
    'test_mode': False,
    'trans_id': None,
    'type': 'sale',
    'updated_at': order_date + timedelta(days=30),
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
            "card_num": card_num_last_four,
            "created_at":"2020-04-23T20:42:55",
            "currency":"USD",
            "exp_date":"0822",
            "id": order_recurring_monthly_id,
            "order": order_with_order_recurring_monthly_object,
            "period":"months",
            "recurring_id":"z9zzzz",
            "resource_uri": order_recurring_monthly_uri,
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
        },
        order_recurring_weekly_id: order_recurring_weekly_object,
        order_recurring_monthly_id: order_recurring_monthly_object,
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
            act_blue_order_id: act_blue_order_object,
            failed_order_id: failed_order_object,
            order_with_order_recurring_weekly_id: order_with_order_recurring_weekly_object,
            order_with_order_recurring_monthly_id: order_with_order_recurring_monthly_object,
            product_order_id: product_order_object,
            regular_order_id: regular_order_object,
            recent_product_order_id: recent_product_order_object,
        },
    'orderdetails': {
        product_order_detail_uri: product_order_detail_object,
        second_product_order_detail_uri: second_product_order_detail_object,
        recent_product_order_detail_uri: recent_product_order_detail_object,
    },
    'products': {
        product_id: product_object,
        second_product_id: second_product_object
    },
    'transactions': {
        first_transaction_id: first_transaction_object,
        first_transaction_uri: first_transaction_object,
        second_transaction_id: second_transaction_object,
        second_transaction_uri: second_transaction_object,
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
