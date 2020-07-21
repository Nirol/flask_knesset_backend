from typing import List

from sqlalchemy import desc
from app import db
from app.models import  Knesset_22, Yeshuv
#make sure the api call for yeshuv data by yeshuv_sv is legal.
from queries import knesset22, kalfi, yeshuv_knesset
from queries.yeshuv_knesset import query_yeshuvknesset_by_sn_count


def query_validate_yeshuv_exist_by_sn(yeshuv_sn: int) -> int:
    yeshuv = db.session.query(Yeshuv).filter_by(
        yeshuv_sn=yeshuv_sn).first()
    if not yeshuv:
        return -1

    count_knesset22_table = knesset22.query_knesset_22_kalfi_count(yeshuv_sn)
    if count_knesset22_table < 1:
        return -1
    count_kalfi_table =kalfi.quary_kalfi_count_by_yeshuv_sn(yeshuv_sn)
    if count_kalfi_table < 1:
        return -1

    count_yeshuv_knesset =  query_yeshuvknesset_by_sn_count(yeshuv_sn)
    if count_yeshuv_knesset <1:
        return -1

    return 1

