from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


from Global_Constants import GlobalConstants
from . import pre_test_questions

author = 'Kyubum Moon <mailto:moonx190@umn.edu>'

doc = """
행동강화물품 행동실험 사전조사
"""


class Constants(BaseConstants):
    name_in_url = 'pre_test_d'
    players_per_group = None
    num_rounds = 1
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    BINARY_POSSESSION = GlobalConstants.BINARY_POSSESSION
    smoker_type = pre_test_questions.SMOKER_TYPE
    satisfaction = pre_test_questions.SATISFACTION
    smoking_cessation_adverse_effect = pre_test_questions.SMOKING_CESSATION_ADVERSE_EFFECT
    smoking_experience = pre_test_questions.SMOKING_DESIRE_EXPERIENCE
    smoking_opinion = pre_test_questions.SMOKING_OPINION
    confidence_against_smoking = pre_test_questions.CONFIDENCE_AGAINST_SMOKING
    experience_frequency = pre_test_questions.EXPERIENCE_FREQUENCY
    L5_CHOICES = GlobalConstants.L5_CHOICES
    L53_CHOICES = GlobalConstants.L53_CHOICES
    L54_CHOICES = GlobalConstants.L54_CHOICES
    L55_CHOICES = GlobalConstants.L55_CHOICES
    L56_CHOICES = GlobalConstants.L56_CHOICES
    REGISTRATION_TYPE = [
        [1, "위기청소년"],
        [2, "여성"],
        [3, "대학생"],
        [4, "장애인"],
        [5, "소규모사업장"],
        [6, "기타"],
    ]

    MAX_YEAR = 2020
    MIN_YEAR = 1959
    MAX_MONTH = 12
    MIN_MONTH = 1
    MAX_DATE = 31
    MIN_DATE = 1

    NICOTINE_PATCH_ADVERSE_EFFECT = [
        [1, "없음"],
        [2, "최근 2주내 불안정 협심증 혹은 심근경색"],
        [3, "중증 부정맥"],
        [4, "뇌졸중"],
        [5, "장기적인 피부염(건선 등)"],
        [6, "피부 알레르기"],
        [7, "임신중 또는 수유중"],
        [8, "기타(직접입력)"],
    ]

    MEDICAL_GUARANTEE = [
        [1, "국민건강보험"],
        [2, "의료급여(기초수급자 및 차상위)"],
        [3, "모름"],
        [4, "미가입"],
        [5, "무응답/응답거부"],
    ]

    HIGHEST_SCHOOLING = [
        [1, "무학"],
        [2, "초등학교 졸업이하"],
        [3, "중학교 졸업이하"],
        [4, "고등학교 졸업이하"],
        [5, "전문대/대학교 졸업이하"],
        [6, "전문대/대학교 졸업이하"],
        [7, "모름"],
        [8, "무응답/응답거부"],
    ]

    OCCUPATION = [
        [1, "관리자"],
        [2, "전문가 및 관련종사자"],
        [3, "사무 종사자"],
        [4, "서비스 종사자"],
        [5, "판매 종사자"],
        [6, "농림어업 숙련 종사자"],
        [7, "기능 및 관련기능 종사자"],
        [8, "장치, 기계조작 및 조립 종사자"],
        [9, "단순 노무 종사자"],
        [10, "군인"],
        [11, "청소년(만 24세 이하)"],
        [12, "대학생"],
        [13, "무직"],
        [14, "모름"],
        [15, "무응답/응답거부"],
        [16, "기타(직접입력)"],
    ]

    SMOKING_CESSATION_THIS_TIME_REASON = [
        [1, "가족 혹은 주변사람들의 권유"],
        [2, "개인의 건강을 위해(현재 질병악화 및 장래 질병발생예방)"],
        [3, "담뱃값 인상 등 경제적 이유"],
        [4, "금연구역 확대 등 환경적 이유"],
        [5, "깨끗한 이미지 관리를 위해서(예: 입 냄새가 고약, 옷에 담배 냄새가 뱀)"],
        [6, "나의 흡연으로 주위사람 건강에 나쁜 영향을 미치는 것을 방지하기 위해서"],
        [7, "금연의지를 보여주기 위해"],
        [8, "흡연자에 대한 사회적 시선 때문"],
        [9, "기타(직접입력)"],
    ]

    TIME_DIVISION = [
        [3, "5분 이내"],
        [2, "6분~30분 사이"],
        [1, "31분~1시간 사이"],
        [0, "1시간 이후"],
    ]

    TYPE_LICKERT = [
        [1, "전혀 그렇지 않다"],
        [2, "그렇지 않은편이다"],
        [3, "간혹 그렇다"],
        [4, "자주 그렇다"],
        [5, "항상 그렇다"],
    ]

    SATISFACTION_LICKERT =[
        [1, "매우 그렇다"],
        [2, "그렇다"],
        [3, "보통이다"],
        [4, "그렇지 않다"],
        [5, "전혀 그렇지 않다"],
    ]

    SMOKING_CESSATION_PRE_TEST_LICKERT = [
        [1, "전혀 그렇지않다"],
        [2, "그렇지 않다"],
        [3, "보통"],
        [4, "그렇다"],
        [5, "매우 그렇다"],
    ]

    DESIRE_METRIC = [
        [1, "전혀 욕구가 없다"],
        [2, "아무욕구도 없다"],
        [3, "보통"],
        [4, "항상"],
        [5, "매우강하다"],
    ]

    CONFIDENCE_METRIC = [
        [1, "전혀 자신없다"],
        [2, "자신없다"],
        [3, "보통"],
        [4, "자신있다"],
        [5, "매우 자신있다"],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_smoker_type(index):
    return models.IntegerField(
        label=Constants.smoker_type[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )
def make_field_satisfaction(index):
    return models.IntegerField(
        label=Constants.satisfaction[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L53_CHOICES,
    )

def make_field_smoking_cessation_adverse(index):
    return models.IntegerField(
        label=Constants.smoking_cessation_adverse_effect[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L54_CHOICES,
    )
def make_field_smoking_experience(index):
    return models.IntegerField(
        label=Constants.smoking_experience[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L55_CHOICES,
    )
def make_field_smoking_opinion(index):
    return models.IntegerField(
        label=Constants.smoking_opinion[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L54_CHOICES,
    )
def make_field_confidence(index):
    return models.IntegerField(
        label=Constants.confidence_against_smoking[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L56_CHOICES,
    )
def make_field_experience_frequency(index):
    return models.IntegerField(
        label=Constants.experience_frequency[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L54_CHOICES,
    )


class Player(BasePlayer):
    self_reported_health_status = models.IntegerField(
        label="귀하가 생각하는 본인의 현재 건강상태는 어떻습니까?",
        choices=[
            [1, "① 매우 건강함"],
            [2, "② 건강한 편"],
            [3, "③ 보통"],
            [4, "④ 허약한 편"],
            [5, "⑤ 매우 허약함"],
        ],
        widget=widgets.RadioSelect,
    )

    stress_metric_self_reported = models.IntegerField(
        label="평소 귀하의 스트레스 정도는 어떻습니까?",
        choices=[
            [1, "① 전혀 받지 않음"],
            [2, "② 별로 받지 않음"],
            [3, "③ 그저 그런 편임 "],
            [4, "④ 약간 받는 편"],
            [5, "⑤ 매우 많이 받음"],
        ],
        widget=widgets.RadioSelect,
    )

    afterward_smoking_cessation_yesno = models.IntegerField(
        label="향후에 금연을 실천할 생각이 있습니까?",
        choices=[
            [1, "금연에 대해 생각해 본 적 없음"],
            [2, "향후 6개월 이내에 금연할 계획이 있음"],
            [3, "1개월 이내에 금연할 계획이 있음"],
            [4, "금연을 실천한 지 1일 이상이 지났음"],
            [5, "금연을 실천한 지 6개월 이상 되었음 "],
        ],
        widget=widgets.RadioSelect,
    )

    sa_1 = make_field_smoking_cessation_adverse(0)
    sa_2 = make_field_smoking_cessation_adverse(1)
    sa_3 = make_field_smoking_cessation_adverse(2)
    sa_4 = make_field_smoking_cessation_adverse(3)
    sa_5 = make_field_smoking_cessation_adverse(4)
    sa_6 = make_field_smoking_cessation_adverse(5)
    sa_7 = make_field_smoking_cessation_adverse(6)
    sa_8 = make_field_smoking_cessation_adverse(7)
    sa_9 = make_field_smoking_cessation_adverse(8)

    se_1 = make_field_smoking_experience(0)
    se_2 = make_field_smoking_experience(1)

    so_1 = make_field_smoking_opinion(0)
    so_2 = make_field_smoking_opinion(1)
    so_3 = make_field_smoking_opinion(2)
    so_4 = make_field_smoking_opinion(3)
    so_5 = make_field_smoking_opinion(4)
    so_6 = make_field_smoking_opinion(5)

    cas_1 = make_field_confidence(0)
    cas_2 = make_field_confidence(1)
    cas_3 = make_field_confidence(2)
    cas_4 = make_field_confidence(3)
    cas_5 = make_field_confidence(4)
    cas_6 = make_field_confidence(5)
    cas_7 = make_field_confidence(6)

    ef_1 = make_field_experience_frequency(0)
    ef_2 = make_field_experience_frequency(1)
    ef_3 = make_field_experience_frequency(2)
    ef_4 = make_field_experience_frequency(3)
    ef_5 = make_field_experience_frequency(4)
    ef_6 = make_field_experience_frequency(5)
    ef_7 = make_field_experience_frequency(6)
    ef_8 = make_field_experience_frequency(7)
    ef_9 = make_field_experience_frequency(8)
    ef_10 = make_field_experience_frequency(9)

    behavior_strengthening_material_barcode = models.IntegerField(
        label="지급받은 행동물품 일련번호를 입력해주십시오.",
        blank=True,
    )

    gender = models.IntegerField(
        label="귀하의 성별은 어떻게 되십니까?",
        choices=[
            [1, "남성"],
            [2, "여성"],
        ],
        widget=widgets.RadioSelect,
    )

    birth_year = models.IntegerField(
        label="귀하의 출생년도는 몇년도이십니까?",
        choices=range(1940, 2002),
        blank=True,
    )

    region = models.IntegerField(
        label="귀하의 거주 지역을 선택해주세요.",
        choices=[
            [1, "서울"],
            [2, "인천"],
            [3, "경기도"],
            [4, "강원도"],
            [5, "세종"],
            [6, "충청남도"],
            [7, "충청북도"],
            [8, "대전"],
            [9, "대구"],
            [10, "경상북도"],
            [11, "경상남도"],
            [12, "울산"],
            [13, "부산"],
            [14, "전라북도"],
            [15, "전라남도"],
            [16, "광주"],
            [17, "제주도"],
        ],
        widget=widgets.RadioSelect,
    )

    region_size = models.IntegerField(
        label="귀하의 거주지의 지역규모를 선택해주세요.",
        choices=[
            [1, "대도시(특별/광역시-서울, 부산, 대구, 인천, 광주, 대전, 울산)"],
            [2, "중소도시(특별/광역시가 아닌 그 외 지역)"],
            [3, "읍면지역(ex. ○○시 ○○읍/면)"],
            [4, "특수지역(도서·벽지 지역)"],
        ],
        widget=widgets.RadioSelect,
    )

    marriage = models.IntegerField(
        label="귀하의 혼인상태를 선택해주십시오:",
        choices=[
            [1, "결혼안함"],
            [2, "결혼함"],
            [3, "이혼/사별함"],
            [4, "기타"],
        ],
        widget=widgets.RadioSelect,
    )

    job_position = models.IntegerField(
        label="직장(일)에서 귀하의 지위는 무엇입니까?",
        choices=[
            [1, "전일제 근무자"],
            [2, "파트타임 근무자"],
            [3, "프리랜서"],
            [4, "최근 6개월 이내 근무경력 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    firm_type = models.IntegerField(
        label="귀하께서 현재 근무하시는 기업의 유형은 다음 중 무엇입니까?",
        choices=[
            [1, "공기업·준정부기관·기타 공공기관"],
            [2, "공무원"],
            [3, "사기업-규모별: 대기업"],
            [4, "사기업-규모별: 중견기업"],
            [5, "사기업-규모별: 중소·벤처기업"],
            [6, "사기업-규모별: 소기업 및 소상공인"],
            [7, "현재 근무중이 아님"],
            [8, "기타(위에 해당하지 않는 경우 자유 입력: )"],

        ],
        widget=widgets.RadioSelect,
    )

    firm_type_op = models.StringField(
        label="기타(위에 해당하지 않는 경우 자유 입력: )",
        blank=True,
    )

    firm_size = models.IntegerField(
        label="현재 근무하시는 사업장 규모를 다음 중 선택해주십시오",
        choices=[
            [1, "5인 미만"],
            [2, "5인 이상~50인 미만"],
            [3, "50인 이상~100인 미만"],
            [4, "100인 이상~200인 미만"],
            [5, "200인 이상~300인 미만"],
            [6, "300인 이상"],
            [7, "현재 근무중이 아님"],
        ],
        widget=widgets.RadioSelect,
    )

    household_income = models.IntegerField(
        label="최근 6개월 평균 가구소득액(즉, 가족구성원 전체의 수입 합산액)은 어떻게 되십니까? 월별 세후 실질 수령액 기준으로 선택해 주십시오.",
        choices=[
            [1, "없음"],
            [2, "150만원 미만"],
            [3, "150만원 이상 300만원 미만"],
            [4, "300만원 이상 450만원 미만"],
            [5, "450만원 이상 600만원 미만"],
            [6, "600만원 이상 750만원 미만"],
            [7, "750만원 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    text_field = models.LongStringField(
        label="메모남겨주실 부분 있으시면 여기에 남겨주시면 감사드리겠습니다.",
        blank=True,
    )
