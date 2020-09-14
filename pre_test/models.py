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
from . import satisfaction

author = 'Kyubum Moon <mailto:moonx190@umn.edu>'

doc = """
행동강화물품 행동실험 사전조사
"""


class Constants(BaseConstants):
    name_in_url = 'pre_test'
    players_per_group = None
    num_rounds = 1

    sm1_list = satisfaction.sm1_list
    BINARY_CHOICE = GlobalConstants.BINARY_CHOICES
    BINARY_POSSESSION = GlobalConstants.BINARY_POSSESSION

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
        [1, "(3) 5분 이내"],
        [2, "(2) 6분~30분 사이"],
        [3, "(1) 31분~1시간 사이"],
        [4, "(0) 1시간 이후"],
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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_sm(index):
    return models.IntegerField(
        label=Constants.sm1_list[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.SATISFACTION_LICKERT,
    )

class Player(BasePlayer):
    registration_type = models.IntegerField(
        label="귀하의 등록유형을 선택해주십시오.",
        choices=Constants.REGISTRATION_TYPE,
        widget=widgets.RadioSelect,
    )

    smoking_cessation_start_year = models.IntegerField(
        label="귀하의 금연시작년도를 입력해주십시오.",
        choices=range(Constants.MIN_YEAR, Constants.MAX_YEAR + 1),

    )

    smoking_cessation_start_month = models.IntegerField(
        label="귀하의 금연시작월을 입력해주십시오.",
        choices=range(Constants.MIN_MONTH,Constants.MAX_MONTH+1),

    )
    smoking_cessation_start_date = models.IntegerField(
        label="귀하의 금연시작일을 입력해주십시오.",
        choices=range(Constants.MIN_DATE, Constants.MAX_DATE + 1),

    )

    support_service_registration_year = models.IntegerField(
        label="귀하의 금연지원프로그램 등록년도를 입력해주십시오.",
        choices=range(Constants.MIN_YEAR, Constants.MAX_YEAR + 1),

    )

    support_service_registration_month = models.IntegerField(
        label="귀하의 금연지원프로그램 등록월을 입력해주십시오.",
        choices=range(Constants.MIN_MONTH, Constants.MAX_MONTH + 1),

    )
    support_service_registration_date = models.IntegerField(
        label="귀하의 금연지원프로그램 등록일을 입력해주십시오.",
        choices=range(Constants.MIN_DATE, Constants.MAX_DATE + 1),

    )

    smoking_cessation_resolution_year = models.IntegerField(
        label="귀하의 금연결심년도를 입력해주십시오.",
        choices=range(Constants.MIN_YEAR, Constants.MAX_YEAR + 1),

    )

    smoking_cessation_resolution_month = models.IntegerField(
        label="귀하의 금연결심월을 입력해주십시오.",
        choices=range(Constants.MIN_MONTH, Constants.MAX_MONTH + 1),

    )
    smoking_cessation_resolution_date = models.IntegerField(
        label="귀하의 금연결심일을 입력해주십시오.",
        choices=range(Constants.MIN_DATE, Constants.MAX_DATE + 1),

    )

    smoking_cessation_supporter_1 = models.BooleanField(
        label="부모/조부모",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_2 = models.BooleanField(
        label="형제자매",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_3 = models.BooleanField(
        label="배우자/애인",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_4 = models.BooleanField(
        label="자녀",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_5 = models.BooleanField(
        label="친구/선후배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_6 = models.BooleanField(
        label="직장동료",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_7 = models.BooleanField(
        label="교사",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_8 = models.BooleanField(
        label="의료인",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_9 = models.BooleanField(
        label="없음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_supporter_10 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    support_service_registration_source_1 = models.BooleanField(
        label="TV 및 라디오 광고를 통해",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_2 = models.BooleanField(
        label="플랜카드, 포스터, 홍보책자 등을 통해",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_3 = models.BooleanField(
        label="인터넷을 통해",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_4 = models.BooleanField(
        label="보건소 안내문을 통해",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_5 = models.BooleanField(
        label="주변의 권유",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_6 = models.BooleanField(
        label="금연상담전화를 통해",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_7 = models.BooleanField(
        label="행사/이벤트를 통해",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_8 = models.BooleanField(
        label="의료진의 권고",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    support_service_registration_source_9 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    height = models.FloatField(
        label="귀하의 신장을 cm단위로 입력해주십시오.",
        blank=True,
    )

    weight = models.FloatField(
        label="귀하의 체중을 kg단위로 입력해주십시오.",
        blank=True,
    )

    waist_circumference = models.FloatField(
        label="귀하의 복부둘레를 inch 입력해주십시오.",
        blank=True,
    )

    carbon_monoxide = models.FloatField(
        label="귀하의 호기일산화탄소를 ppm단위로 입력해주십시오.",
        blank=True,
    )

    systolic_blood_pressure = models.IntegerField(
        label="귀하의 수축기혈압을 입력해주십시오.",
        blank=True,
    )

    diastolic_blood_pressure = models.IntegerField(
        label="귀하의 이완기혈압을 입력해주십시오.",
        blank=True,
    )

    disease_history_1 = models.BooleanField(
        label="구강인두암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_2 = models.BooleanField(
        label="후두암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_3 = models.BooleanField(
        label="식도암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_4 = models.BooleanField(
        label="기관, 기관지 및 폐암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_5 = models.BooleanField(
        label="급성 골수성 백혈병",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_6 = models.BooleanField(
        label="위암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_7 = models.BooleanField(
        label="간암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_8 = models.BooleanField(
        label="췌장암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_9 = models.BooleanField(
        label="신장암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_10 = models.BooleanField(
        label="요관암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_11 = models.BooleanField(
        label="자궁경부암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_12 = models.BooleanField(
        label="방광암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_13 = models.BooleanField(
        label="결직장암",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_14 = models.BooleanField(
        label="뇌졸중",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_15 = models.BooleanField(
        label="실명, 백내장, 노인성 황반변성증",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_16 = models.BooleanField(
        label="모성흡연으로 인한 선천적 결함:구강안면 파열",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_17 = models.BooleanField(
        label="치주염",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_18 = models.BooleanField(
        label="청소년기 대동맥류, 조기 복대동맥죽상경화증",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_19 = models.BooleanField(
        label="관상동맥질환",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_20 = models.BooleanField(
        label="폐렴",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_21 = models.BooleanField(
        label="동맥경화성폐질환 말초혈관질환",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_22 = models.BooleanField(
        label="만성폐쇄성폐질환, 결핵, 천식, 호흡기영향, 비염",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_23 = models.BooleanField(
        label="당뇨",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_24 = models.BooleanField(
        label="여성생식기계영향, 태아발육부진",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_25 = models.BooleanField(
        label="고관절 골절",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_26 = models.BooleanField(
        label="자궁외임신",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_27 = models.BooleanField(
        label="남성 성기능-발기부전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_28 = models.BooleanField(
        label="고혈압",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_29 = models.BooleanField(
        label="류마티스관절염",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_30 = models.BooleanField(
        label="고지혈증",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    disease_history_31 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    drug_in_use = models.StringField(
        label="현재 귀하께서 복용 중인 약물을 입력해주십시오.",
        blank=True,
    )

    did_you_drink_within_the_last_one_year = models.BooleanField(
        label="최근 1년 간 음주경험이 있습니까?",
        choices=Constants.BINARY_POSSESSION,
        widget=widgets.RadioSelectHorizontal,
    )

    drinking_amount_per_drinking_outing = models.IntegerField(
        label="귀하의 1회 음주량을 잔으로 환산하여 입력해주십시오.",
        blank=True,
    )

    drinking_frequency_per_week = models.IntegerField(
        label="귀하는 1주에 몇 회 정도 술을 드십니까?",
        blank=True,
    )
    intense_workout_yes_no = models.BooleanField(
        label="귀하는 주 1회, 10분 이상, 중강도 신체활동을 실천하십니까?",
        choices=Constants.BINARY_POSSESSION,
        widget=widgets.RadioSelectHorizontal,
    )

    type_of_workout = models.StringField(
        label="귀하가 주로 하시는 운동의 종류를 입력해주십시오.",
        blank=True,
    )

    workout_frequency = models.IntegerField(
        label = "일주일에 평균 몇 회 운동하십니까?",
        choices=range(101),
        blank=True,

    )

    workout_minutes_per_time = models.IntegerField(
        label="한 번 운동할 때 평균 몇 분 정도 운동하십니까?",
        blank=True,
    )

    age_of_first_smoking = models.IntegerField(
        label="귀하의 처음흡연연령을 입력해주십시오",
        choices=range(10,101),
        blank=True,
    )

    avg_daily_smoking_amount_in_gaebi = models.IntegerField(
        label="귀하의 하루 평균 흡연량을 개비로 환산하여 선택해주십시오.",
        choices=range(101),
        blank=True,
    )

    total_smoking_years = models.IntegerField(
        label="귀하는 총 몇년간 흡연하셨습니까?",
        choices=range(101),
        blank=True,
    )

    nicotine_patch_adverse_effect = models.IntegerField(
        label="귀하의 니코틴 패치 금기증상 여부를 표시해주십시오.",
        choices=Constants.NICOTINE_PATCH_ADVERSE_EFFECT,
        widget=widgets.RadioSelect,
        blank=True,
    )

    nicotine_patch_adverse_effect_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    tobacco_type_in_use_1 = models.BooleanField(
        label="궐련(일반담배)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_in_use_2 = models.BooleanField(
        label="액상형 전자담배(니코틴 함유)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_in_use_3 = models.BooleanField(
        label="액상형 전자담배(니코틴 미함유)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_in_use_4 = models.BooleanField(
        label="궐련형 전자담배(아이코스,릴,글로 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_in_use_5 = models.BooleanField(
        label="CSV형 전자담배(쥴, 릴 베이퍼 등)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_6 = models.BooleanField(
        label = "머금는 담배(스누스)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_7 = models.BooleanField(
        label = "파이프담배",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_8 = models.BooleanField(
        label = "엽권련(시가)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_9 = models.BooleanField(
        label = "각련(말아피우는 담배)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_10 = models.BooleanField(
        label = "물담배",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_11 = models.BooleanField(
        label = "씹는담배",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_12 = models.BooleanField(
        label = "냄새맡는 담배",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    tobacco_type_in_use_13 = models.BooleanField(
        label = "무응답",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    medical_guarantee = models.IntegerField(
        label="귀하의 의료보장 형태를 선택해주십시오.",
        choices=Constants.MEDICAL_GUARANTEE,
        widget=widgets.RadioSelect,
    )

    highest_schooling = models.IntegerField(
        label="귀하의 최종학력을 선택해주십시오.",
        choices=Constants.HIGHEST_SCHOOLING,
        widget=widgets.RadioSelect,
    )

    occupation = models.IntegerField(
        label="귀하의 직업을 선택해주십시오.",
        choices=Constants.OCCUPATION,
        widget=widgets.RadioSelect,
        blank=True,
    )

    occupation_op = models.StringField(
        label="직업(직접입력)",
        blank=True,
    )

    within_last_one_year_smoking_cessation_tryout_yesno = models.BooleanField(
        label="귀하는 지난 1년 동안 금연 시도를 하셨습니까?",
        choices=Constants.BINARY_CHOICE,
        widget=widgets.RadioSelectHorizontal,
    )

    within_last_one_year_smoking_cessation_tryout_yesno_op_month = models.StringField(
        label="작년 1년동안 가장오랫동안 금연시도를 한 개월수를 입력해주십시오.",
        choices=range(0,13),
        blank=True,
    )

    within_last_one_year_smoking_cessation_tryout_yesno_op_days = models.StringField(
        label="작년 1년동안 가장오랫동안 금연시도를 한 일수 입력해주십시오.",
        choices=range(0, 30),
        blank=True,
    )

    smoking_cessation_method_1 = models.BooleanField(
        label="자기 의지",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_method_2 = models.BooleanField(
        label="보건소 금연클리닉",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_method_3 = models.BooleanField(
        label="지역금연지원센터",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_method_4 = models.BooleanField(
        label="금연상담전화",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_method_5 = models.BooleanField(
        label="병의원 금연치료",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_method_6 = models.StringField(
        label="기타서비스 또는 대체용품 사용(직접입력)",
        blank=True,
    )

    smoking_cessation_failure_reason_1 = models.BooleanField(
        label="본인의 의지가 약해서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_failure_reason_2 = models.BooleanField(
        label="금단증상 때문에",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_failure_reason_3 = models.BooleanField(
        label="스트레스가 쌓여서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_failure_reason_4 = models.BooleanField(
        label="주위의 유혹에 의해서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_failure_reason_5 = models.BooleanField(
        label="금연 후 체중이 늘어서",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_failure_reason_6 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    smoking_cessation_this_time_reason_primary = models.IntegerField(
        label="이번에 금연을 시도하는 첫번째 이유 ",
        choices = Constants.SMOKING_CESSATION_THIS_TIME_REASON,
        widget = widgets.RadioSelect,
        blank = True,
    )

    smoking_cessation_this_time_reason_primary_op = models.StringField(
        label = "기타(직접입력)",
        blank = True,
    )

    smoking_cessation_this_time_reason_secondary = models.IntegerField(
        label = "이번에 금연을 시도하는 두번째 이유 ",
        choices = Constants.SMOKING_CESSATION_THIS_TIME_REASON,
        widget = widgets.RadioSelect,
        blank = True,
    )

    smoking_cessation_this_time_reason_secondary_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    smoking_cessation_this_time_reason_tertiary = models.IntegerField(
        label="이번에 금연을 시도하는 세번째 이유 ",
        choices = Constants.SMOKING_CESSATION_THIS_TIME_REASON,
        widget = widgets.RadioSelect,
        blank = True,
    )

    smoking_cessation_this_time_reason_tertiary_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_3 = models.BooleanField(
        label="식사 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_5 = models.BooleanField(
        label="휴식시간",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/담배를 피우지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_7 = models.BooleanField(
        label="긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_8 = models.BooleanField(
        label="부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_9 = models.BooleanField(
        label="흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_event_to_resist_smoking_desire_10 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    smoking_cessation_motivation = models.IntegerField(
        label="금연은 당신에게 어느 정도 중요합니까?",
        choices=range(11),
        blank=True,
    )

    smoking_cessation_confidence = models.IntegerField(
        label="당신은 금연에 성공할 자신감이 어느 정도 입니까?",
        choices=range(11),
        blank=True,
    )

    smoking_cessation_readiness = models.IntegerField(
        label="당신은 금연할 준비가 어느 정도 되어 있습니까?",
        choices=range(11),
        blank=True,
    )

    morning_smoking_time = models.IntegerField(
        label="아침에 일어나서 얼마 만에 첫 담배를 피우십니까?",
        choices=Constants.TIME_DIVISION,
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_resistancy = models.BooleanField(
        label="금연구역(도서관, 극장, 병원 등)에서 담배를 참기가 어렵습니까?",
        choices=[
            [1, "(1) 예"],
            [2, "(0) 아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    most_tasty_smoking_time = models.BooleanField(
        label="하루 중 담배 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "(1) 아침 첫 담배"],
            [2, "(0) 그 외의 담배"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    how_many_gaebis_per_day = models.IntegerField(
        label="하루에 보통 몇 개비나 피우십니까?",
        choices=[
                [1, "(0) 10개비 이하"],
                [2, "(1) 11~20개비"],
                [3, "(2) 21~30개비"],
                [4, "(3) 31개비 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    morning_smoking_more_than_the_rest_of_day = models.BooleanField(
        label="아침에 일어나서 첫 몇 시간 동안하루 중 다른 시간보다 거 자주 담배를 피우십니까?",
        choices=[
            [1, "(1) 예"],
            [2, "(0) 아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    sick_all_day_still_smoking = models.BooleanField(
        label="몸이 아파 하루 종일 누워있을 때에도 담배를 피우십니까?",
        choices=[
            [1, "(1) 예"],
            [2, "(0) 아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoker_typeA_1 = models.IntegerField(
        label="마음이 조급할 때 여유를 가지기 위해 피운다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeA_2 = models.IntegerField(
        label="집중력을 높이기 위해 피운다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeA_3 = models.IntegerField(
        label="기분 전환을 하려고 피운다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeB_1 = models.IntegerField(
        label="담배, 라이터, 성냥 등을 만지작거리는 버릇이 있다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeB_2 = models.IntegerField(
        label="담배를 꺼내 불을 붙이고 연기를 들이마셨다가 내뿜고 재떨이에 비벼  끄는 과정자체가 좋다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeB_3 = models.IntegerField(
        label="담배 연기로 모양을 만드는 것을 좋아한다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeC_1 = models.IntegerField(
        label="담배를 피우면 마음이 가라앉는다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeC_2 = models.IntegerField(
        label="담배연기를 내뿜으면 나른한 행복감을 느낄 수 있다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeC_3 = models.IntegerField(
        label="마음이 편안할 때면 담배생각이 더 난다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeD_1 = models.IntegerField(
        label="흥분하거나 화가 났을 때 담배를 찾게 된다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeD_2 = models.IntegerField(
        label="불안하고 긴장되면 담배를 피우게 된다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeD_3 = models.IntegerField(
        label="마음이 울적하거나 걱정거리가 있을 때 담배를 피운다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeE_1 = models.IntegerField(
        label="담배가 떨어지면 안절부절 못한다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeE_2 = models.IntegerField(
        label="아무리 바빠도 담배를 거르면 마음 한 구적에 담배생각이 난다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeE_3 = models.IntegerField(
        label="오랫동안 안 피우다가 한 대 피우면 그 순간 불안했던 마음이 사라진다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeF_1 = models.IntegerField(
        label="자신도 모르는 사이에 담배를 물고 있는 것을 발견하곤 한다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeF_2 = models.IntegerField(
        label="특정한 장소(화장실 등)에서는 담배가 당기지 않는데도 흡연하게 된다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeF_3 = models.IntegerField(
        label="특정한 상황(식사 후 등)에서는 담배가 당기지 않는데도 흡연하게 된다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeG_1 = models.IntegerField(
        label="주위 사람들이 흡연하면 나도 담배를 피운다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeG_2 = models.IntegerField(
        label="동료/친구들과 함께 흥겨운 시간을 보낼 때 흡연하게 된다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    smoker_typeG_3 = models.IntegerField(
        label="나는 친구들과 회식이나 모임을 할 때 항상 흡연한다.",
        choices=Constants.TYPE_LICKERT,
        widget=widgets.RadioSelect,
    )

    sm1_1 = make_field_sm(1)
    sm1_2 = make_field_sm(2)
    sm1_3 = make_field_sm(3)
    sm1_4 = make_field_sm(4)
    sm1_5 = make_field_sm(5)
    sm1_6 = make_field_sm(6)
    sm1_7 = make_field_sm(7)

    satisfactory_1 = models.IntegerField(
        label="금연상담사는 상담 약속시간을 잘 지켰습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    satisfactory_2 = models.IntegerField(
        label="금연하는 동안 상담사로부터 도움을 충분히 받았습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    satisfactory_3 = models.IntegerField(
        label="CO측정, 혈압, 체중 등을 충분히 체크를 받으셨습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    satisfactory_4 = models.IntegerField(
        label="금연상담사나 다른 직원들이 친절하게 잘 대해주었습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    satisfactory_5 = models.IntegerField(
        label="방문서비스를 이용하는 것에 불편하였습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    satisfactory_6 = models.IntegerField(
        label="국가금연지원서비스 이용이 금연성공에 얼마나 도움이 되었습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    satisfactory_7 = models.IntegerField(
        label="담배를 피우는 다른 사람에게도 국가금연지원서비스를 이용하도록 권유할 생각이 있습니까?",
        choices=Constants.SATISFACTION_LICKERT,
        widget=widgets.RadioSelect,
    )

    self_reported_health_status = models.IntegerField(
        label="귀하가 생각하는 본인의 현재 건강상태는 어떻습니까?",
        choices=[
            [1, "매우 건강함"],
            [2, "건강한 편"],
            [3, "보통"],
            [4, "허약한 편"],
            [5, "매우 허약함"],
        ],
        widget=widgets.RadioSelect,
    )

    stress_metric_self_reported = models.IntegerField(
        label="평소 귀하의 스트레스 정도는 어떻습니까?",
        choices=[
            [1, "전혀 받지 않음"],
            [2, "별로 받지 않음"],
            [3, "그저 그런 편임 "],
            [4, "약간 받는 편"],
            [5, "매우 많이 받음"],
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





















