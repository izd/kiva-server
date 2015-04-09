raw = {u'account_is_developer': True, u'stats_currency_loss_rate': 0, u'stats_num_raised': 0, u'lender_country_code': u'US', u'stats_number_of_invites': 0, u'stats_number_of_loans_by_invitees': 0, u'stats_total_inactive': 0, u'lender_loan_count': 1, u'lender_name': u'Zack', u'stats_num_expired': 0, u'stats_amount_outstanding_promo': 0, u'account_lender_id': u'zack4340', u'lender_uid': u'zack4340', u'stats_arrears_rate': 0, u'account_is_public': True, u'stats_amount_repaid': 0, u'stats_total_defaulted': 0, u'account_last_name': u'Hsi', u'stats_total_ended': 0, u'stats_num_defaulted': 0, u'lender_invitee_count': 0, u'stats_amount_in_arrears': 0, u'stats_total_inactive_expired': 0, u'account_first_name': u'Zack', u'stats_num_paying_back': 1, u'stats_num_ended': 0, u'account_id': 2089742, u'stats_number_of_gift_certificates': 0, u'lender_occupational_info': u"Hi I'm Zack!", u'stats_num_inactive': 0, u'stats_amount_refunded': 0, u'stats_num_inactive_expired': 0, u'stats_total_expired': 0, u'stats_num_refunded': 0, u'stats_number_delinquent': 0, u'expected_repayments': [{u'repayment_date': u'2015-05-01 00:00:00', u'user_repayments': u'3.00', u'id': u'1430463600000', u'promo_repayments': u'0.00', u'loans_making_repayments': u'1'}, {u'repayment_date': u'2015-10-01 00:00:00', u'user_repayments': u'4.00', u'id': u'1443682800000', u'promo_repayments': u'0.00', u'loans_making_repayments': u'1'}, {u'repayment_date': u'2015-09-01 00:00:00', u'user_repayments': u'5.00', u'id': u'1441090800000', u'promo_repayments': u'0.00', u'loans_making_repayments': u'1'}, {u'repayment_date': u'2015-08-01 00:00:00', u'user_repayments': u'4.00', u'id': u'1438412400000', u'promo_repayments': u'0.00', u'loans_making_repayments': u'1'}, {u'repayment_date': u'2015-06-01 00:00:00', u'user_repayments': u'5.00', u'id': u'1433142000000', u'promo_repayments': u'0.00', u'loans_making_repayments': u'1'}, {u'repayment_date': u'2015-07-01 00:00:00', u'user_repayments': u'4.00', u'id': u'1435734000000', u'promo_repayments': u'0.00', u'loans_making_repayments': u'1'}], u'stats_amount_donated': 0, u'stats_amount_of_loans': 25, u'stats_currency_loss': 0, u'lender_personal_url': u'zackhsi.com', u'stats_total_fund_raising': 0, u'lender_member_since': u'2015-03-22T01:57:39Z', u'stats_total_paying_back': 25, u'stats_amount_of_loans_by_invitees': 0, u'stats_number_of_loans': 1, u'lender_lender_id': u'zack4340', u'lender_occupation': u'Engineer', u'stats_default_rate': 0, u'stats_amount_outstanding': 25, u'lender_whereabouts': u'San Francisco California', u'stats_num_fund_raising': 0, u'stats_total_refunded': 0, u'lender_image_id': 1841451, u'lender_loan_because': u'warm fuzzy feelings'}

formatted_list = []
for k, v in raw.iteritems():
    if k == 'expected_repayments':
        continue  # skip that beast

    java_class = 'int'
    if 'lender' in k or k in ['account_first_name', 'account_last_name', 'lender_whereabouts', 'lender_country_code', 'lender_lender_id', 'lender_loan_because']:
        java_class = 'String'

    if k == 'lender_member_since':
        java_class = 'Date'

    if k in ['account_is_developer', 'account_is_public']:
        java_class = 'boolean'

    if k in ['lender_image_id', 'lender_loan_count', 'lender_invitee_count']:
        java_class = 'int'

    # formatted = "public {} {}; {}".format(java_class, k, v)
    formatted = "public {} {};".format(java_class, k)
    formatted_list.append(formatted)

formatted_list.sort()

for each in formatted_list:
    print each
