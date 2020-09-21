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
from . import smoking_cessation_questions
from datetime import datetime

author = 'Kyubum Moon<mailto:moonx190@umn.edu>'

doc = """
행동강화 물품이 금연동기강화 및 금연유지에 미치는 효과분석 온라인설문
"""


class Constants(BaseConstants):
    name_in_url = 'online_survey'
    players_per_group = None
    num_rounds = 1
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    BINARY_POSSESSION = GlobalConstants.BINARY_POSSESSION
    BORN_YEAR_MIN = 1959
    BORN_YEAR_MAX = 2000
    L5_CHOICES = GlobalConstants.L5_CHOICES
    L52_CHOICES = GlobalConstants.L52_CHOICES
    smoking_type_list = smoking_cessation_questions.SMOKING_TYPE
    subjective_norm_list = smoking_cessation_questions.SUBJECTIVE_NORM
    perceived_behavioral_control_list = smoking_cessation_questions.PERCEIVED_BEHAVIORAL_CONTROL
    attitude_toward_smoking_list = smoking_cessation_questions.ATTITUDE_TOWARD_SMOKING
    intention_list = smoking_cessation_questions.INTENTION
    FULLTIME, PARTTIME, FREELANCER, UNPAID = 1, 2, 3, 99
    JOB_POSITION = [
                        [FULLTIME, "①전일제 근무자"],
                        [PARTTIME, "②파트타임 근무자"],
                        [FREELANCER, "③프리랜서"],
                        [UNPAID, "④최근 6개월 이내 근무경력 없음"]
                    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_lickert(index):
    return models.IntegerField(
        label=Constants.smoking_type_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_lickert_2(index):
    return models.IntegerField(
        label=Constants.attitude_toward_smoking_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L52_CHOICES,
    )


def make_field_lickert_3(index):
    return models.IntegerField(
        label=Constants.subjective_norm_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L52_CHOICES,
    )


def make_field_lickert_4(index):
    return models.IntegerField(
        label=Constants.perceived_behavioral_control_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L52_CHOICES,
    )


def make_field_lickert_5(index):
    return models.IntegerField(
        label=Constants.intention_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L52_CHOICES,
    )


class Player(BasePlayer):
    gender = models.IntegerField(
        label="귀하의 성별은 어떻게 되십니까?",
        choices=[
                    [1, "①남성"],
                    [2, "②여성"],
                ],
        widget=widgets.RadioSelectHorizontal,
    )

    born_year = models.IntegerField(
        label="귀하의 출생년도를 기입해주세요. (대상자: 만20세~59세:2000년생부터 1960년생까지)",
        choices=range(Constants.BORN_YEAR_MAX, Constants.BORN_YEAR_MIN, -1),
    )

    def born_year_error_message(self, value):
        if (value > Constants.BORN_YEAR_MAX or value < Constants.BORN_YEAR_MIN):
            return str.format("태어나신 해는 유효한 네자리 숫자 (가령 {} - {} 사이의 숫자) 로 입력하셔야 합니다.", Constants.BORN_YEAR_MIN,
                              Constants.BORN_YEAR_MAX)

    job_position = models.IntegerField(
        label="직장(일)에서 귀하의 지위는 무엇입니까?",
        choices=Constants.JOB_POSITION,
        widget=widgets.RadioSelect,
    )

    def job_position_error_message(self, value):
        if (value == Constants.UNPAID):
            return str.format(
                "안녕하십니까? 본 연구는 보건복지부의 위탁을 받아 행동강화 물품이 금연동기강화 및 금연유지에 미치는 효과를 연구하기 위한 목적에 따라, 현재 6개월 이상 재직자를 대상으로 연구참여를 제한하게 된 점 양해 부탁드립니다. 감사합니다.")  # todo: 이것을 클릭했을 경우 alert 뜨고 종료로 안내하도록 수정하기

    smoking_in_lifetime_yesno = models.IntegerField(
        label="지금까지 살아오는 동안 담배를 피운 적 있습니까? (여기에서 담배는, 일반 담배(궐련)과 액상형/궐련형 전자담배 모두를 포괄합니다.)",
        choices=[
                    [999, "예. 5갑(100개비) 미만"],
                    [1, "예. 5갑(100개비) 이상"],
                    [9999, "아니오. 피운 적 없음"],
                ],
        widget=widgets.RadioSelect,
    )

    def smoking_in_lifetime_yesno_error_message(self, value):
        if (value == 999 or value == 9999):
            return str.format(
                "안녕하십니까? 본 연구는 보건복지부의 위탁을 받아 행동강화 물품이 금연동기강화 및 금연유지에 미치는 효과를 연구하기 위한 목적에 따라, 5갑(100개비)이상 흡연자를 대상으로 진행되기에 귀하의 연구참여를 제한합니다. ")

    within_past_one_year_smoking_cessation_attempted = models.IntegerField(
        label="최근 1년 동안 담배를 끊고자 하루(24시간) 이상 금연한 적이 있습니까?",
        choices=[
            [1, "예"],
            [99999, "아니오"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    def within_past_one_year_smoking_cessation_attempted_error_message(self, value):
        if (value == 99999):
            return str.format(
                "본 연구는 보건복지부의 위탁을 받아 행동강화물품이 금연동기강화 및 금연유지에 미치는 효과를 연구하기 위한 목적에 따라, 최근 1년 동안 담배를 끊고자 하루(24시간) 이상 금연한 적이 있는 분들만을 대상으로 하는 연구입니다. 따라서 귀하의 연구 참가를 제한합니다.")

    region = models.IntegerField(
        label="귀하의 거주 지역을 선택해주세요.",
        choices=[
                    [1, "①서울"],
                    [2, "②인천"],
                    [3, "③경기도"],
                    [4, "④강원도"],
                    [5, "⑤세종"],
                    [6, "⑥충청남도"],
                    [7, "⑦충청북도"],
                    [8, "⑧대전"],
                    [9, "⑨대구"],
                    [10, "⑩경상북도"],
                    [11, "⑪경상남도"],
                    [12, "⑫울산"],
                    [13, "⑬부산"],
                    [14, "⑭전라북도"],
                    [15, "⑮전라남도"],
                    [16, "⑯광주"],
                    [17, "⑰제주도"],
                ],
        widget=widgets.RadioSelect,
    )

    region_size = models.IntegerField(
        label="귀하의 거주지의 지역규모를 선택해주세요.",
        choices=[
                    [1, "①대도시(특별/광역시-서울, 부산, 대구, 인천, 광주, 대전, 울산)"],
                    [2, "②중소도시(특별/광역시가 아닌 그 외 지역)"],
                    [3, "③읍면지역(ex. ○○시 ○○읍/면)"],
                    [4, "④특수지역(도서·벽지 지역)"],
        ],
        widget=widgets.RadioSelect,
    )

    marriage = models.IntegerField(
        label="귀하의 혼인상태를 선택해주십시오",
        choices=[
            [1, "결혼안함"],
            [2, "결혼함"],
            [3, "이혼/사별함"],
            [4, "기타"],
        ],
        widget=widgets.RadioSelect,
    )

    final_schooling = models.IntegerField(
        label="귀하의 최종 학력을 선택해주세요",
        choices=[
                    [1, "①무학"],
                    [2, "②초등학교 졸업이하"],
                    [3, "③중학교 졸업이하"],
                    [4, "④고등학교 졸업이하"],
                    [5, "⑤전문대/대학교 졸업이하"],
                    [6, "⑥대학원 수료이상"],
        ],
        widget=widgets.RadioSelect,
    )

    occupation = models.IntegerField(
        label="귀하의 직업을 선택해주세요",
        choices=[
                    [1, "①관리자"],
                    [2, "②전문가 및 관련종사자"],
                    [3, "③사무 종사자"],
                    [4, "④서비스 종사자"],
                    [5, "⑤판매 종사자"],
                    [6, "⑥농림어업 숙련 종사자"],
                    [7, "⑦기능 및 관련기능 종사자"],
                    [8, "⑧장치, 기계조작 및 조립 종사자"],
                    [9, "⑨ 단순 노무 종사자"],
                    [10,"⑩군인"],
                    [11, "⑭기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )

    occupation_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    firm_type = models.IntegerField(
        label="귀하께서 현재 근무하시는 기업의 유형은 다음 중 무엇입니까?",
        choices=[
                    [1, "①공기업·준정부기관·기타 공공기관"],
                    [2, "②공무원"],
                    [3, "③사기업-규모별: 대기업"],
                    [4, "④사기업-규모별: 중견기업"],
                    [5, "⑤사기업-규모별: 중소·벤처기업"],
                    [6, "⑥사기업-규모별: 소기업 및 소상공인"],
                    [7, "⑦기타(위에 해당하지 않는 경우 자유 입력: )"],
                ],
        widget=widgets.RadioSelect,
    )

    firm_type_op = models.StringField(
        label="기타(위에 해당하지 않는 경우 자유 입력)",
        blank=True,
    )

    firm_size = models.IntegerField(
        label="현재 근무하시는 사업장 규모를 다음 중 선택해주십시오",
        choices=[
                    [1, "①5인 미만"],
                    [2, "②5인 이상~50인 미만"],
                    [3, "③50인 이상~100인 미만"],
                    [4, "④100인 이상~200인 미만"],
                    [5, "⑤200인 이상~300인 미만"],
                    [6, "⑥300인 이상"],
                ],
        widget=widgets.RadioSelect,
    )

    household_income = models.IntegerField(
        label="최근 6개월 평균 가구소득액(즉, 가족구성원 전체의 수입 합산액)은 어떻게 되십니까? 월별 세후 실질 수령액 기준으로 선택해 주십시오.",
        choices=[
                    [1, "①없음"],
                    [2, "②150만원 미만"],
                    [3, "③150만원 이상 300만원 미만"],
                    [4, "④300만원 이상 450만원 미만"],
                    [5, "⑤450만원 이상 600만원 미만"],
                    [6, "⑥600만원 이상 750만원 미만"],
                    [7, "⑦750만원 이상"],
                ],
        widget=widgets.RadioSelect,
    )

    num_drink_not = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    drink_freq_1 = models.IntegerField(
        label="일주일에 (__)회",
        choices=range(1, 8),
        blank=True,
    )

    alc_avg_1_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    mid_act_yesno = models.BooleanField(
        label="",
        choices=Constants.BINARY_POSSESSION,
        widget=widgets.RadioSelectHorizontal,
    )

    mid_act_type = models.StringField(
        label="",
        blank=True,
    )
    mid_act_day = models.IntegerField(
        label="",
        choices=range(1, 8),
    )

    mid_act_min = models.IntegerField(
        label="",
        choices=[
            [1, "00"],
            [2, "15"],
            [3, "30"],
            [4, "45"],
            [5, "60"],
            [6, "75"],
            [7, "90"],
            [8, "105"],
            [9, "120"],
            [10, "135"],
            [11, "150"],
            [12, "165"],
            [13, "180"],
            [14, "195"],
            [15, "210"],
            [16, "225"],
            [17, "240"],
            [18, "240+"],
        ],
    )

    overall_health_evaluation = models.IntegerField(
        label="귀하가 생각하는 본인의 현재 건강상태는 어떻습니까?",
        choices=range(0, 11),
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )
    overall_stress_evaluation = models.IntegerField(
        label="평소 귀하의 스트레스 정도는 어떻습니까?",
        choices=range(0, 11),
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )

    tobacco_product_in_use_1 = models.BooleanField(
        label="궐련(일반담배)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_2 = models.BooleanField(
        label="액상형 전자담배(니코틴 함유)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_3 = models.BooleanField(
        label="액상형 전자담배(니코틴 미함유)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_4 = models.BooleanField(
        label="궐련형 전자담배(아이코스,릴,글로 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_5 = models.BooleanField(
        label="CSV형 전자담배(쥴, 릴 베이퍼 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_6 = models.BooleanField(
        label="머금는 담배(스누스)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_7 = models.BooleanField(
        label="파이프담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_8 = models.BooleanField(
        label="엽권련(시가)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_9 = models.BooleanField(
        label="각련(말아피우는 담배)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_10 = models.BooleanField(
        label="물담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_11 = models.BooleanField(
        label="씹는담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_product_in_use_12 = models.BooleanField(
        label="냄새맡는 담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    do_you_smoke_tobacco = models.IntegerField(
        label="현재 일반담배(궐련)를 피우십니까?",
        choices=[
            [1, "매일피움"],
            [2, "가끔피움"],
            [3, "과거엔 피웠으나, 현재 피우지 않음"],
            [4, "과거에도, 현재에도 피운 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    first_time_to_finish_one_stick_of_tobacco = models.IntegerField(
        label="처음으로 일반담배(궐련) 한 개비를 다 피운 시기는 언제입니까? (만나이로 대답해주시기 바랍니다.)",
        choices=range(100),
        blank=True,
    )

    first_time_to_finish_one_stick_or_more = models.IntegerField(
        label="매일 한 개비 이상의 일반담배(궐련)를 피운 시기는 언제입니까? (만나이로 대답해주시기 바랍니다.)",
        choices=range(100),
        blank=True,
    )

    avg_daily_tobacco_smoking_amount = models.IntegerField(
        label="하루 평균 일반담배(궐련) 흡연량(기준: 개비)",
        blank=True,
    )

    within_past_month_tobacco_smoking_days = models.IntegerField(
        label="최근 1달 간 일반담배(궐련) 흡연일수",
        choices=range(1, 31),
        blank=True,
    )

    tobacco_sticks_per_day = models.IntegerField(
        label="일반담배(궐련)를 흡연한 날 하루 평균 흡연량(기준: 개비)",
        choices=range(101),
        blank=True,
    )

    past_tobacco_smoking_years = models.IntegerField(
        label="",
        choices=range(101),
        blank=True,
    )
    past_tobacco_smoking_months = models.IntegerField(
        label="",
        choices=range(12),
        blank=True,
    )
    past_tobacco_sticks_per_day = models.IntegerField(
        label="과거 일반담배(궐련)를 피울 때 하루 평균 흡연량(기준: 개비)",
        choices=range(101),
        blank=True,
    )

    hardest_time_to_resist_smoking_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_3 = models.BooleanField(
        label="식사",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_5 = models.BooleanField(
        label="휴식시",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/담배를 피우지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때 등",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_7 = models.BooleanField(
        label="긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_8 = models.BooleanField(
        label="부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_9 = models.BooleanField(
        label="흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_10 = models.BooleanField(
        label="흡연을 참기 힘들지 않음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    hardest_time_to_resist_smoking_11 = models.StringField(
        label="기타",
        blank=True,
    )

    first_tobacco_of_the_day = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 일반담배(궐련)를 피우십니까?",
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ],
        widget=widgets.RadioSelect,
    )

    is_it_hard_to_resist_smoking_in_the_public = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 일반담배(궐련)를 참기가 어렵습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    when_is_tobacco_the_most_tasty = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 하루 중 일반담배(궐련) 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "아침 첫 담배"],
            [0, "그 외의 담배"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    number_of_sticks_per_day_in_the_past = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 하루에 보통 몇 개비나 피우십니까?",
        choices=[
            [1, "10개비 이하"],
            [2, "11~20개비"],
            [3, "21~30개비"],
            [4, "31개비 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    is_morning_tobacco_more_tasty_than_the_rest = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 일반담배(궐련)를 피우십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    sick_all_day_still_smoking = models.BooleanField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 일반담배(궐련)를 피우십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    do_you_use_liquid_cigarette = models.IntegerField(
        label="귀하께서는 현재 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=[
            [1, "매일 사용"],
            [2, "가끔 사용"],
            [3, "과거엔 사용했으나, 현재는 사용하지 않음"],
            [4, "과거에도 , 현재에도 사용한 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    liquid_cigarette_start_year = models.IntegerField(
        label="",
        choices=range(2000,int(datetime.now().strftime('%Y'))+1),
        blank=True,
    )

    liquid_cigarette_start_month = models.IntegerField(
        label="",
        choices=range(1, int(datetime.now().strftime('%m'))+1),
        blank=True,
    )

    liquid_cigarette_end_year = models.IntegerField(
        label = "",
        choices = range(2000, int(datetime.now().strftime('%Y')) + 1),
        blank = True,
    )
    liquid_cigarette_end_month = models.IntegerField(
        label="",
        choices=range(1, int(datetime.now().strftime('%m'))+1),
        blank=True,
    )

    most_recent_month_liquid_cigarette_use_days = models.IntegerField(
        label="최근 1달 간 액상형 전자담배(쥴, 탱크형 등) 사용일수",
        choices=range(1, 31),
        blank=True,
    )

    liquid_amount_of_liquid_cigarette_recent_week = models.IntegerField(
        label="",
        choices=range(101),
        blank=True,
    )

    liquid_cigarette_density = models.IntegerField(
        label="귀하가 현재 사용하는 또는 과거에 사용한 액상형 전자담배(쥴, 탱크형 등) 액상의 니코틴 농도(액상 1ml 기준 니코틴 함유량)는 얼마입니까? (1mg/ml=0.1%)",
        choices=[
            [1, "니코틴 없음"],
            [2, "1~6mg/ml"],
            [3, "7~12mg/ml"],
            [4, "13~18mg/ml"],
            [5, "19mg/ml 이상"],
            [6, "잘 모름"],
        ],
        widget=widgets.RadioSelect,
    )

    liquid_cigarette_hardest_to_resist_when_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_3 = models.BooleanField(
        label="식사 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_5 = models.BooleanField(
        label="휴식시간",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/전자담배를 사용하지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_7 = models.BooleanField(
        label="긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_8 = models.BooleanField(
        label="부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_9 = models.BooleanField(
        label="흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때 ",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_10 = models.BooleanField(
        label="사용을 참기 힘들지 않음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    liquid_cigarette_hardest_to_resist_when_11 = models.StringField(
        label="기타(직접입력:)",
        blank=True,
    )

    liquid_cigarette_first_in_the_day = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ],
        widget=widgets.RadioSelect,
    )

    is_it_hard_to_resist_smoking_liquid_cigarette_in_public = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 액상형 전자담배(쥴, 탱크형 등)를 참기가 어렵습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    when_is_the_liquid_cigarette_the_most_tasty = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 하루 중 액상형 전자담배(쥴, 탱크형 등) 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "아침 첫 사용시기"],
            [0, "그 외의 사용시기"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    liquid_cigarette_use_frequency_per_day = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 하루에 보통 몇 번 사용하십니까?",
        choices=[
            [0, "10회 이하"],
            [1, "11~20회"],
            [2, "21~30회"],
            [3, "31회 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    liquid_cigarette_morning_is_more_tasty_than_the_rest = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    liquid_cigarette_sick_all_day_still_smoking = models.BooleanField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    do_you_use_tobacco_type_e_cigarette = models.IntegerField(
        label="현재 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=[
            [1, "매일 사용함"],
            [2, "가끔 사용함"],
            [3, "과거엔 사용했었으나, 현재는 사용하지 않음"],
            [4, "과거에도 , 현재에도 사용한 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    tobacco_type_e_cigarette_start_year = models.IntegerField(
        label="",
        choices=range(2000, int(datetime.now().strftime('%Y')) + 1),
        blank=True,
    )
    tobacco_type_e_cigarette_start_month = models.IntegerField(
        label="",
        choices=range(1, int(datetime.now().strftime('%m')) + 1),
        blank=True,
    )

    tobacco_type_e_cigarette_end_year = models.IntegerField(
        label="",
        choices=range(2000, int(datetime.now().strftime('%Y')) + 1),
        blank=True,
    )
    tobacco_type_e_cigarette_end_month = models.IntegerField(
        label="",
        choices=range(1, int(datetime.now().strftime('%m')) + 1),
        blank=True,
    )

    within_recent_month_days_of_use_for_tobacco_type_e_cigarette = models.IntegerField(
        label="",
        choices=range(1, 31),
        blank=True,
    )

    tobacco_type_e_cigarette_avg_sticks_per_day = models.IntegerField(
        label="",
        choices=range(1, 101),
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_1 = models.BooleanField(
        label="아침에 일어나자마자",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_2 = models.BooleanField(
        label="잠들기 전",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_3 = models.BooleanField(
        label="식사 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_4 = models.BooleanField(
        label="화장실에서/샤워 후",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_5 = models.BooleanField(
        label="휴식시간",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_6 = models.BooleanField(
        label="습관적 상황에서 (활력이 필요할 때/전자담배를 사용하지 않음을 깨달을 때, 술/커피마실 때, 혼자 있거나 무언가 기다릴 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_7 = models.BooleanField(
        label="긍정적 상황 (친구나 가족과 함께 있을 때, 대화나 피로를 풀 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_8 = models.BooleanField(
        label="부정적 상황 (스트레스 받을 때, 일이 뜻대로 안될 때, 화날 때 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_9 = models.BooleanField(
        label="흡연자와 같이 있거나, TV의 배우 또는 주위 흡연자의 모습을 보았을 때",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_10 = models.BooleanField(
        label="사용을 참기 힘들지 않음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_e_cigarette_hardest_to_resist_when_11 = models.StringField(
        label="기타",
        blank=True,
    )

    tobacco_type_e_cigarette_first_in_the_day = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ],
        widget=widgets.RadioSelect,
    )

    tobacco_type_e_cigarette_hard_to_resist_in_public = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 참기가 어렵습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    tobacco_type_e_cigarette_most_tasty_in_the_day = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 하루 중 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 맛이 가장 좋은 때는 언제입니까?",
        choices=[
            [1, "아침 첫 사용 시기"],
            [0, "그 외의 사용 시기"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    tobacco_type_e_cigarette_sticks_per_day = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 하루에 보통 몇 개비를 사용하십니까?",
        choices=[
            [1, "10개비 이하"],
            [2, "11~20개비"],
            [3, "21~30개비"],
            [4, "31개비 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    tobacco_e_cig_more_tasty_in_the_morning = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    tobacco_type_e_cigarette_sick_all_day_still_smoking = models.BooleanField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_attempt_count = models.IntegerField(
        label="귀하께서는 금연 시도 경험이 있다고 답변하신 바 있습니다. 지금까지 금연 시도를 몇 번 정도 시도하셨습니까?",
        choices=[
            [1, "① 1회"],
            [2, "② 2회"],
            [3, "③ 3회"],
            [4, "④ 4회"],
            [5, "⑤ 5회 이상"],
        ],
        widget=widgets.RadioSelect,
    )

    within_one_month_do_you_plan_to_quit_smoking = models.IntegerField(
        label="앞으로 1개월 안에 담배를 끊을 계획이 있습니까?",
        choices=[
            [1, "1개월내 금연할 계획이 있음"],
            [2, "6개월내 금연할 계획이 있음"],
            [3, "6개월내 아니지만 언젠가 금연생각 있음"],
            [4, "현재 전혀 금연 생각 없음"],
            [5, "현재 금연중임"],
        ],
        widget=widgets.RadioSelect,
    )

    within_past_five_days_last_time_to_use_nicotine_alternatives = models.IntegerField(
        label="최근 5일 동안 니코틴 패치, 니코틴 껌, 니코틴 사탕 등의 니코틴 대체용품을 마지막으로 사용한 때는 언제입니까?",
        choices=[
            [1, "①오늘 사용"],
            [2, "②1일 전 사용"],
            [3, "③2일 전 사용"],
            [4, "④3~5일전사용"],
            [5, "⑤최근 5일 동안 사용하지 않음"],
            [6, "⑥지금까지 사용해본 적 없음"],
        ],
        widget=widgets.RadioSelect,
    )

    ate_food_products_when_smoking_desire_arose = models.IntegerField(
        label="담배가 피우고 싶을 때 식품류 (껌, 사탕, 비타민)를 대신 먹었음	",
        choices=[
                    [1, "①오늘 사용"],
                    [2, "②1일 전 사용"],
                    [3, "③2일 전 사용"],
                    [4, "④3~5일전사용"],
                    [5, "⑤최근 5일 동안 사용하지 않음"],
                ],
        widget=widgets.RadioSelect,
    )

    effect_of_food_product_in_resisting_smoking_desire = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    drink_water_when_desiring_to_smoke = models.IntegerField(
        label="담배가 피우고 싶을 때 물을마심",
        choices=[
                    [1, "①오늘 사용"],
                    [2, "②1일 전 사용"],
                    [3, "③2일 전 사용"],
                    [4, "④3~5일전사용"],
                    [5, "⑤최근 5일 동안 사용하지 않음"],
                ],
        widget=widgets.RadioSelect,
    )

    effect_of_water_in_resisting_smoking_desire = models.IntegerField(
        label="",
        choices=[
                    [1, "0"],
                    [2, "1"],
                    [3, "2"],
                    [4, "3"],
                    [5, "4"],
                    [6, "5"],
                    [7, "6"],
                    [8, "7"],
                    [9, "8"],
                    [10, "9"],
                    [11, "10"],
                ],
        widget=widgets.RadioSelectHorizontal,
    )

    pressure_tool_when_desiring_to_smoke = models.IntegerField(
        label="담배가 피우고 싶을 때 지압기와 같은 몸에 자극을 줄 수 있는 기구로 자극을 줌",
        choices=[
                    [1, "①오늘 사용"],
                    [2, "②1일 전 사용"],
                    [3, "③2일 전 사용"],
                    [4, "④3~5일전사용"],
                    [5, "⑤최근 5일 동안 사용하지 않음"],
                ],
        widget=widgets.RadioSelect,
    )

    effect_of_pressure_tool_in_resisting_smoking_desire = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    mouth_wash_when_resisting_smoking_desire = models.IntegerField(
        label="담배가 피우고 싶을 때 구강청결제 (가그린, 양치질등) 등을 대신함",
        choices=[
                    [1, "①오늘 사용"],
                    [2, "②1일 전 사용"],
                    [3, "③2일 전 사용"],
                    [4, "④3~5일전사용"],
                    [5, "⑤최근 5일 동안 사용하지 않음"],
                ],
        widget=widgets.RadioSelect,
    )

    effect_of_mouth_wash_in_resisting_smoking_desire = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    aroma_pipe_or_change_stick_when_resisting_smoking_desire = models.IntegerField(
        label="담배가 피우고 싶을 때 아로마파이프나 체인지스틱 같은 흡연욕구저하제를 대신 사용함	",
        choices=[
                    [1, "①오늘 사용"],
                    [2, "②1일 전 사용"],
                    [3, "③2일 전 사용"],
                    [4, "④3~5일전사용"],
                    [5, "⑤최근 5일 동안 사용하지 않음"],
                ],
        widget=widgets.RadioSelect,
    )

    effect_of_aroma_stick_against_smoking_desire = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_self_will = models.BooleanField(
        label="금연방법: 의지로",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_call_center = models.BooleanField(
        label="금연방법: 금연상담전화(금연콜센터)",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_clinic = models.BooleanField(
        label="금연방법: 보건소금연클리닉",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_pharmaceuticals = models.BooleanField(
        label="금연방법: 약국에서 본인 스스로 니코틴대체용품 (니코틴껌, 패치, 사탕) 구입",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_champix = models.BooleanField(
        label="금연방법: 병의원을 통해 금연치료약으로 금연 (챔픽스 등)",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_internet = models.BooleanField(
        label="금연방법: 인터넷, 금연길라잡이",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_method_other = models.BooleanField(
        label="금연방법: 기타",
        choices=[
            [0, "아니오"],
            [1, "예"],
        ],
        widget=widgets.RadioSelectHorizontal,
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

    smoking_cessation_failure_reason_6 = models.BooleanField(
        label="금연 실패한 경험 없음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_failure_reason_7 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    reason_to_quit_smoking_this_time_primary = models.IntegerField(
        label="이번에 담배를 끊고 싶은 첫번째 이유",
        choices=[
            [1, "가족 혹은 주변사람들의 권유"],
            [2, "개인의 건강을 위해(현재 질병악화 및 장래 질병발생예방)"],
            [3, "담뱃값 인상 등 경제적 이유"],
            [4, "금연구역 확대 등 환경적 이유"],
            [5, "깨끗한 이미지 관리를 위해서(예: 입 냄새가 고약, 옷에 담배 냄새가 뱀)"],
            [6, "나의 흡연으로 주위사람 건강에 나쁜 영향을 미치는 것을 방지하기 위해서"],
            [7, "금연의지를 보여주기 위해"],
            [8, "흡연자에 대한 사회적 시선 때문"],
            [9, "현재 금연 의사가 없음"],
            [10, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )

    reason_to_quit_smoking_this_time_primary_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    reason_to_quit_smoking_this_time_secondary = models.IntegerField(
        label="이번에 담배를 끊고 싶은 두번째 이유",
        choices=[
            [1, "가족 혹은 주변사람들의 권유"],
            [2, "개인의 건강을 위해(현재 질병악화 및 장래 질병발생예방)"],
            [3, "담뱃값 인상 등 경제적 이유"],
            [4, "금연구역 확대 등 환경적 이유"],
            [5, "깨끗한 이미지 관리를 위해서(예: 입 냄새가 고약, 옷에 담배 냄새가 뱀)"],
            [6, "나의 흡연으로 주위사람 건강에 나쁜 영향을 미치는 것을 방지하기 위해서"],
            [7, "금연의지를 보여주기 위해"],
            [8, "흡연자에 대한 사회적 시선 때문"],
            [9, "현재 금연 의사가 없음"],
            [10, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )

    reason_to_quit_smoking_this_time_secondary_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    reason_to_quit_smoking_this_time_tertiary = models.IntegerField(
        label="이번에 담배를 끊고 싶은 세번째 이유",
        choices=[
            [1, "가족 혹은 주변사람들의 권유"],
            [2, "개인의 건강을 위해(현재 질병악화 및 장래 질병발생예방)"],
            [3, "담뱃값 인상 등 경제적 이유"],
            [4, "금연구역 확대 등 환경적 이유"],
            [5, "깨끗한 이미지 관리를 위해서(예: 입 냄새가 고약, 옷에 담배 냄새가 뱀)"],
            [6, "나의 흡연으로 주위사람 건강에 나쁜 영향을 미치는 것을 방지하기 위해서"],
            [7, "금연의지를 보여주기 위해"],
            [8, "흡연자에 대한 사회적 시선 때문"],
            [9, "현재 금연 의사가 없음"],
            [10, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )

    reason_to_quit_smoking_this_time_tertiary_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

    smoking_cessation_helper_1 = models.BooleanField(
        label="부모/조부모",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_2 = models.BooleanField(
        label="형제자매",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_3 = models.BooleanField(
        label="배우자/애인",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_4 = models.BooleanField(
        label="자녀",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_5 = models.BooleanField(
        label="친구/선후배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_6 = models.BooleanField(
        label="직장동료",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_7 = models.BooleanField(
        label="교사",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_8 = models.BooleanField(
        label="의료인",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_9 = models.BooleanField(
        label="없음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    smoking_cessation_helper_10 = models.StringField(
        label="기타(직접입력:)",
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
        label="기타",
        blank=True,
    )

    smoking_cessation_importance = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_confidence = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    smoking_cessation_readiness = models.IntegerField(
        label="",
        choices=[
            [1, "0"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    def vars_for_template(self) -> dict:
        vars_to_return = {'L5': [i[1] for i in Constants.L5_CHOICES], 'L52': [i[1] for i in Constants.L52_CHOICES]}
        return vars_to_return

    st_1 = make_field_lickert(0)
    st_2 = make_field_lickert(1)
    st_3 = make_field_lickert(2)
    st_4 = make_field_lickert(3)
    st_5 = make_field_lickert(4)
    st_6 = make_field_lickert(5)
    st_7 = make_field_lickert(6)
    st_8 = make_field_lickert(7)
    st_9 = make_field_lickert(8)
    st_10 = make_field_lickert(9)
    st_11 = make_field_lickert(10)
    st_12 = make_field_lickert(11)
    st_13 = make_field_lickert(12)
    st_14 = make_field_lickert(13)
    st_15 = make_field_lickert(14)
    st_16 = make_field_lickert(15)
    st_17 = make_field_lickert(16)
    st_18 = make_field_lickert(17)
    st_19 = make_field_lickert(18)
    st_20 = make_field_lickert(19)
    st_21 = make_field_lickert(20)

    sa_1 = make_field_lickert_2(0)
    sa_2 = make_field_lickert_2(1)
    sa_3 = make_field_lickert_2(2)
    sa_4 = make_field_lickert_2(3)
    sa_5 = make_field_lickert_2(4)
    sa_6 = make_field_lickert_2(5)
    sa_7 = make_field_lickert_2(6)
    sa_8 = make_field_lickert_2(7)

    sn_1 = make_field_lickert_3(0)
    sn_2 = make_field_lickert_3(1)

    pbc_1 = make_field_lickert_4(0)
    pbc_2 = make_field_lickert_4(1)

    i_1 = make_field_lickert_5(0)
    i_2 = make_field_lickert_5(1)
    i_3 = make_field_lickert_5(2)
    i_4 = make_field_lickert_5(3)
