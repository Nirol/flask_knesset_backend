
from text_helper import combine_yeshuv_jsons
from yeshuv_queries import query_yeshuv_sn_by_name


from . import api
from kalfi_display import get_yeshuv_knesset_elections_data_json, get_yeshuv_kalfi_json
from flask import  jsonify
from app import db
from models import  Yeshuv


@api.route('/yeshuvHebrewList', methods=['GET'])
def full_yeshuv_list():
    optional_yeshuv_list_of_lists = db.session.query(Yeshuv.yeshuv_name_hebrew).all()
    yeshuv_list = [item for sublist in optional_yeshuv_list_of_lists for item in sublist]
    return jsonify(yeshuv_list)

@api.route('/yeshuv/<string:yeshuv_name>',  methods=['GET'])
def get_yeshuv_data_api(yeshuv_name):
    yeshuv_sn = query_yeshuv_sn_by_name(yeshuv_name)
    elec_data_json = get_yeshuv_knesset_elections_data_json(yeshuv_sn)
    kalfi_data_json = get_yeshuv_kalfi_json(yeshuv_sn)
    full_json = combine_yeshuv_jsons(elec_data_json, kalfi_data_json)
    print(full_json)
    return jsonify(full_json)

@api.route('/yeshuv/sn/<int:yeshuv_sn>',  methods=['GET'])
def get_yeshuv_data_api_sn(yeshuv_sn):

    elec_data_json = get_yeshuv_knesset_elections_data_json(yeshuv_sn)
    kalfi_data_json = get_yeshuv_kalfi_json(yeshuv_sn)
    full_json = combine_yeshuv_jsons(elec_data_json, kalfi_data_json)
    print(full_json)
    return jsonify(full_json)

@api.route('/autocomplete/<string:prefix_yeshuv>', methods=['GET'])
def autocomplete(prefix_yeshuv):
    # optional_yeshuv_list = Yeshuv.query.filter(Yeshuv.yeshuv_name_hebrew.like('%' + str(search) + '%'))
    optional_yeshuv_list = db.session.query(Yeshuv.yeshuv_name_hebrew).filter(
        Yeshuv.yeshuv_name_hebrew.like('%' + str(prefix_yeshuv) + '%')).all()
    print(optional_yeshuv_list)
    return jsonify(optional_yeshuv_list)